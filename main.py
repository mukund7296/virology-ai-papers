import pandas as pd
import re

# Load the dataset
df = pd.read_csv("collection_with_abstracts.csv")

# Define deep learning keywords and classification keywords
deep_learning_keywords = [
    "neural network", "artificial neural network", "machine learning model", 
    "feedforward neural network", "neural net algorithm", "multilayer perceptron", 
    "convolutional neural network", "recurrent neural network", "long short-term memory network", 
    "CNN", "GRNN", "RNN", "LSTM", "deep learning", "deep neural networks"
]

# Keywords for classification categories
text_mining_keywords = ["natural language processing", "NLP", "text mining", "language modeling"]
computer_vision_keywords = ["computer vision", "image processing", "object recognition", "scene understanding"]

# Helper function to check if any keywords are present in a text
def contains_keywords(text, keywords):
    return any(re.search(r'\b' + re.escape(keyword) + r'\b', text, re.IGNORECASE) for keyword in keywords)

# Step 1: Filter relevant papers based on deep learning keywords
filtered_df = df[df['Abstract'].apply(lambda x: contains_keywords(str(x), deep_learning_keywords) or contains_keywords(str(df['Title']), deep_learning_keywords))]

# Step 2: Classify papers based on method used
def classify_method(row):
    has_text_mining = contains_keywords(row['Abstract'], text_mining_keywords) or contains_keywords(row['Title'], text_mining_keywords)
    has_computer_vision = contains_keywords(row['Abstract'], computer_vision_keywords) or contains_keywords(row['Title'], computer_vision_keywords)
    
    if has_text_mining and has_computer_vision:
        return "both"
    elif has_text_mining:
        return "text mining"
    elif has_computer_vision:
        return "computer vision"
    else:
        return "other"

filtered_df['Method_Type'] = filtered_df.apply(classify_method, axis=1)

# Step 3: Extract method names (e.g., CNN, LSTM) from each relevant paper
def extract_method_name(text):
    found_methods = [method for method in deep_learning_keywords if re.search(r'\b' + re.escape(method) + r'\b', text, re.IGNORECASE)]
    return ", ".join(found_methods) if found_methods else "None"

filtered_df['Extracted_Method'] = filtered_df['Abstract'].apply(lambda x: extract_method_name(str(x)))

# Save the filtered and annotated dataset to a new CSV
filtered_df.to_csv("filtered_virology_papers.csv", index=False)

print("Filtered dataset saved as 'filtered_virology_papers.csv'")
print("Sample records:")
print(filtered_df.head())
