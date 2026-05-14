# Fintech Review Analytics: Ethiopian Banking Sector

## Overview
This project provides a data-driven analysis of user reviews for the top three Ethiopian banks: Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank. By analyzing Play Store feedback, we aim to provide actionable insights for product managers to improve customer retention and app performance.

---

## Task 1: Data Collection & Preprocessing

### 1. Scraping Methodology
- **Source:** Google Play Store.
- **Tool:** Python library `google-play-scraper`.
- **Target Apps:** 
    - Commercial Bank of Ethiopia (CBE) - `com.combanketh.mobilebanking`
    - Bank of Abyssinia (BOA) - `com.boa.boaMobileBanking`
    - Dashen Bank - `com.dashen.dashensuperapp`
- **Volume:** Collected 500 reviews per bank to ensure a robust sample size .
- **Attributes Collected:** Review ID, Review Text, Rating (1-5), Date, Bank Name, and Source.

### 2. Date Range
- **Start Date:** 12/02/2025
- **End Date:** 13/05/2026
- *Note: Reviews were collected using the `Sort.NEWEST` parameter to capture the most recent user sentiment following recent app updates.*

### 3. Preprocessing Steps
To ensure data quality, the following steps were performed using `pandas`:
- **De-duplication:** Removed duplicate entries based on the unique `review_id`.
- **Missing Values:** Dropped rows where the review text or rating was missing (Null).
- **Standardization:** 
    - Converted all dates to the `YYYY-MM-DD` format.
    - Simplified the dataset to the required columns: `review`, `rating`, `date`, `bank`, and `source`.

### 4. Limitations Encountered
- **Rate Limiting:** While `google-play-scraper` is efficient, scraping larger volumes (10,000+) would require request throttling to avoid IP blocks.
- **Language Barrier:** A small portion of reviews are written in Amharic using Latin script or Ge'ez script. The current NLP pipeline is optimized for English, which may lead to "Neutral" sentiment scores for non-English text.
- **Store Limitation:** This analysis only covers Android users (Google Play). iOS (App Store) reviews are not included in this dataset.