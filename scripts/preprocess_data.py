import pandas as pd

def preprocess():
    # Load raw data
    df = pd.read_csv('data/raw/raw_reviews.csv')
    
    # 1. Remove duplicates based on review_id
    initial_count = len(df)
    df = df.drop_duplicates(subset=['review_id'])
    
    # 2. Handle missing values
    df = df.dropna(subset=['review', 'rating'])
    
    # 3. Normalize dates to YYYY-MM-DD
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    
    # 4. Final selection of columns
    df = df[['review', 'rating', 'date', 'bank', 'source']]
    
    # Save cleaned data
    df.to_csv('data/cleaned_reviews.csv', index=False)
    
    print(f"Original: {initial_count} rows")
    print(f"Cleaned: {len(df)} rows")
    print("Cleaned data saved to data/cleaned_reviews.csv")

if __name__ == "__main__":
    preprocess()