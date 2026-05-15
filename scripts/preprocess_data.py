import pandas as pd
import os

def preprocess():
    df = pd.read_csv('data/raw/raw_reviews.csv')
    df = df.drop_duplicates(subset=['review_id'])
    df = df.dropna(subset=['review', 'rating'])
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    
    # CRITICAL: Keep all columns for the next steps
    df = df[['review_id', 'review', 'rating', 'date', 'bank', 'source']]
    
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/cleaned_reviews.csv', index=False)
    print("Preprocess Success: 'review_id' is now in cleaned_reviews.csv")

if __name__ == "__main__":
    preprocess()