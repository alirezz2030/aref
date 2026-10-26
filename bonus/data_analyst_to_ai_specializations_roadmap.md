# Roadmap After Data Analysis: Data Science, ML, DL, NLP, CV, Big Data, and LLMs

This guide compares seven potential specializations after Data Analysis, including what to learn, approximate study timelines, portfolio projects, target roles, salary reference points, and a practical 12-month plan.

> **Important:** Timelines are planning estimates, not guarantees of employment. Salaries vary by location, seniority, industry, employer, and compensation structure. Salary figures below are the reference points cited in the original guide and should be rechecked before making career decisions.

## 1. The Overall Roadmap

```text
Data Analyst Foundation
SQL · Python · pandas · Statistics · Excel · Power BI · Business Analysis
                         |
                         v
                    Data Science
Statistics · Experimentation · Feature Engineering · Predictive Modeling
                         |
                         v
                  Machine Learning
Model Evaluation · Pipelines · Model Selection · Deployment
                         |
                         v
                   Deep Learning
PyTorch · Neural Networks · CNNs · Transformers · GPU Training
                   /             \
                  v               v
                NLP          Computer Vision
                  |
                  v
           LLM Engineering

Parallel path from Data Analysis:
Big Data Engineering
Advanced SQL · Spark/PySpark · Data Pipelines · Warehouses · Cloud
```

This is a learning map, not a mandatory sequence:

- **Deep Learning** is a subset of Machine Learning.
- **NLP** is the broader field of processing and understanding human language.
- **LLM Engineering** focuses on building reliable systems and applications around large language models.
- **Computer Vision** focuses on images and video.
- **Big Data Engineering** focuses on data infrastructure and processing at scale; it does not require completing Deep Learning first.

## 2. Roadmap for Each Specialization

The study estimates below assume approximately **10–15 hours per week**, after building a reasonable Data Analysis foundation.

### 2.1 Data Science

**Estimated learning period:** 2–3 months for core skills.

**What to learn**
- Probability and inferential statistics
- Experiment design and A/B testing
- Feature engineering
- Regression and classification
- Clustering and segmentation
- Forecasting
- Model evaluation and interpretation

**Recommended tools**
- NumPy, pandas, SciPy
- scikit-learn
- Matplotlib and Seaborn

**Portfolio project**

Predict customer churn or forecast monthly sales. Compare a simple baseline with a more sophisticated model and explain whether the improvement is useful to the business.

**Potential roles**
- Junior Data Scientist
- Product Analyst
- Decision Scientist

### 2.2 Machine Learning (ML)

**Estimated learning period:** 2–3 months for core applied skills.

**What to learn**
- Linear and logistic regression
- Decision trees and Random Forest
- Gradient boosting
- Support Vector Machines
- Clustering
- Cross-validation and hyperparameter tuning
- Data leakage and imbalanced datasets
- Feature pipelines and model interpretation

**Recommended tools**
- scikit-learn
- XGBoost or LightGBM
- MLflow
- FastAPI for serving models

**Portfolio project**

Train a churn or fraud-risk model, evaluate it on held-out data, expose predictions through an API, and document limitations.

**Potential roles**
- Junior ML Engineer
- Applied ML Engineer
- Data Scientist

**Advice:** Learn conventional ML fundamentals before specializing in Deep Learning. Many business prediction tasks can be solved very well using traditional ML.

### 2.3 Deep Learning (DL)

**Estimated learning period:** 2–3 months for fundamentals, after ML foundations.

**What to learn**
- Tensors and tensor operations
- Gradients and backpropagation
- Neural networks and optimizers
- Regularization
- Embeddings
- Convolutional Neural Networks (CNNs)
- Transformer architecture
- Training and evaluating pretrained models

**Recommended tools**
- PyTorch
- Jupyter
- Hugging Face
- Experiment tracking tools

**Portfolio project**

Fine-tune a small pretrained model and explain the training setup, evaluation metrics, resource use, and failure cases.

**Potential roles**
- Deep Learning Engineer
- ML Engineer
- Research Engineer

