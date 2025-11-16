"""
Simple Resume-to-Job Matching using SBERT Embeddings
No LLM needed - pure semantic similarity matching
"""

# TensorFlow compatibility issues 
import os
os.environ['USE_TF'] = '0'  # Disable TensorFlow backend
os.environ['USE_TORCH'] = '1'  # Use PyTorch backend
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings

import pandas as pd
import numpy as np
print("imported np")
from sentence_transformers import SentenceTransformer
print("imported transformer")
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm


# 1. Load SBERT Model

print("Loading SBERT model...")
model = SentenceTransformer('all-MiniLM-L6-v2')


# 2. Load Data

print("Loading job descriptions...")
jd_df = pd.read_excel('1_data_cleaning/filtered_jd_sections2.xlsx')
print(f"Loaded {len(jd_df)} job descriptions")

print("\nLoading resumes...")
resume_df = pd.read_csv('0_raw_dataset/resumes.csv')
print(f"Loaded {len(resume_df)} resumes")


# 3. Create Job Description Text 

def create_job_semantic_text(row):
    """
    Combine all job fields into a rich semantic description
    This matches the approach in jd_embedding.ipynb
    """
    return f"""This job, titled {row['job_title']} and located in {row['location_cleaned']}, involves {row['jd_duties']}.
The role description states: {row['job_description']}.
Applicants are expected to meet the following requirements: {row['jd_requirements']}.
The position lists the following educational background: {row['jd_education']}."""

print("\nCreating job semantic texts...")
jd_df['job_semantic_text'] = jd_df.apply(create_job_semantic_text, axis=1)


# 4. Create Resume Text

def create_resume_semantic_text(row):
    """
    Combine all resume fields into a rich semantic description
    """
    return f"""Resume for {row['Resume Title']}.
Introduction: {row['Introduction']}.
Work Experience: {row['Work Experience']}.
Education: {row['Education']}.
Skills: {row['Skills']}.
Additional Information: {row['Additional Information']}."""

print("Creating resume semantic texts...")
resume_df['resume_semantic_text'] = resume_df.apply(create_resume_semantic_text, axis=1)


# 5. Generate Embeddings

print("\nGenerating job embeddings...")
job_embeddings = model.encode(
    jd_df['job_semantic_text'].tolist(),
    show_progress_bar=True,
    batch_size=32
)
print(f"Job embeddings shape: {job_embeddings.shape}")

print("\nGenerating resume embeddings...")
resume_embeddings = model.encode(
    resume_df['resume_semantic_text'].tolist(),
    show_progress_bar=True,
    batch_size=32
)
print(f"Resume embeddings shape: {resume_embeddings.shape}")


# 6. Find Top 3 Matches for Each Resume

print("\nFinding top 3 job matches for each resume...")

results = []

for resume_idx in tqdm(range(len(resume_df)), desc="Matching resumes"):
    # Get resume embedding
    resume_emb = resume_embeddings[resume_idx].reshape(1, -1)

    # Compute cosine similarity with all jobs
    similarities = cosine_similarity(resume_emb, job_embeddings)[0]

    # Get top 3 job indices
    top3_indices = np.argsort(similarities)[::-1][:3]

    # Create result record
    result = {
        'resume_id': resume_df.iloc[resume_idx]['Uniq Id'],
        'resume_title': resume_df.iloc[resume_idx]['Resume Title'],
    }

    # Add top 3 matches
    for rank, job_idx in enumerate(top3_indices, start=1):
        result[f'top{rank}_job_title'] = jd_df.iloc[job_idx]['job_title']
        result[f'top{rank}_location'] = jd_df.iloc[job_idx]['location_cleaned']
        result[f'top{rank}_similarity'] = float(similarities[job_idx])
        result[f'top{rank}_job_description'] = jd_df.iloc[job_idx]['job_description'][:200] + '...'

    results.append(result)

# 7. Save Results

results_df = pd.DataFrame(results)
output_file = '5_checking_accuracy/resume_job_matching_simple.xlsx'
results_df.to_excel(output_file, index=False)

print(f"\n✓ Results saved to {output_file}")
print(f"✓ Matched {len(resume_df)} resumes to jobs")
print(f"✓ Average top-1 similarity: {results_df['top1_similarity'].mean():.3f}")
print(f"✓ Average top-3 similarity: {results_df['top3_similarity'].mean():.3f}")


# 8. Display Sample Results

print("\n" + "="*80)
print("SAMPLE RESULTS")
print("="*80)

for i in range(min(3, len(results_df))):
    print(f"\n--- Resume {i+1}: {results_df.iloc[i]['resume_title']} ---")
    for rank in range(1, 4):
        print(f"\n  Top {rank} Match (similarity: {results_df.iloc[i][f'top{rank}_similarity']:.3f}):")
        print(f"    Job: {results_df.iloc[i][f'top{rank}_job_title']}")
        print(f"    Location: {results_df.iloc[i][f'top{rank}_location']}")
