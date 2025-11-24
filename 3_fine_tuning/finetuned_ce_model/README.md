---
tags:
- sentence-transformers
- cross-encoder
- reranker
- generated_from_trainer
- dataset_size:1000
- loss:BinaryCrossEntropyLoss
base_model: cross-encoder/ms-marco-MiniLM-L12-v2
pipeline_tag: text-ranking
library_name: sentence-transformers
---

# CrossEncoder based on cross-encoder/ms-marco-MiniLM-L12-v2

This is a [Cross Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html) model finetuned from [cross-encoder/ms-marco-MiniLM-L12-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L12-v2) using the [sentence-transformers](https://www.SBERT.net) library. It computes scores for pairs of texts, which can be used for text reranking and semantic search.

## Model Details

### Model Description
- **Model Type:** Cross Encoder
- **Base model:** [cross-encoder/ms-marco-MiniLM-L12-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L12-v2) <!-- at revision 7b0235231ca2674cb8ca8f022859a6eba2b1c968 -->
- **Maximum Sequence Length:** 512 tokens
- **Number of Output Labels:** 1 label
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Documentation:** [Cross Encoder Documentation](https://www.sbert.net/docs/cross_encoder/usage/usage.html)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Cross Encoders on Hugging Face](https://huggingface.co/models?library=sentence-transformers&other=cross-encoder)

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import CrossEncoder

# Download from the 🤗 Hub
model = CrossEncoder("cross_encoder_model_id")
# Get scores for pairs of texts
pairs = [
    ["Candidate Profile:\n- Career Objective: Machine learning Enthusiast. Motivated to learn, grow and excel my experience by challenging myself.\n- Work Experience: Machinery Maintenance\nTroubleshooting\nReport Preparation\nLog Maintenance\n- Skills: ['Machine Learning', 'Text Analytics', 'Software Development', 'Data Analysis', 'Python', 'Java', 'JavaScript', 'Matplotlib']\n- Degrees: ['B.Tech']\n- Major Field(s) of Study: ['CSE']", 'Job Posting:\n- Job Title: Software Engineer\n- Description: Software DeveloperTulsa, OKDescription:We are looking for a Software Developer with more than 1 year of programming experience.This development position is for an experienced developer (more than 1 yrs on the job experience) and will be working on one of several potential projects depending on skill set. This individual must be highly motivated, creative problem solver, excellent communicator, a quick learner and a self-starter. All these projects are team based and someone that can function in a team environment is a must. Additionally being a quick learner with a solid programming background is required. Because it is team based there will be a good support environment to learn quickly and provide immediate value to the teams. As this is an experienced position, leadership skills and mentoring will be a big part of the role. Responsible for analysis, design, coding, unit tests for new development as well as some maintenance of existing code. The individual fulfilling this role must be able to work in an open agile environment.Job Requirements:A Bachelor’s degree, with a concentration in MIS, CS, or Applicable Experience.1+ years of software development experience.Experience programming in C#, SQL, and .Net (will consider Java or equivalent OO experience)\n- Responsibilities: All these projects are team based and someone that can function in a team environment is a must\nBecause it is team based there will be a good support environment to learn quickly and provide immediate value to the teams\nAs this is an experienced position, leadership skills and mentoring will be a big part of the role\nResponsible for analysis, design, coding, unit tests for new development as well as some maintenance of existing code\nThe individual fulfilling this role must be able to work in an open agile environment\nNet (will consider Java or equivalent OO experience)\n- Requirements: Software DeveloperTulsa, OKDescription:We are looking for a Software Developer with more than 1 year of programming experience\nThis development position is for an experienced developer (more than 1 yrs on the job experience) and will be working on one of several potential projects depending on skill set\nThis individual must be highly motivated, creative problem solver, excellent communicator, a quick learner and a self-starter\nAdditionally being a quick learner with a solid programming background is required\n1+ years of software development experience\nExperience programming in C#, SQL, and\n- Preferred Education: Job Requirements:A Bachelor’s degree, with a concentration in MIS, CS, or Applicable Experience'],
    ["Candidate Profile:\n- Career Objective: Computer Science graduate with 2+ years of experience in systems management, information technology, and data administration. Demonstrated exceptional knowledge in all phases of multiple framework application infrastructures, development, technical process improvement, and system integration.\n- Work Experience: Design Review\nCoordination\nProposal Preparation\nFeasibility Analysis\nSoftware Utilization\nSupervision\nTechnical Support\nSubmission Review\nProgress Reporting\nCompliance\nSite Visits\n- Skills: ['C++', 'Python', '.Ney(VB, ASP)', 'CSS', 'Javascript', 'Visual Basic', 'Visual FoxPro', 'Analytical Process Improvement', 'Risk Assessment & Tracking', 'Data & Network Management', 'Scrum & Agile']\n- Degrees: ['Bachelor of Science']\n- Major Field(s) of Study: ['Computer Science']", 'Job Posting:\n- Job Title: Sr Software Engineer-Amdocs\n- Description: Description:\xa0·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Support our core CRM/Publishing/Billing/Sales backend systems leveraging Amdocs technology and Cobol/Java and SOA/ESB. Prior knowledge/experience with Amdocs technology a mandatory. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Knowledge of SOA and the demonstrated ability to expose and leverage Amdocs systems across other enterprise systems key to your success and growth. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Designs, develops and maintains our core systems and leverages/extends them into our growth areas/systems. Utilizes DexMedia s technology stack and related software development technologies to implement highly scalable and reliable enterprise n-tier distributed applications. Provides technical leadership and/or solutions. Identifies efficiency improvement opportunities. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Performs product design, bug verification and remediation, as well as production support. Modifies, repairs, or enhances existing software to correct errors, increase efficiency, upgrade interfaces, or improve performance. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Works closely with junior developers to maintain high-level of coding standards. Mentors junior developers. Collaborates and performs code reviews with onshore and off-shore team members ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Writes and contributes to technical documentation. Creates test scripts and performs detailed unit testing and analysis on software and systems. Works with operations staff to troubleshoot and maintain production systems. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Participates in software design meetings and analyzes user needs to determine technical requirements. Analyzes project requirements and makes recommendations as appropriate. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Zero prejudices about legacy technologies; drives to solve business needs with tools at hand and finds creative ways to extend/improve new technologies/solutions. \xa0Requirements:\xa0·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Deep expertise with Oracle 7 and SQL development/debugging/performance tuning at the query level. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Experience using Unix/Linux shell scripting ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Deep experience with Java and Cobol. Service Oriented Architecture and working in a Tibco/ESB environment preferred. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Experience and comfort working in Agile/Scrum as well as Waterfall SDLC. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Experience with Continuous Integration and related tools. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Fluency and comfort in Batch as well as Online development/operations. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Amdocs experience mandatory.·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Enjoy working with as a team member fully engage in verbal and written communication methods.·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Bachelor s Degree or equivalent Experience in required.·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Must have at least 5-8 years progressive software development/delivery experience.\xa0Dex Media is an equal opportunity employer. \xa0\n- Responsibilities: Description: · Support our core CRM/Publishing/Billing/Sales backend systems leveraging Amdocs technology and Cobol/Java and SOA/ESB\n· Designs, develops and maintains our core systems and leverages/extends them into our growth areas/systems\nProvides technical leadership and/or solutions\nIdentifies efficiency improvement opportunities\n· Performs product design, bug verification and remediation, as well as production support\nModifies, repairs, or enhances existing software to correct errors, increase efficiency, upgrade interfaces, or improve performance\nCollaborates and performs code reviews with onshore and off-shore team members · Writes and contributes to technical documentation\nCreates test scripts and performs detailed unit testing and analysis on software and systems\nWorks with operations staff to troubleshoot and maintain production systems\n· Experience using Unix/Linux shell scripting · Deep experience with Java and Cobol\nService Oriented Architecture and working in a Tibco/ESB environment preferred\n· Fluency and comfort in Batch as well as Online development/operations\n· Enjoy working with as a team member fully engage in verbal and written communication methods\n- Requirements: Prior knowledge/experience with Amdocs technology a mandatory\n· Participates in software design meetings and analyzes user needs to determine technical requirements\nAnalyzes project requirements and makes recommendations as appropriate\nRequirements: · Deep expertise with Oracle 7 and SQL development/debugging/performance tuning at the query level\n· Experience and comfort working in Agile/Scrum as well as Waterfall SDLC\n· Experience with Continuous Integration and related tools\n· Amdocs experience mandatory\n· Must have at least 5-8 years progressive software development/delivery experience\n- Preferred Education: · Bachelor s Degree or equivalent Experience in required'],
    ["Candidate Profile:\n- Career Objective: As a recent graduate, I am looking for roles that challenge me and feed my craving for learning. I can easily adapt to new technologies, understand and work with a variety of people, and always looking to solving business problems in much more technology sophisticated ways.\n- Work Experience: Project Design\nData Analysis\nACCORD/Alliance Knowledge\nBNBC Standards\nCost Estimation\nFeasibility Studies\nDocumentation\nCompliance\nSite Monitoring\nPolicy Enforcement\nLegal Compliance\nData Management\nTeam Collaboration\n- Skills: ['Machine Learning', 'Deep learning', 'Logistic Regression', 'k-means clustering', 'LSTM', 'Emperical Modelling']\n- Degrees: ['B.Tech(Computers)']\n- Major Field(s) of Study: ['Computers']", "Job Posting:\n- Job Title: Recruiter\n- Description: Our client is currently seeking a Recruiter. JOB SUMMARY A Recruiter is responsible for recruiting and consulting services to support the business needs of a respective client group and/or business line. This position will utilize proactive recruiting techniques and develop industry contacts to hire qualified and talented individuals who mirror\xa0 culture and brand, selecting individuals who will provide added value to the department, business line and company. Recruiters work closely with managers to clarify job specifications and requirements, discuss business operations and develop recruiting strategies to fill current and further staffing needs. Recruiters mentor hiring managers on appropriate company legal hiring/interviewing practices and procedures. Recruiters creatively recruit, develop sources, successfully execute recruitment strategies, market and sell the company's attributes. Recruiters partner with their clients to review, analyze and reduce turnover, meet current and future hiring needs, and assist in the development and rollout of retention programs. ESSENTIAL JOB FUNCTIONS 1.Work closely with managers to clarify job specifications and requirements, discuss business operations and develop recruiting strategies to fill current and further staffing needs. 2.Create a recruiting strategy with the hiring managers on appropriate company legal hiring/interviewing practices and procedures. 3.Recruit, develop sources, and execute recruitment strategies, market and sell the company's attributes. 4.Partner with the business line to review, analyze and reduce turnover, meet current and future hiring needs. 5.Participates in special projects associated with recruitment, performance improvement initiatives, system enhancements, conversions, or implementations, and other applicable Recruitment projects. 6.Assists with compliance requirements for OFCCP and SOX researching regulations when required and identifying needed changes to recruitment processes. EDUCATION / EXPERIENCE REQUIREMENTS •Bachelor’s degree in business or related field with major course work in a discipline related and/or equivalent combination of work experience and education. •Ability to work individually, with recruiting team, business HR and functional HR to design, schedule, implement, and evaluate recruitment initiatives and tools with minimal supervision. Attention to detail and/or math aptitude for reporting development and analytics. Excellent verbal and written communication skills Proficiency in Microsoft Office, Excel, Access, PowerPoint •Minimum 2 years previous related talent acquisition/HR experience with applicant tracking systems and other recruiting tools is preferred.\n- Responsibilities: JOB SUMMARY A Recruiter is responsible for recruiting and consulting services to support the business needs of a respective client group and/or business line\nRecruiters work closely with managers to clarify job specifications and requirements, discuss business operations and develop recruiting strategies to fill current and further staffing needs\nRecruiters mentor hiring managers on appropriate company legal hiring/interviewing practices and procedures\nRecruiters creatively recruit, develop sources, successfully execute recruitment strategies, market and sell the company's attributes\nESSENTIAL JOB FUNCTIONS 1\nWork closely with managers to clarify job specifications and requirements, discuss business operations and develop recruiting strategies to fill current and further staffing needs\nCreate a recruiting strategy with the hiring managers on appropriate company legal hiring/interviewing practices and procedures\nRecruit, develop sources, and execute recruitment strategies, market and sell the company's attributes\nParticipates in special projects associated with recruitment, performance improvement initiatives, system enhancements, conversions, or implementations, and other applicable Recruitment projects\n- Requirements: Assists with compliance requirements for OFCCP and SOX researching regulations when required and identifying needed changes to recruitment processes\nExcellent verbal and written communication skills Proficiency in Microsoft Office, Excel, Access, PowerPoint •Minimum 2 years previous related talent acquisition/HR experience with applicant tracking systems and other recruiting tools is preferred\n- Preferred Education: EDUCATION / EXPERIENCE REQUIREMENTS •Bachelor’s degree in business or related field with major course work in a discipline related and/or equivalent combination of work experience and education"],
    ["Candidate Profile:\n- Career Objective: Desires an accounting position in a positive working environment that encourages and supports continuing professional growth.\n- Work Experience: Internal Audit Assistance\nVoucher & Bill Verification\nCost Sheet Analysis\nL/C Voucher Verification\nExpense Verification\nSalary & Wages Verification\nMarket Rate Verification\n- Skills: ['A/p', 'A/r', 'Automated Payroll', 'Cpa', 'Excel', 'General Ledger', 'Office Management', 'Outlook', 'Payroll', 'Payroll Processing', 'Powerpoint', 'Accounting', 'Bookkeeping', 'Office Manager', 'Accounts For', 'Bookkeeper', 'Cash', 'Financial Statements', 'Process Payroll', 'Reconciliations', 'Tax Returns', 'Balance Sheet', 'Bank Reconciliations', 'Clients', 'G/l', 'Its', 'Job Costing', 'Journal', 'Quickbooks', 'Business Management', 'Clerical', 'Training', 'Account Reconciliations', 'Accountant', 'Accounts And', 'And Account', 'As400', 'Audit', 'Balance Sheets', 'Contracts', 'Inventory', 'Invoice', 'Office Administration', 'Operations', 'Peachtree', 'Peachtree Accounting', 'Progress', 'Reconciling', 'Restaurant Manager', 'Scheduling', 'Secretary', 'State Tax', 'Timberline', 'Timberline Software', 'Typing', 'Word']\n- Degrees: ['A.A.', 'Diploma']\n- Major Field(s) of Study: ['Business Management-Accounting', 'Bookkeeping and Office Administration']", 'Job Posting:\n- Job Title: Financial Analyst: % MBA tuition reimbursement\n- Description: This position offers the opportunity to join a successful and exciting team where you can make a significant impact immediately. This individual will have the opportunity to grow with the company and get promoted quickly. Enjoy a competitive salary, generous benefits, and a 100% tuition reimbursement program. Client DetailsThis company is a clear global leader in materials testing applications and its leadership in the marketplace is continually expanding. With established strength, commitment to core values and team focus, this company provides an engaging work environment and offers exceptional opportunities for personal and career development. This position is based in Norwood, Massachusetts.DescriptionMaintains General Ledger and insures compliance with generally accepted accounting principles (GAAP)Provides accounting support for accounts payable, billing and general ledger reporting.Responsible for the completion of the monthly, quarterly, and annual reporting requirements as well as other ad-hoc requests.Provides business team leaders with financial support.Prepares monthly reports of financial results for local management. These reports generally compare actual performance to plan, forecast and/or prior period.Creates, maintains, and oversees the financial reports in the ERP system used in the review and completion of ITW reporting.ProfileBS/BA in Accounting/Finance combined with some relevant accounting experience.Must possess key leadership qualities, including flexibility, reliability, self-starter and effective team player and communicator.A positive attitude focused on understanding, anticipating and responding to the needs of our customers, both internal and external to the department and company.Interpersonal skills needed to deal effectively with suppliers and company personnel in resolving discrepancies and disputes.Strong analytical skills, detail oriented with an aptitude to work quickly and accurately.Job OfferInterested? Apply now.\n- Responsibilities: This position offers the opportunity to join a successful and exciting team where you can make a significant impact immediately\nThis individual will have the opportunity to grow with the company and get promoted quickly\nClient DetailsThis company is a clear global leader in materials testing applications and its leadership in the marketplace is continually expanding\nWith established strength, commitment to core values and team focus, this company provides an engaging work environment and offers exceptional opportunities for personal and career development\nDescriptionMaintains General Ledger and insures compliance with generally accepted accounting principles (GAAP)Provides accounting support for accounts payable, billing and general ledger reporting\nResponsible for the completion of the monthly, quarterly, and annual reporting requirements as well as other ad-hoc requests\nProvides business team leaders with financial support\nPrepares monthly reports of financial results for local management\nThese reports generally compare actual performance to plan, forecast and/or prior period\nCreates, maintains, and oversees the financial reports in the ERP system used in the review and completion of ITW reporting\nMust possess key leadership qualities, including flexibility, reliability, self-starter and effective team player and communicator\nA positive attitude focused on understanding, anticipating and responding to the needs of our customers, both internal and external to the department and company\nJob OfferInterested\n- Requirements: Interpersonal skills needed to deal effectively with suppliers and company personnel in resolving discrepancies and disputes\nStrong analytical skills, detail oriented with an aptitude to work quickly and accurately\n- Preferred Education: ProfileBS/BA in Accounting/Finance combined with some relevant accounting experience'],
    ["Candidate Profile:\n- Career Objective: A python programmer, currently pursuing Data science and looking for roles that involve the application of Machine Learning. I am always excited to take on real life problems and tread through different technology stacks.\n- Work Experience: Management Trainee\nMechanical Systems\nMaintenance & Troubleshooting\nPerformance Analysis\nProject Support\nProcess Improvement\nTraining & Development\nAdministrative Support\n- Skills: ['Python Developer', 'Django', 'Flask', 'Data Science', 'Spark', 'PySpark', 'Machine Learning', 'Data Modelling', 'Natural language Processing', 'SVM', 'Computer Vision', 'Neural Networks.']\n- Degrees: ['B.Tech']\n- Major Field(s) of Study: ['N/A']", 'Job Posting:\n- Job Title: Software Engineer\n- Description: We are seeking qualified and motivated candidates to join our software engineering team.\xa0 Responsible for the systematic approach to the development of requirements, design, implementation, test and maintenance of software components.\xa0 Researches, designs, develops and tests computer software systems, in conjunction with hardware product development. Analyzes system requirements to determine adequacy, consistency and realism; and to estimate the feasibility of design within cost and schedules constraints. Formulates and designs software systems, including critical real-time and/or embedded systems, using empirical methods, scientific analysis and/or mathematical models to predict and measure outcome and consequence of design. Consults with Hardware Engineers and other Engineering staff to evaluate the interface between hardware and software, and the operational and performance requirements of overall systems.\xa0Bachelor’s degree plus 7+ years related experience.\xa0 Must have the ability to use data and logic analyzers.\xa0 The ability to read, analyze, and interpret technical periodicals, professional journals, technical procedures, or governmental specifications is required.\xa0 Must have experience with software architecture design and test.\xa0 Must be able to generate code to requirements.\xa0 Experience in C, C++, DOORS and UML.\xa0 Must have knowledge of VxWorks, real time operating systems, CMM, and team oriented design.\xa0 Desired experience includes Kalman Tracker, Object oriented design, GUI development, Radar (i.e. Airborne and Weather), and Radar Test equipment.\xa0 Must have a background that would permit the issuance of a Security clearance, which includes US citizenship.\n- Responsibilities: Responsible for the systematic approach to the development of requirements, design, implementation, test and maintenance of software components\nConsults with Hardware Engineers and other Engineering staff to evaluate the interface between hardware and software, and the operational and performance requirements of overall systems\n- Requirements: Analyzes system requirements to determine adequacy, consistency and realism\nThe ability to read, analyze, and interpret technical periodicals, professional journals, technical procedures, or governmental specifications is required\nMust have experience with software architecture design and test\nMust be able to generate code to requirements\nExperience in C, C++, DOORS and UML\nDesired experience includes Kalman Tracker, Object oriented design, GUI development, Radar (i\n- Preferred Education: Bachelor’s degree plus 7+ years related experience'],
]
scores = model.predict(pairs)
print(scores.shape)
# (5,)

# Or rank different texts based on similarity to a single text
ranks = model.rank(
    "Candidate Profile:\n- Career Objective: Machine learning Enthusiast. Motivated to learn, grow and excel my experience by challenging myself.\n- Work Experience: Machinery Maintenance\nTroubleshooting\nReport Preparation\nLog Maintenance\n- Skills: ['Machine Learning', 'Text Analytics', 'Software Development', 'Data Analysis', 'Python', 'Java', 'JavaScript', 'Matplotlib']\n- Degrees: ['B.Tech']\n- Major Field(s) of Study: ['CSE']",
    [
        'Job Posting:\n- Job Title: Software Engineer\n- Description: Software DeveloperTulsa, OKDescription:We are looking for a Software Developer with more than 1 year of programming experience.This development position is for an experienced developer (more than 1 yrs on the job experience) and will be working on one of several potential projects depending on skill set. This individual must be highly motivated, creative problem solver, excellent communicator, a quick learner and a self-starter. All these projects are team based and someone that can function in a team environment is a must. Additionally being a quick learner with a solid programming background is required. Because it is team based there will be a good support environment to learn quickly and provide immediate value to the teams. As this is an experienced position, leadership skills and mentoring will be a big part of the role. Responsible for analysis, design, coding, unit tests for new development as well as some maintenance of existing code. The individual fulfilling this role must be able to work in an open agile environment.Job Requirements:A Bachelor’s degree, with a concentration in MIS, CS, or Applicable Experience.1+ years of software development experience.Experience programming in C#, SQL, and .Net (will consider Java or equivalent OO experience)\n- Responsibilities: All these projects are team based and someone that can function in a team environment is a must\nBecause it is team based there will be a good support environment to learn quickly and provide immediate value to the teams\nAs this is an experienced position, leadership skills and mentoring will be a big part of the role\nResponsible for analysis, design, coding, unit tests for new development as well as some maintenance of existing code\nThe individual fulfilling this role must be able to work in an open agile environment\nNet (will consider Java or equivalent OO experience)\n- Requirements: Software DeveloperTulsa, OKDescription:We are looking for a Software Developer with more than 1 year of programming experience\nThis development position is for an experienced developer (more than 1 yrs on the job experience) and will be working on one of several potential projects depending on skill set\nThis individual must be highly motivated, creative problem solver, excellent communicator, a quick learner and a self-starter\nAdditionally being a quick learner with a solid programming background is required\n1+ years of software development experience\nExperience programming in C#, SQL, and\n- Preferred Education: Job Requirements:A Bachelor’s degree, with a concentration in MIS, CS, or Applicable Experience',
        'Job Posting:\n- Job Title: Sr Software Engineer-Amdocs\n- Description: Description:\xa0·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Support our core CRM/Publishing/Billing/Sales backend systems leveraging Amdocs technology and Cobol/Java and SOA/ESB. Prior knowledge/experience with Amdocs technology a mandatory. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Knowledge of SOA and the demonstrated ability to expose and leverage Amdocs systems across other enterprise systems key to your success and growth. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Designs, develops and maintains our core systems and leverages/extends them into our growth areas/systems. Utilizes DexMedia s technology stack and related software development technologies to implement highly scalable and reliable enterprise n-tier distributed applications. Provides technical leadership and/or solutions. Identifies efficiency improvement opportunities. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Performs product design, bug verification and remediation, as well as production support. Modifies, repairs, or enhances existing software to correct errors, increase efficiency, upgrade interfaces, or improve performance. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Works closely with junior developers to maintain high-level of coding standards. Mentors junior developers. Collaborates and performs code reviews with onshore and off-shore team members ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Writes and contributes to technical documentation. Creates test scripts and performs detailed unit testing and analysis on software and systems. Works with operations staff to troubleshoot and maintain production systems. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Participates in software design meetings and analyzes user needs to determine technical requirements. Analyzes project requirements and makes recommendations as appropriate. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Zero prejudices about legacy technologies; drives to solve business needs with tools at hand and finds creative ways to extend/improve new technologies/solutions. \xa0Requirements:\xa0·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Deep expertise with Oracle 7 and SQL development/debugging/performance tuning at the query level. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Experience using Unix/Linux shell scripting ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Deep experience with Java and Cobol. Service Oriented Architecture and working in a Tibco/ESB environment preferred. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Experience and comfort working in Agile/Scrum as well as Waterfall SDLC. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Experience with Continuous Integration and related tools. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Fluency and comfort in Batch as well as Online development/operations. ·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Amdocs experience mandatory.·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Enjoy working with as a team member fully engage in verbal and written communication methods.·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Bachelor s Degree or equivalent Experience in required.·\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0 Must have at least 5-8 years progressive software development/delivery experience.\xa0Dex Media is an equal opportunity employer. \xa0\n- Responsibilities: Description: · Support our core CRM/Publishing/Billing/Sales backend systems leveraging Amdocs technology and Cobol/Java and SOA/ESB\n· Designs, develops and maintains our core systems and leverages/extends them into our growth areas/systems\nProvides technical leadership and/or solutions\nIdentifies efficiency improvement opportunities\n· Performs product design, bug verification and remediation, as well as production support\nModifies, repairs, or enhances existing software to correct errors, increase efficiency, upgrade interfaces, or improve performance\nCollaborates and performs code reviews with onshore and off-shore team members · Writes and contributes to technical documentation\nCreates test scripts and performs detailed unit testing and analysis on software and systems\nWorks with operations staff to troubleshoot and maintain production systems\n· Experience using Unix/Linux shell scripting · Deep experience with Java and Cobol\nService Oriented Architecture and working in a Tibco/ESB environment preferred\n· Fluency and comfort in Batch as well as Online development/operations\n· Enjoy working with as a team member fully engage in verbal and written communication methods\n- Requirements: Prior knowledge/experience with Amdocs technology a mandatory\n· Participates in software design meetings and analyzes user needs to determine technical requirements\nAnalyzes project requirements and makes recommendations as appropriate\nRequirements: · Deep expertise with Oracle 7 and SQL development/debugging/performance tuning at the query level\n· Experience and comfort working in Agile/Scrum as well as Waterfall SDLC\n· Experience with Continuous Integration and related tools\n· Amdocs experience mandatory\n· Must have at least 5-8 years progressive software development/delivery experience\n- Preferred Education: · Bachelor s Degree or equivalent Experience in required',
        "Job Posting:\n- Job Title: Recruiter\n- Description: Our client is currently seeking a Recruiter. JOB SUMMARY A Recruiter is responsible for recruiting and consulting services to support the business needs of a respective client group and/or business line. This position will utilize proactive recruiting techniques and develop industry contacts to hire qualified and talented individuals who mirror\xa0 culture and brand, selecting individuals who will provide added value to the department, business line and company. Recruiters work closely with managers to clarify job specifications and requirements, discuss business operations and develop recruiting strategies to fill current and further staffing needs. Recruiters mentor hiring managers on appropriate company legal hiring/interviewing practices and procedures. Recruiters creatively recruit, develop sources, successfully execute recruitment strategies, market and sell the company's attributes. Recruiters partner with their clients to review, analyze and reduce turnover, meet current and future hiring needs, and assist in the development and rollout of retention programs. ESSENTIAL JOB FUNCTIONS 1.Work closely with managers to clarify job specifications and requirements, discuss business operations and develop recruiting strategies to fill current and further staffing needs. 2.Create a recruiting strategy with the hiring managers on appropriate company legal hiring/interviewing practices and procedures. 3.Recruit, develop sources, and execute recruitment strategies, market and sell the company's attributes. 4.Partner with the business line to review, analyze and reduce turnover, meet current and future hiring needs. 5.Participates in special projects associated with recruitment, performance improvement initiatives, system enhancements, conversions, or implementations, and other applicable Recruitment projects. 6.Assists with compliance requirements for OFCCP and SOX researching regulations when required and identifying needed changes to recruitment processes. EDUCATION / EXPERIENCE REQUIREMENTS •Bachelor’s degree in business or related field with major course work in a discipline related and/or equivalent combination of work experience and education. •Ability to work individually, with recruiting team, business HR and functional HR to design, schedule, implement, and evaluate recruitment initiatives and tools with minimal supervision. Attention to detail and/or math aptitude for reporting development and analytics. Excellent verbal and written communication skills Proficiency in Microsoft Office, Excel, Access, PowerPoint •Minimum 2 years previous related talent acquisition/HR experience with applicant tracking systems and other recruiting tools is preferred.\n- Responsibilities: JOB SUMMARY A Recruiter is responsible for recruiting and consulting services to support the business needs of a respective client group and/or business line\nRecruiters work closely with managers to clarify job specifications and requirements, discuss business operations and develop recruiting strategies to fill current and further staffing needs\nRecruiters mentor hiring managers on appropriate company legal hiring/interviewing practices and procedures\nRecruiters creatively recruit, develop sources, successfully execute recruitment strategies, market and sell the company's attributes\nESSENTIAL JOB FUNCTIONS 1\nWork closely with managers to clarify job specifications and requirements, discuss business operations and develop recruiting strategies to fill current and further staffing needs\nCreate a recruiting strategy with the hiring managers on appropriate company legal hiring/interviewing practices and procedures\nRecruit, develop sources, and execute recruitment strategies, market and sell the company's attributes\nParticipates in special projects associated with recruitment, performance improvement initiatives, system enhancements, conversions, or implementations, and other applicable Recruitment projects\n- Requirements: Assists with compliance requirements for OFCCP and SOX researching regulations when required and identifying needed changes to recruitment processes\nExcellent verbal and written communication skills Proficiency in Microsoft Office, Excel, Access, PowerPoint •Minimum 2 years previous related talent acquisition/HR experience with applicant tracking systems and other recruiting tools is preferred\n- Preferred Education: EDUCATION / EXPERIENCE REQUIREMENTS •Bachelor’s degree in business or related field with major course work in a discipline related and/or equivalent combination of work experience and education",
        'Job Posting:\n- Job Title: Financial Analyst: % MBA tuition reimbursement\n- Description: This position offers the opportunity to join a successful and exciting team where you can make a significant impact immediately. This individual will have the opportunity to grow with the company and get promoted quickly. Enjoy a competitive salary, generous benefits, and a 100% tuition reimbursement program. Client DetailsThis company is a clear global leader in materials testing applications and its leadership in the marketplace is continually expanding. With established strength, commitment to core values and team focus, this company provides an engaging work environment and offers exceptional opportunities for personal and career development. This position is based in Norwood, Massachusetts.DescriptionMaintains General Ledger and insures compliance with generally accepted accounting principles (GAAP)Provides accounting support for accounts payable, billing and general ledger reporting.Responsible for the completion of the monthly, quarterly, and annual reporting requirements as well as other ad-hoc requests.Provides business team leaders with financial support.Prepares monthly reports of financial results for local management. These reports generally compare actual performance to plan, forecast and/or prior period.Creates, maintains, and oversees the financial reports in the ERP system used in the review and completion of ITW reporting.ProfileBS/BA in Accounting/Finance combined with some relevant accounting experience.Must possess key leadership qualities, including flexibility, reliability, self-starter and effective team player and communicator.A positive attitude focused on understanding, anticipating and responding to the needs of our customers, both internal and external to the department and company.Interpersonal skills needed to deal effectively with suppliers and company personnel in resolving discrepancies and disputes.Strong analytical skills, detail oriented with an aptitude to work quickly and accurately.Job OfferInterested? Apply now.\n- Responsibilities: This position offers the opportunity to join a successful and exciting team where you can make a significant impact immediately\nThis individual will have the opportunity to grow with the company and get promoted quickly\nClient DetailsThis company is a clear global leader in materials testing applications and its leadership in the marketplace is continually expanding\nWith established strength, commitment to core values and team focus, this company provides an engaging work environment and offers exceptional opportunities for personal and career development\nDescriptionMaintains General Ledger and insures compliance with generally accepted accounting principles (GAAP)Provides accounting support for accounts payable, billing and general ledger reporting\nResponsible for the completion of the monthly, quarterly, and annual reporting requirements as well as other ad-hoc requests\nProvides business team leaders with financial support\nPrepares monthly reports of financial results for local management\nThese reports generally compare actual performance to plan, forecast and/or prior period\nCreates, maintains, and oversees the financial reports in the ERP system used in the review and completion of ITW reporting\nMust possess key leadership qualities, including flexibility, reliability, self-starter and effective team player and communicator\nA positive attitude focused on understanding, anticipating and responding to the needs of our customers, both internal and external to the department and company\nJob OfferInterested\n- Requirements: Interpersonal skills needed to deal effectively with suppliers and company personnel in resolving discrepancies and disputes\nStrong analytical skills, detail oriented with an aptitude to work quickly and accurately\n- Preferred Education: ProfileBS/BA in Accounting/Finance combined with some relevant accounting experience',
        'Job Posting:\n- Job Title: Software Engineer\n- Description: We are seeking qualified and motivated candidates to join our software engineering team.\xa0 Responsible for the systematic approach to the development of requirements, design, implementation, test and maintenance of software components.\xa0 Researches, designs, develops and tests computer software systems, in conjunction with hardware product development. Analyzes system requirements to determine adequacy, consistency and realism; and to estimate the feasibility of design within cost and schedules constraints. Formulates and designs software systems, including critical real-time and/or embedded systems, using empirical methods, scientific analysis and/or mathematical models to predict and measure outcome and consequence of design. Consults with Hardware Engineers and other Engineering staff to evaluate the interface between hardware and software, and the operational and performance requirements of overall systems.\xa0Bachelor’s degree plus 7+ years related experience.\xa0 Must have the ability to use data and logic analyzers.\xa0 The ability to read, analyze, and interpret technical periodicals, professional journals, technical procedures, or governmental specifications is required.\xa0 Must have experience with software architecture design and test.\xa0 Must be able to generate code to requirements.\xa0 Experience in C, C++, DOORS and UML.\xa0 Must have knowledge of VxWorks, real time operating systems, CMM, and team oriented design.\xa0 Desired experience includes Kalman Tracker, Object oriented design, GUI development, Radar (i.e. Airborne and Weather), and Radar Test equipment.\xa0 Must have a background that would permit the issuance of a Security clearance, which includes US citizenship.\n- Responsibilities: Responsible for the systematic approach to the development of requirements, design, implementation, test and maintenance of software components\nConsults with Hardware Engineers and other Engineering staff to evaluate the interface between hardware and software, and the operational and performance requirements of overall systems\n- Requirements: Analyzes system requirements to determine adequacy, consistency and realism\nThe ability to read, analyze, and interpret technical periodicals, professional journals, technical procedures, or governmental specifications is required\nMust have experience with software architecture design and test\nMust be able to generate code to requirements\nExperience in C, C++, DOORS and UML\nDesired experience includes Kalman Tracker, Object oriented design, GUI development, Radar (i\n- Preferred Education: Bachelor’s degree plus 7+ years related experience',
    ]
)
# [{'corpus_id': ..., 'score': ...}, {'corpus_id': ..., 'score': ...}, ...]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 1,000 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                                         | sentence_1                                                                                           | label                                                         |
  |:--------|:---------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | type    | string                                                                                             | string                                                                                               | float                                                         |
  | details | <ul><li>min: 424 characters</li><li>mean: 900.77 characters</li><li>max: 2880 characters</li></ul> | <ul><li>min: 962 characters</li><li>mean: 3434.54 characters</li><li>max: 11309 characters</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.1</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | label            |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>Candidate Profile:<br>- Career Objective: Machine learning Enthusiast. Motivated to learn, grow and excel my experience by challenging myself.<br>- Work Experience: Machinery Maintenance<br>Troubleshooting<br>Report Preparation<br>Log Maintenance<br>- Skills: ['Machine Learning', 'Text Analytics', 'Software Development', 'Data Analysis', 'Python', 'Java', 'JavaScript', 'Matplotlib']<br>- Degrees: ['B.Tech']<br>- Major Field(s) of Study: ['CSE']</code>                                                                                                                                                                                                                                                                                                                                                                                                                                     | <code>Job Posting:<br>- Job Title: Software Engineer<br>- Description: Software DeveloperTulsa, OKDescription:We are looking for a Software Developer with more than 1 year of programming experience.This development position is for an experienced developer (more than 1 yrs on the job experience) and will be working on one of several potential projects depending on skill set. This individual must be highly motivated, creative problem solver, excellent communicator, a quick learner and a self-starter. All these projects are team based and someone that can function in a team environment is a must. Additionally being a quick learner with a solid programming background is required. Because it is team based there will be a good support environment to learn quickly and provide immediate value to the teams. As this is an experienced position, leadership skills and mentoring will be a big part of the role. Responsible for analysis, design, coding, unit tests for new development as well as some maintenance o...</code> | <code>0.0</code> |
  | <code>Candidate Profile:<br>- Career Objective: Computer Science graduate with 2+ years of experience in systems management, information technology, and data administration. Demonstrated exceptional knowledge in all phases of multiple framework application infrastructures, development, technical process improvement, and system integration.<br>- Work Experience: Design Review<br>Coordination<br>Proposal Preparation<br>Feasibility Analysis<br>Software Utilization<br>Supervision<br>Technical Support<br>Submission Review<br>Progress Reporting<br>Compliance<br>Site Visits<br>- Skills: ['C++', 'Python', '.Ney(VB, ASP)', 'CSS', 'Javascript', 'Visual Basic', 'Visual FoxPro', 'Analytical Process Improvement', 'Risk Assessment & Tracking', 'Data & Network Management', 'Scrum & Agile']<br>- Degrees: ['Bachelor of Science']<br>- Major Field(s) of Study: ['Computer Science']</code> | <code>Job Posting:<br>- Job Title: Sr Software Engineer-Amdocs<br>- Description: Description: ·         Support our core CRM/Publishing/Billing/Sales backend systems leveraging Amdocs technology and Cobol/Java and SOA/ESB. Prior knowledge/experience with Amdocs technology a mandatory. ·         Knowledge of SOA and the demonstrated ability to expose and leverage Amdocs systems across other enterprise systems key to your success and growth. ·         Designs, develops and maintains our core systems and leverages/extends them into our growth areas/systems. Utilizes DexMedia s technology stack and related software development technologies to implement highly scalable and reliable enterprise n-tier distributed applications. Provides technical leadership and/or solutions. Identifies efficiency improvement opportunities. ·         Performs product design, bug verification and remediation, as well as production support. Modifies, repairs, or enhances existing software to correct errors, increase efficien...</code> | <code>0.0</code> |
  | <code>Candidate Profile:<br>- Career Objective: As a recent graduate, I am looking for roles that challenge me and feed my craving for learning. I can easily adapt to new technologies, understand and work with a variety of people, and always looking to solving business problems in much more technology sophisticated ways.<br>- Work Experience: Project Design<br>Data Analysis<br>ACCORD/Alliance Knowledge<br>BNBC Standards<br>Cost Estimation<br>Feasibility Studies<br>Documentation<br>Compliance<br>Site Monitoring<br>Policy Enforcement<br>Legal Compliance<br>Data Management<br>Team Collaboration<br>- Skills: ['Machine Learning', 'Deep learning', 'Logistic Regression', 'k-means clustering', 'LSTM', 'Emperical Modelling']<br>- Degrees: ['B.Tech(Computers)']<br>- Major Field(s) of Study: ['Computers']</code>                                                                      | <code>Job Posting:<br>- Job Title: Recruiter<br>- Description: Our client is currently seeking a Recruiter. JOB SUMMARY A Recruiter is responsible for recruiting and consulting services to support the business needs of a respective client group and/or business line. This position will utilize proactive recruiting techniques and develop industry contacts to hire qualified and talented individuals who mirror  culture and brand, selecting individuals who will provide added value to the department, business line and company. Recruiters work closely with managers to clarify job specifications and requirements, discuss business operations and develop recruiting strategies to fill current and further staffing needs. Recruiters mentor hiring managers on appropriate company legal hiring/interviewing practices and procedures. Recruiters creatively recruit, develop sources, successfully execute recruitment strategies, market and sell the company's attributes. Recruiters partner with their clients to review, ...</code> | <code>0.0</code> |
* Loss: [<code>BinaryCrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#binarycrossentropyloss) with these parameters:
  ```json
  {
      "activation_fn": "torch.nn.modules.linear.Identity",
      "pos_weight": null
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `num_train_epochs`: 5

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 8
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 5
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch | Step | Training Loss |
|:-----:|:----:|:-------------:|
| 4.0   | 500  | 0.3382        |


### Framework Versions
- Python: 3.10.19
- Sentence Transformers: 5.1.2
- Transformers: 4.57.1
- PyTorch: 2.9.1
- Accelerate: 1.12.0
- Datasets: 4.4.1
- Tokenizers: 0.22.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->