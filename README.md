# 🧬 Virology and Epidemiology AI Research Collection

This repository contains the dataset [`collection_with_abstracts.csv`](https://github.com/jd-coderepos/virology-ai-papers/blob/main/collection_with_abstracts.csv), compiled via queries issued to the [PubMed](https://pubmed.ncbi.nlm.nih.gov/) database. PubMed is one of the largest databases indexing publications in the Life Sciences.

## 📊 Dataset Scope

This dataset includes papers from PubMed that address problems in virology or epidemiology using deep learning neural network-based solutions. The dataset consists of 11,450 unique papers. For more detailed insights into the queries used to compile this collection, please view [this document](https://docs.google.com/document/d/1uMkXik3B3rNnKLbZc5AyqWruTGUKdpJcZFZZ4euM0Aw/edit?usp=sharing).

## 📑 Data Columns Description

Each row in the `collection_with_abstracts.csv` file corresponds to a unique academic paper, structured with the following columns:

- **PMID**: PubMed ID, a unique identifier for each publication.
- **Title**: Title of the publication.
- **Authors**: List of authors in the format `Last Name, First Initials`.
- **Citation**: Citation details, typically including volume, issue, and pages.
- **First Author**: The first listed author of the paper.
- **Journal/Book**: The name of the journal or book in which the paper is published.
- **Publication Year**: The year the paper was published.
- **Create Date**: The date the record was created in PubMed.
- **PMCID**: PubMed Central ID, linking to the full text of the article in the [PubMed Central](https://pmc.ncbi.nlm.nih.gov/) database. This field is optional and may not be present for all records.
- **NIHMS ID**: NIH Manuscript Submission ID, used when a paper is included in NIH public access policy compliance. This field is optional and may not be present for all records.
- **DOI**: Digital Object Identifier, providing a persistent link to its location on the internet. This field is optional and may not be present for all records.
- **Abstract**: The abstract of the publication. This field is optional and may not be present for all records.

### ❗ Note on Optional Fields

Fields marked as "optional" may not be present for all records within the dataset. This indicates that certain information is not available or applicable for those specific entries.

## 🌐 Accessing Full Texts

The PubMed Central (PMC) database, a subset of PubMed records, provides access to the full text of articles in XML format or other formats. Articles can be accessed via the API using the following URL: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=[insert-pmcid-here]`, where `[insert-pmcid-here]` is to be replaced with the actual PMCID of the article.
