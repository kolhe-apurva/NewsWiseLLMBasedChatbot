import pandas as pd

# Load the data from the CSV file
file_path = 'train_with_text.csv'  # Path to CSV file
df = pd.read_csv(file_path)

# Function to process each group
def process_group(group):
    story_text = group['story_text'].iloc[0]  # same for all rows in the group
    prompt = "[INST] Answer the given question based on the news article below : Article: " + story_text + " [/INST]\n"
    prompt += "Sure! What is your question?\n"
    prompt += "[INST] QUESTION : " + group['question'] + " [/INST]\n"
    prompt += group['extracted_text'] + "\n"
    return pd.DataFrame({
        'question': group['question'],
        'answer': group['extracted_text'],
        'prompt': prompt
    })

# Group by 'story_id' and apply the function
processed_df = df.groupby('story_id').apply(process_group).reset_index(drop=True)

# Save only the x rows of the processed DataFrame to a CSV file
processed_df.iloc[3000:3100].to_csv('test_100_rows.csv', index=False)
