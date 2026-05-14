from google_play_scraper import Sort, reviews
import pandas as pd
import os

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

def scrape_bank_reviews():
    all_reviews = []
    
    for bank_name, app_id in apps.items():
        print(f"Scraping {bank_name}...")
        
        # scrape 500 to ensure we have >400 after cleaning duplicates
        result, _ = reviews(
            app_id,
            lang='en',
            country='us', 
            sort=Sort.NEWEST,
            count=500 
        )
        
        for r in result:
            all_reviews.append({
                'review_id': r['reviewId'],
                'review': r['content'],
                'rating': r['score'],
                'date': r['at'],
                'bank': bank_name,
                'source': 'Google Play'
            })
            
    return pd.DataFrame(all_reviews)

if __name__ == "__main__":
    df = scrape_bank_reviews()
    # Create data directory if not exists
    os.makedirs('data/raw', exist_ok=True)
    df.to_csv('data/raw/raw_reviews.csv', index=False)
    print(f"Successfully scraped {len(df)} reviews.")