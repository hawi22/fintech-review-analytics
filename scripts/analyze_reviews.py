import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from collections import Counter
import os

nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

def perform_analysis():
    df = pd.read_csv('data/cleaned_reviews.csv')
    
    # Rename for assignment requirements
    df = df.rename(columns={'review': 'review_text'})
    df['review_text'] = df['review_text'].astype(str)

    # 2. Sentiment
    sid = SentimentIntensityAnalyzer()
    def get_vader_sentiment(text):
        score = sid.polarity_scores(text)['compound']
        label = "POSITIVE" if score >= 0.05 else "NEGATIVE" if score <= -0.05 else "NEUTRAL"
        return label, score

    sentiments = df['review_text'].apply(get_vader_sentiment)
    df['sentiment_label'] = [x[0] for x in sentiments]
    df['sentiment_score'] = [x[1] for x in sentiments]

    # 3. Themes
    stop_words = set(stopwords.words('english'))
    # Added more stop words to get BETTER themes
    stop_words.update(['app', 'bank', 'banking', 'cbe', 'boa', 'dashen', 'good', 'nice', 'please', 'money', 'worst', 'ever', 'even', 'time'])
    
    def get_keywords(text):
        tokens = nltk.word_tokenize(text.lower())
        return [word for word in tokens if word.isalpha() and word not in stop_words and len(word) > 3]

    df['identified_theme'] = "General Feedback"

    for bank in df['bank'].unique():
        neg_reviews = df[(df['bank'] == bank) & (df['sentiment_label'] == 'NEGATIVE')]['review_text']
        all_keywords = []
        for rev in neg_reviews:
            all_keywords.extend(get_keywords(rev))
        
        top_themes = Counter(all_keywords).most_common(3)
        print(f"--- {bank} Improved Themes: {top_themes} ---")
        
        if top_themes:
            top_word = top_themes[0][0]
            mask = (df['bank'] == bank) & (df['review_text'].str.contains(top_word, case=False))
            df.loc[mask, 'identified_theme'] = f"Issue: {top_word}"

    # 4. Final selection - including bank and date for Task 3
    # Note: We need bank and rating for the database later
    df.to_csv('data/analyzed_reviews.csv', index=False)
    
    # Create the specialized task-2 output file for the evaluators
    task2_output = df[['review_id', 'review_text', 'sentiment_label', 'sentiment_score', 'identified_theme']]
    task2_output.to_csv('data/task2_final_output.csv', index=False)
    
    print("\nSuccess! Files saved in data/ folder.")

if __name__ == "__main__":
    perform_analysis()