**Advice:** Course completion alone is not enough. Employers need evidence that you can train, evaluate, or deploy models. Training large models from scratch also requires substantially more compute and expertise.

### 2.4 Natural Language Processing (NLP)

**Estimated learning period:** 2–3 months for applied skills.

**What to learn**
- Text preprocessing and tokenization
- Bag-of-words and TF-IDF
- Text classification
- Word and sentence embeddings
- Transformers
- Semantic search
- Retrieval and evaluation

**Recommended tools**
- Hugging Face Transformers and Datasets
- spaCy
- PyTorch
- sentence-transformers

**Portfolio project**

Build a searchable document system or a support-ticket classifier. Compare a simple text model with a transformer-based approach.

**Potential roles**
- NLP Engineer
- Applied Scientist
- Language AI Engineer

NLP is a useful foundation for LLM work, and modern NLP jobs often overlap with LLM Engineering.

### 2.5 LLM Engineering

**Estimated learning period:** 3–4 months to build an applied portfolio.

**What to learn**
- Transformer fundamentals
- Prompt design
- Embeddings
- Vector databases
- Retrieval-Augmented Generation (RAG)
- Reranking
- LLM evaluation
- Tool calling and structured outputs
- Fine-tuning with LoRA/QLoRA
- Deployment, latency, and cost optimization

**Recommended tools**
- Hugging Face
- PyTorch
- A vector database
- FastAPI
- Docker
- An LLM evaluation framework

**Portfolio project**

Build a RAG assistant over technical documents. It should:
1. Retrieve relevant passages.
2. Cite supporting sources.
3. Handle questions when evidence is missing.
4. Be evaluated against a test set.
5. Track answer quality, latency, and cost.

**Potential roles**
- LLM Engineer
- AI Engineer
- Generative AI Developer

**Important distinction:** Building applications with existing LLMs differs from pretraining a foundation model from scratch. Pretraining generally requires substantially more computing resources, research expertise, and data.

### 2.6 Computer Vision (CV)

**Estimated learning period:** 3–4 months for an applied portfolio.

**What to learn**
- Image processing
- Image augmentation
- CNNs and transfer learning
- Image classification
- Object detection
- Image segmentation
- Model evaluation and inference optimization

**Recommended tools**
- OpenCV
- PyTorch
- torchvision
- A modern object-detection framework

**Portfolio project**

Train or fine-tune an object detector for a clear task. Report precision, recall, inference speed, and failure cases on images that were not used for training.

**Potential roles**
- Computer Vision Engineer
- Vision ML Engineer
- Applied Scientist

Choose CV because you enjoy working with images and video—not just because it sounds prestigious. Dataset availability and deployment constraints matter.

### 2.7 Big Data Engineering

**Estimated learning period:** 3–4 months for foundations.

**What to learn**
- Advanced SQL
- Data modeling
- ETL/ELT
- Partitioning and Parquet
- Spark and PySpark
- Data warehouses
- Workflow orchestration
- Data quality
- Cloud fundamentals

**Recommended tools**
- PySpark
- Apache Airflow
- dbt
- Docker
- One cloud ecosystem

**Portfolio project**

Build a pipeline that ingests raw sales data, validates it, processes it with Spark, stores clean data in Parquet, and produces reporting-ready tables.

**Potential roles**
- Data Engineer
- Big Data Engineer
- Analytics Engineer
- Data Platform Engineer

This can be a more direct move from Data Analysis than Deep Learning if you enjoy SQL, systems, and pipelines.

## 3. Salary Comparison

Salaries depend on geography, seniority, industry, employer, and whether compensation includes bonuses or equity. The figures here are reference points, not guaranteed offers or forecasts for any specific candidate.

### 3.1 United States: Salary-Guide Reference Points

The following approximate US annual base-salary figures were cited from a specialized 2026 AI/ML salary guide. They should be treated as indicative guide figures rather than perfectly comparable official statistics.

