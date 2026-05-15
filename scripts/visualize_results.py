import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_visualizations():
    # 1. Load data from the analyzed CSV
    df = pd.read_csv('data/analyzed_reviews.csv')
    os.makedirs('data/plots', exist_ok=True)
    
    # Set the style
    sns.set_theme(style="whitegrid")
    
    # --- Plot 1: Sentiment Distribution by Bank ---
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='bank', hue='sentiment_label', palette='viridis')
    plt.title('Sentiment Distribution across Ethiopian Banks')
    plt.xlabel('Bank Name')
    plt.ylabel('Number of Reviews')
    plt.legend(title='Sentiment')
    plt.savefig('data/plots/sentiment_distribution.png')
    print("Saved Plot 1: Sentiment Distribution")

    # --- Plot 2: Average Rating per Bank ---
    plt.figure(figsize=(10, 6))
    avg_ratings = df.groupby('bank')['rating'].mean().sort_values()
    avg_ratings.plot(kind='bar', color='skyblue')
    plt.title('Average User Rating (1-5 Stars)')
    plt.ylabel('Mean Rating')
    plt.ylim(1, 5)
    plt.savefig('data/plots/average_rating.png')
    print("Saved Plot 2: Average Rating")

    # --- Plot 3: Common Issues (Themes) ---
    plt.figure(figsize=(12, 6))
    # Filter only reviews where an issue was identified
    issues_df = df[df['identified_theme'].str.contains('Issue:', na=False)]
    sns.countplot(data=issues_df, y='identified_theme', hue='bank', palette='magma')
    plt.title('Frequency of Identified Product Issues')
    plt.xlabel('Number of Mentions')
    plt.ylabel('Theme')
    plt.savefig('data/plots/theme_frequency.png')
    print("Saved Plot 3: Theme Frequency")

if __name__ == "__main__":
    generate_visualizations()