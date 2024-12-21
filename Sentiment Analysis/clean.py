import pandas as pd

# Define column names for the dataset
column_names = ['id', 'game', 'sentiment', 'text']

# Read the CSV file and assign column names
data = pd.read_csv("tweets.csv", names=column_names, header=None)

# Function to clean text data
def clean_text(text):
    if isinstance(text, str):  # Check if the value is a string
        return text.lower().strip()
    else:
        return ""  # Replace non-string values with an empty string

# Apply the cleaning function to the 'text' column
data['cleaned_text'] = data['text'].apply(clean_text)

# Display the first few rows of the dataset
print("Original Data:")
print(data.head())

print("\nCleaned Text Data:")
print(data[['id', 'game', 'sentiment', 'cleaned_text']].head())

# Save the cleaned dataset to a new CSV file if needed
data.to_csv("cleaned_data.csv", index=False)
