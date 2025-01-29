import pandas as pd

# Load the dataset
file_path = "House_Data.csv"
df = pd.read_csv(file_path)

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values
df['size'].fillna('Unknown', inplace=True)  # Fill missing sizes with 'Unknown'
df['bath'].fillna(df['bath'].median(), inplace=True)  # Fill missing bathrooms with median value
df['balcony'].fillna(df['balcony'].median(), inplace=True)  # Fill missing balconies with median value
df.drop(columns=['society'], inplace=True)  # Drop 'society' due to high missing values
df.dropna(subset=['site_location'], inplace=True)  # Drop the single missing value in 'site_location'

# Handle outliers: Cap 'bath' at 99th percentile and 'price' at 99th percentile
bath_cap = df['bath'].quantile(0.99)
price_cap = df['price'].quantile(0.99)

df['bath'] = df['bath'].apply(lambda x: min(x, bath_cap))
df['price'] = df['price'].apply(lambda x: min(x, price_cap))

# Verify the cleaning process
print(df.info())
print(df.describe())