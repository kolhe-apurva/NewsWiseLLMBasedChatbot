import pandas as pd

# Load the data from the CSV file
file_path = 'train_data_2500_rows.csv'  # Replace with the path to your CSV file
df = pd.read_csv(file_path)

def clean_text(text):
    if pd.isna(text):
        # Return NaN as it is
        return text
    # Replace '-LRB-' with '(' and '-RRB-' with ')'
    text = text.replace('-LRB-', '(').replace('-RRB-', ')')
    return text

# Apply the clean_text function to each column
df['question'] = df['question'].apply(clean_text)
df['answer'] = df['answer'].apply(clean_text)
df['prompt'] = df['prompt'].apply(clean_text)

# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_train_data_2500_rows.csv', index=False)
