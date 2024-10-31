# Virology and Epidemiology AI Research Collection

This project compiles a dataset of academic papers focusing on **virology** and **epidemiology** that utilize **deep learning** techniques. The dataset, `collection_with_abstracts.csv`, consists of **11,450 unique papers** sourced from PubMed, indexed for easy access and analysis.

## Table of Contents
- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [Queries and Dataset Creation](#queries-and-dataset-creation)
- [NLP Techniques for Filtering](#nlp-techniques-for-filtering)
- [Dataset Statistics](#dataset-statistics)
- [Conclusion](#conclusion)
- [Usage Instructions](#usage-instructions)
- [Contributions](#contributions)

## Project Overview
This project aims to facilitate research in the fields of virology and epidemiology by providing a comprehensive collection of literature that employs deep learning methods. By utilizing automated queries and NLP techniques, we streamline the process of collecting and analyzing relevant academic publications.

## Setup Instructions
### Step 1: Set Up the Environment
1. **Install Required Software:**
   - Ensure Python 3.8+ is installed.
   - Set up a virtual environment:
     ```bash
     python3 -m venv env
     source env/bin/activate  # On Windows use `env\Scripts\activate`
     ```

2. **Install Required Libraries:**
   - Install the dependencies listed in the `requirements.txt` file:
   - ```bash
     # Data manipulation and analysis
      pandas==1.5.3

      # Natural Language Processing
      transformers==4.29.0
      torch==2.0.1  # Ensure you have the right version for your hardware

      # Additional libraries (if needed)
      numpy==1.23.5
      scikit-learn==1.2.2
      scipy==1.10.0

      # Optional: For working with Jupyter notebooks
      jupyterlab==3.6.1

      # Optional: For visualizations (if applicable)
      matplotlib==3.7.1
      seaborn==0.12.2

     ```
     #Install using Terminal
     ```bash
     pip install -r requirements.txt
     ```

### Step 2: Define PubMed Queries
- Construct and run the PubMed queries to retrieve relevant records for each deep learning technique. Export results to separate CSV files.

### Step 3: Compile and Deduplicate Results
- Load the CSV files, merge them, and remove duplicates based on the PMID column.

### Step 4: Analyze the Dataset
- Open `collection_with_abstracts.csv` to ensure data integrity.

### Step 5: Running the Script
- python main.py

### Step 6: Output
- The script will print a message indicating that the filtered dataset has been saved:
- The script successfully filtered the dataset and saved the results to a new file called filtered_virology_papers.csv. This file contains the papers that met your specified criteria regarding the use of deep learning approaches in virology and epidemiology.


## Dataset Statistics
- **Total Papers Retrieved**: 12,980
- **Unique Papers After Deduplication**: 11,450
- **Total Fields in Dataset**: 10 (PMID, Title, Authors, Citation, First Author, Journal/Book, Publication Year, Create Date, PMCID, DOI, Abstract)


## Conclusion
This project provides a structured approach to gathering and analyzing academic literature in virology and epidemiology using modern NLP techniques. By leveraging deep learning methods for filtering, we enhance the quality and relevance of the collected dataset.