| Field / related job family | Junior reference | Senior median reference |
|---|---:|---:|
| Data Science | $108,000 | $195,000 |
| Machine Learning Engineer | $130,000 | $230,000 |
| Deep Learning Engineer* | Use ML Engineer as a proxy | Use ML Engineer as a proxy |
| NLP Engineer | $120,000 | $215,000 |
| Computer Vision Engineer | $125,000 | $220,000 |
| Big Data / Data Engineer | $105,000 | $185,000 |
| LLM Engineer | $125,000 | $220,000 |

\*Deep Learning Engineer is not a consistently standardized job title; many roles are advertised as ML Engineer or Research Engineer. Data Engineer is used as the nearest common proxy for Big Data Engineering.

**Salary guide source:** [AI/LLM Jobs — Salaries](https://aillmjobs.com/salaries)

For a separate broad-market reference, the US Bureau of Labor Statistics reported a **$120,230 median annual wage for Data Scientists in May 2025**, with the lowest 10% earning below $67,240 and the highest 10% above $199,130. It projected 35% employment growth for US Data Scientists from 2025 to 2035. These are national occupational statistics, not salary estimates for every AI specialization.

**Source:** [US Bureau of Labor Statistics — Data Scientists](https://www.bls.gov/ooh/math/data-scientists.htm)

Another 2026 US hiring guide placed the middle of its salary ranges at approximately $165,000 for Data Scientists, $174,000 for ML Engineers, and $167,000 for Data Engineers, illustrating that salary estimates can differ by source and population.

**Source:** [Pearson Carter — Data & AI Hiring Guides](https://www.pearsoncarter.com/hiring-guides/data-ai-2026)

### 3.2 Iran: Public Reference Points

The cited IranTalent 1405 salary data for Data Science and AI roles in Tehran reported the following expected monthly net salary levels. These are local-market reference points, not guaranteed salaries.

| Role / source | Reported monthly amount |
|---|---:|
| Data Science and AI expert in Tehran — median expected salary | 50 million toman |
| Middle 50% of that Tehran Data Science/AI group | 37–71 million toman |
| ML Engineer, listed in Isfahan | 35–50 million toman |
| Senior ML Engineer (NLP), listed in Tehran | 40–60 million toman |
| Computer Vision Developer, listed in Tehran | 30–45 million toman |
| NLP specialist, part-time remote listing | 25–40 million toman |

**Source:** [IranTalent — Data Science and AI Expert Salary](https://salary.irantalent.com/salary-report/data-science-ai-expert-salary/)

The specialist amounts are examples of listed positions, not a comprehensive salary survey. The Data Science/AI figures are described as expected/requested net salaries, which may differ from final agreed compensation.

Reliable public median figures specifically separated into NLP, CV, LLM, and Deep Learning jobs in Iran are limited. It is better to compare recent advertisements with the actual responsibilities, seniority, and required experience than to invent a precise median.

**Remote-work note:** US salary figures do not automatically apply to remote jobs performed from Iran. Employers may restrict hiring locations or payment arrangements, and remote compensation may be adjusted by location.

## 4. Practical 12-Month Plan

This plan assumes the Data Analysis foundation is already in place. Timelines can be adjusted to your available study hours and current skill level.

### Months 1–2: Data Science Foundations
- Strengthen statistics and experimentation.
- Learn feature engineering and scikit-learn.
- Complete one predictive project.
- Compare the model against a simple baseline.

**Deliverable:** A reproducible notebook with metrics, interpretation, and limitations.

### Months 3–4: Machine Learning
- Learn pipelines and cross-validation.
- Practice model selection and handling imbalanced data.
- Study model interpretation and error analysis.
- Build a second project comparing algorithms fairly.

**Deliverable:** A trained model, reliable evaluation, documented experiments, and a model card.

### Months 5–6: Deep Learning
- Study PyTorch, tensors, gradients, and neural networks.
- Learn transfer learning and transformer fundamentals.
- Start with small pretrained models instead of large models from scratch.

**Deliverable:** One fine-tuned model with honest evaluation and documented compute requirements.

### Months 7–9: Choose One Specialization
Choose **one** primary path:
- **LLM Engineering:** RAG, embeddings, retrieval, evaluation, and application deployment.
- **Computer Vision:** image data, object detection, segmentation, and transfer learning.
- **Big Data Engineering:** Spark, data pipelines, warehouses, and orchestration.

**Deliverable:** One end-to-end project in the chosen specialty.

### Months 10–12: Deployment and Job Applications
- Package a project with a clean API or pipeline.
- Add testing, Docker, documentation, and a clear README.
- Practice relevant interview questions.
- Apply to jobs that match the selected path.

**Deliverable:** Two strong specialty projects, a portfolio page, and targeted job applications.

You can explore all seven subjects in a year, but becoming deeply proficient in all of them normally takes longer. Focused specialization is generally more useful than shallow familiarity with every tool.

## 5. Choose the Career Path That Fits Your Goal

### Path A: Applied AI / LLM Engineer
**Sequence:** Data Analysis → Data Science & ML → LLM applications → evaluation and deployment

**Planning estimate:** About 9–12 months for a focused, part-time learning plan.

**Focus on:** Python/backend development, APIs, RAG, evaluation, Docker, and production reliability.

**Portfolio project:** A RAG system with source citations, a repeatable evaluation set, error analysis, and an API.

### Path B: Data Scientist / ML Engineer
**Sequence:** Data Analysis → Statistics → Data Science → ML → model deployment

**Planning estimate:** About 6–10 months for a focused, part-time plan after a solid analyst foundation.

**Focus on:** Statistics, experimentation, feature engineering, validation, tabular modeling, and model monitoring.

**Portfolio project:** A forecasting or churn model with a baseline comparison and a prediction endpoint.

### Path C: Big Data / Data Engineer
**Sequence:** Data Analysis → Advanced SQL → Data Modeling → ETL/ELT → Spark → Cloud and orchestration

**Planning estimate:** About 4–8 months to build solid starter projects after a good SQL/Python foundation.

**Focus on:** SQL, databases, pipelines, data quality, distributed processing, and reliable infrastructure.

**Portfolio project:** A scheduled pipeline that validates raw data, transforms it with PySpark, and publishes analytics-ready tables.

### Path D: Computer Vision Engineer
**Sequence:** Data Analysis → ML → PyTorch/Deep Learning → Computer Vision → deployment

**Planning estimate:** About 9–12 months for a focused, part-time learning plan.

**Focus on:** Image preparation, transfer learning, object detection, evaluation, and inference performance.

**Portfolio project:** Fine-tune an object detector and benchmark precision, recall, speed, and failure cases.

## 6. Recommendation

A practical strategy is to **pursue Data Analyst opportunities while continuing to learn**, then move toward Data Science or engineering with stronger professional experience.

Given a background that already includes Python, SQL, and Docker, a sensible specialization route is:

1. Finish the Data Analyst portfolio and interview preparation.
2. Learn Data Science and conventional Machine Learning fundamentals.
3. Specialize in **Applied ML and LLM Engineering** if building AI products is the goal.
4. Keep **Big Data Engineering** as an alternative if data pipelines and infrastructure are more appealing than modeling.
5. Choose **Computer Vision** deliberately if you enjoy image and video problems.

You do not need to finish all seven fields before applying for jobs. Focus on one target role, build projects that prove the relevant skills, and be ready to explain your design choices, evaluation, limitations, and business value.

## Sources and Caveats

- AI/LLM Jobs, salary guide: https://aillmjobs.com/salaries
- US Bureau of Labor Statistics, Data Scientists: https://www.bls.gov/ooh/math/data-scientists.htm
- Pearson Carter, Data & AI hiring guide: https://www.pearsoncarter.com/hiring-guides/data-ai-2026
- IranTalent, Data Science and AI Expert salary: https://salary.irantalent.com/salary-report/data-science-ai-expert-salary/

The timelines are study-planning estimates, not hiring guarantees. Salary data is time-sensitive and should be verified against current job postings and reputable salary surveys before negotiation.
