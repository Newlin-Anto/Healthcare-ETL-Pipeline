# 🏥 Healthcare ETL Pipeline using PySpark & Hadoop

## Project Overview

This project is an end-to-end **Healthcare ETL (Extract, Transform, Process, Load) pipeline** built using **PySpark and Hadoop HDFS**.

The pipeline reads raw healthcare data from Hadoop HDFS, performs data cleaning and validation, transforms the data, generates analytical datasets, and stores the processed results in **Parquet format**.

## Architecture

```text
                    ┌─────────────────────┐
                    │   Healthcare CSV    │
                    │     Raw Dataset     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Hadoop HDFS     │
                    │     Raw Layer       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      EXTRACT        │
                    │      PySpark        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     TRANSFORM       │
                    │  Data Cleaning &    │
                    │   Validation        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      PROCESS        │
                    │ Feature Engineering │
                    │ & Aggregations      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        LOAD         │
                    │  Parquet Files in   │
                    │        HDFS         │
                    └─────────────────────┘
```

## 🛠️ Technologies Used

- Python
- PySpark
- Apache Hadoop
- HDFS
- Apache Spark
- Linux
- Parquet

## 📂 Project Structure

```text
healthcare-etl/
│
├── extract/
│   └── extract_data.py
│
├── transform/
│   └── transform_data.py
│
├── process/
│   └── process_data.py
│
├── load/
│   └── load_data.py
│
├── scripts/
│   └── run_pipeline.py
│
└── README.md
```

# ETL Pipeline

## 1️⃣ Extract

The pipeline reads the raw healthcare dataset from **Hadoop HDFS** using PySpark.

**Input Path:**

```text
hdfs://localhost:9000/healthcare/raw/healthcare_dataset.csv
```

The CSV file is loaded with:

- Header enabled
- Automatic schema inference

## 2️⃣ Transform

The transformation stage performs data cleaning and validation.

### Data Quality Checks

The pipeline checks for:

- Duplicate records
- Distinct values in categorical columns
- Minimum and maximum age
- Invalid billing amounts
- Invalid admission and discharge dates

### Data Cleaning

The pipeline:

- Removes duplicate records
- Removes records with invalid billing amounts
- Standardizes patient names using proper capitalization

## 3️⃣ Process

The processed healthcare data is enriched with additional business features.

### Stay Duration

The pipeline calculates the patient's hospital stay duration:

```text
Discharge Date - Date of Admission
```

### Age Groups

Patients are categorized into:

- Child
- Adult
- Senior

### Hospital Summary

The pipeline generates hospital-level metrics:

- Patient Count
- Total Billing
- Average Billing
- Average Stay Duration

### Insurance Summary

The pipeline generates insurance-provider metrics:

- Patient Count
- Total Billing
- Average Billing

## 4️⃣ Load

The final datasets are stored in **Parquet format** in Hadoop HDFS.

### Output Datasets

```text
/healthcare/processed/patient_data
```

```text
/healthcare/processed/hospital_summary
```

```text
/healthcare/processed/insurance_summary
```

# How to Run the Project

## Step 1: Start Hadoop Services

Make sure Hadoop and HDFS are running.

```bash
start-dfs.sh
```

Check the running services:

```bash
jps
```

## Step 2: Upload Raw Data to HDFS

Create the required HDFS directory:

```bash
hdfs dfs -mkdir -p /healthcare/raw
```

Upload the healthcare dataset:

```bash
hdfs dfs -put healthcare_dataset.csv /healthcare/raw/
```

Verify the file:

```bash
hdfs dfs -ls /healthcare/raw
```

## Step 3: Run the PySpark Pipeline

Navigate to the project directory and run:

```bash
python scripts/run_pipeline.py
```

## Step 4: Verify Output

Check the processed datasets:

```bash
hdfs dfs -ls /healthcare/processed
```

You should see:

```text
patient_data
hospital_summary
insurance_summary
```

# Data Flow

```text
Healthcare CSV
      ↓
HDFS Raw Layer
      ↓
Extract
      ↓
Transform & Data Validation
      ↓
Processing & Feature Engineering
      ↓
Aggregations
      ↓
Parquet Files
      ↓
HDFS Processed Layer
```

# Author

**Newlin Anto Marian C**

Aspiring Data Engineer | Python | PySpark | SQL | Hadoop | AWS

🔗 LinkedIn: www.linkedin.com/in/new-lin
