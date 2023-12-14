# Dataset Preparation for QA Llama 2 Model

## Overview
This document outlines the steps to preprocess and transform the dataset for training and testing the QA Llama 2 model. The process involves three main steps: dataset separation, data cleaning, and trimming the test dataset.

## Steps

### 1. Dataset Separation
Use the `generate_data.py` script to separate the dataset into training and testing subsets. 
- Training Dataset: Consists of 2500 rows.
- Testing Dataset: Consists of 101 rows.

Run this script separately for generating the train and test datasets.

### 2. Data Cleaning
After separating the datasets, run the `clean_text.py` script to clean the `article_text` column in the dataset. This script will replace placeholders like `-LRB-` and `-RRB-` with the actual characters `(` and `)` respectively, ensuring clarity in the text.

To clean the dataset, use the following command:

**python clean_text.py**

Make sure to adjust the file path in the script to point to your specific dataset file.

### 3. Trimming the Test Dataset
For the test dataset, an additional step is required after cleaning. Use the `trim_test_101.py` script to trim the `prompt` so that the answer text is removed from it. This step is crucial for ensuring that the test dataset only contains relevant information for evaluation.

To trim the test dataset, use the following command:

**python trim_test_101.py**

Again, ensure the file path in the script is correctly set to your test dataset file.

## Additional Notes
- Ensure that Python and Pandas are installed in your environment to run these scripts.
- Modify the file paths in the scripts as per your directory structure.
- These preprocessing steps are essential for the effective training and testing of the QA Llama 2 model.
