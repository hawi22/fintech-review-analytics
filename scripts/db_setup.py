import pandas as pd
from sqlalchemy import create_engine, text
import os

def populate_database():
    # 1. Load the data
    file_path = 'data/analyzed_reviews.csv'
    if not os.path.exists(file_path):
        print("Analyzed data not found! Run Task 2 first.")
        return
    
    df = pd.read_csv(file_path)

    # 2. Database Connection
   
    engine = create_engine('postgresql://postgres:admin123@localhost:5432/bank_reviews')

    # 3. Create Tables from the schema.sql file
    with engine.connect() as conn:
        with open('scripts/schema.sql') as f:
            conn.execute(text(f.read()))
            conn.commit()
    
    # 4. Get Bank IDs from the DB to map them correctly
    banks_df = pd.read_sql("SELECT bank_id, bank_name FROM banks", engine)
    bank_map = dict(zip(banks_df['bank_name'], banks_df['bank_id']))

    # 5. Prepare the data for insertion
    df['bank_id'] = df['bank'].map(bank_map)
    
    # Select only columns that match our SQL schema
    db_df = df[[
        'review_id', 'bank_id', 'review_text', 'rating', 
        'date', 'sentiment_label', 'sentiment_score', 
        'identified_theme', 'source'
    ]]
    
    # Rename 'date' to 'review_date' to match schema
    db_df = db_df.rename(columns={'date': 'review_date'})

    # 6. Insert data into PostgreSQL
    print("Inserting data into PostgreSQL...")
    db_df.to_sql('reviews', engine, if_exists='append', index=False)
    
    print("Database populated successfully!")

if __name__ == "__main__":
    populate_database()