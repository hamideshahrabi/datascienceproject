# 🧠 End-to-End Data Science Project

This repository demonstrates the design and implementation of a complete **Machine Learning pipeline** from data ingestion to model evaluation. It showcases best practices in modular development, configuration-driven workflows, experiment tracking, and pipeline orchestration.

---

## 🚀 Project Overview

This project is structured to represent a real-world production-ready ML system. It uses a modular, scalable, and configurable approach with the help of:

- **YAML-based configuration management**
- **Object-oriented design patterns**
- **MLflow & DagsHub for experiment tracking**
- **Dockerized environment for deployment**

---

## 🧩 Key Pipeline Stages

1. **Data Ingestion**
   - Downloads or loads the raw dataset.
   - Stores the data in the artifact folder.

2. **Data Validation**
   - Validates schema and data types.
   - Handles missing values and basic sanity checks.

3. **Data Transformation**
   - Performs preprocessing and feature engineering.
   - Converts raw data into model-ready format.

4. **Model Training**
   - Trains machine learning models using configurable hyperparameters.
   - Stores trained models as binary artifacts.

5. **Model Evaluation**
   - Evaluates model performance using custom metrics.
   - Integrates **MLflow** and **DagsHub** for tracking experiments and visualizing results.

---

## 🔧 Project Workflow

To run or modify the pipeline, follow the steps below:

1. ✅ **Update Configuration Files**  
   - `config.yaml`: Paths and global settings  
   - `schema.yaml`: Data schema definition  
   - `params.yaml`: Model hyperparameters  

2. 🔁 **Define Entity Classes**  
   - In `src/entity`, define dataclasses for structured config handling.

3. 🧠 **Configure with Configuration Manager**  
   - Use `src/config/configuration.py` to manage and return configuration objects.

4. 🧱 **Update Pipeline Components**  
   - Modular logic lives in `src/components/`: ingestion, validation, transformation, etc.

5. 🔄 **Update Pipeline Scripts**  
   - Each pipeline (e.g., `data_ingestion_pipeline.py`) glues together the components.

6. ▶️ **Run `main.py`**  
   - Orchestrates the entire ML workflow end-to-end.

---

## 🗂 Project Structure
