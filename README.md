# Cross-Domain Job Matching: Transformer-based Semantic Retrieval

A semantic job matching system that uses transformer-based embeddings to match resumes with job descriptions, going beyond traditional keyword-based approaches.

**Team Members:** Cindy Gao, Cynthia Zhou, Jenny Wu
**Course:** MIDS F25 - Introduction to NLP

## Project Overview

This project formulates resume-job matching as a **cross-domain semantic retrieval problem**. Given a resume, the system identifies the most semantically similar job descriptions and predicts the **top-3 combinations of job field, title, and location** that best align with the candidate's background.

### Key Features

- **Semantic Understanding**: Uses Sentence-BERT (SBERT) to capture semantic meaning beyond keyword matching
- **Content-Based Matching**: Focuses on job duties and requirements rather than just job titles
- **Cross-Encoder Re-ranking**: Optional re-ranking layer for improved precision
- **Context-Aware Retrieval**: Jointly embeds job field, title, and location for nuanced matching

## Project Structure

```
.
├── 0_raw_dataset/              # Raw datasets from Kaggle
├── 1_data_cleaning/            # Data preprocessing and cleaning
├── 2_embeddings/               # Baseline and cross-encoder embeddings
├── 3_fine_tuning/              # Model fine-tuning notebooks
├── 4_model_outputs/            # Model predictions and results
├── 5_checking_accuracy/        # Evaluation and accuracy checking
├── 6_archives/                 # Archived experiments
├── requirements.txt            # Python dependencies
└── README.md                   
```
### Key Notebooks

- `1_data_cleaning/11_cleaning_jd.ipynb` - Clean and structure job descriptions
- `1_data_cleaning/12_clearning_resume.ipynb` - Parse and clean resume data
- `2_embeddings/basemodel_embedding.ipynb` - Generate baseline SBERT embeddings
- `3_fine_tuning/1b_create_content_based_pairs.ipynb` - Create content-focused training pairs
- `3_fine_tuning/2b_finetune_content_based.ipynb` - Fine-tune SBERT model

### Output Files

- `4_model_outputs/baseline_outputs.csv` - Baseline model predictions
- `4_model_outputs/crossencoder_outputs.csv` - Cross-encoder predictions
- `5_checking_accuracy/job_match_results.csv` - Evaluation results with ground truth comparison

## Datasets

1. **Job Descriptions**: [US Jobs on Monster.com](https://www.kaggle.com/datasets/PromptCloudHQ/us-jobs-on-monstercom/data) (1,231 jobs after cleaning)
2. **Resumes**: [Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset) (100 test resumes)

The job descriptions provide structured information (title, field, location) after preprocessing, while resumes contain unstructured skill sets and experience.

## Methodology

### 1. Data Cleaning (`1_data_cleaning/`)

- **Job Descriptions**: Extract and structure duties, requirements, and education sections
- **Resumes**: Parse career objectives, skills, education, and work experience
- Clean location data and normalize job titles

### 2. Baseline Embeddings (`2_embeddings/`)

Generate semantic embeddings using pre-trained models:
- **Base Model**: `all-MiniLM-L6-v2`
- Create structured semantic sentences for both resumes and job descriptions
- Compute cosine similarity for retrieval

### 3. Fine-Tuning (`3_fine_tuning/`)

**Content-Based Training Pairs**:
- **Positive Pairs**: High skill overlap (≥0.4) and content similarity (≥0.5), allowing different job titles
- **Negative Pairs**: Similar keywords but low skill overlap (<0.25) - "hard negatives"
- Training set: 6,000 pairs (3,000 positive, 3,000 negative)
- Split: 70% train / 15% validation / 15% test

**Fine-tuning Strategy**:
- Use contrastive/triplet loss to separate semantically different jobs
- Focus on content (duties + requirements) rather than titles
- Enable cross-domain matching (e.g., similar roles with different titles)

### 4. Inference & Matching

**Retrieval Process**:
1. Encode resume using fine-tuned SBERT encoder
2. Compute cosine similarity with all job embeddings
3. Rank and retrieve top-3 matches
4. (Optional) Apply cross-encoder re-ranking for refinement

**Output**: Top-3 jobs with (Job Title, Location, Similarity Score)

### 5. Evaluation (`5_checking_accuracy/`)

Evaluation compares predicted top-3 jobs against ground truth annotations.

## Installation

### Requirements

```bash
pip install -r requirements.txt
```

Key dependencies:
- `sentence-transformers` - Transformer-based embeddings
- `scikit-learn` - Cosine similarity and evaluation
- `pandas` - Data manipulation
- `numpy` - Numerical operations
- `matplotlib`, `seaborn` - Visualization

### Python Version

Python 3.8+

## Usage

### 1. Data Preparation

```bash
# Navigate to data cleaning directory
cd 1_data_cleaning

# Run notebooks in order:
# - 11_cleaning_jd.ipynb (clean job descriptions)
# - 12_clearning_resume.ipynb (clean resumes)
```

### 2. Generate Baseline Embeddings

```bash
cd 2_embeddings

# Run baseline model
jupyter notebook basemodel_embedding.ipynb

# (Optional) Run cross-encoder
jupyter notebook cross_encoder_embedding.ipynb
```

### 3. Fine-Tune Model

```bash
cd 3_fine_tuning

# Create training pairs
jupyter notebook 1b_create_content_based_pairs.ipynb

# Fine-tune SBERT
jupyter notebook 2b_finetune_content_based.ipynb
```

### 4. Evaluate Results

```bash
cd 5_checking_accuracy

# Check accuracy against ground truth
jupyter notebook 5.2_check_accuracy.ipynb
```



## References

- Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks
- [Kaggle - Monster.com Job Descriptions Dataset](https://www.kaggle.com/datasets/PromptCloudHQ/us-jobs-on-monstercom/data)
- [Kaggle - Resume Dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset)

## License

This project is for educational purposes as part of the MIDS NLP course.

## Contact

For questions or collaboration:
- Cindy Gao
- Cynthia Zhou
- Jenny Wu
