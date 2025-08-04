import pandas as pd

# Use the correct file name here
df = pd.read_csv("netflix_titles.csv")

# Proceed with cleaning steps...
print("Initial Info:")
print(df.info())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(method='ffill', inplace=True)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert 'date_added' column if it exists
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce', dayfirst=True)

# Save cleaned dataset
df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned Info:")
print(df.info())
