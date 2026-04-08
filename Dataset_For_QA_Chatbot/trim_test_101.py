import pandas as pd

# Read the CSV file
df = pd.read_csv('test_101_rows.csv')

# Function to trim the prompt after the last [/INST]
def trim_prompt(prompt):
    index = prompt.rfind('[/INST]')
    if index != -1:
        return prompt[:index + len('[/INST]')]
    return prompt

# Apply the function to the 'prompt' column
df['prompt'] = df['prompt'].apply(trim_prompt)

# Save the modified DataFrame to a new CSV file
df.to_csv('test_101_rows_trimmed.csv', index=False)
