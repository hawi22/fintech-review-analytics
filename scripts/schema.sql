-- Create Banks Table
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name VARCHAR(100) UNIQUE,
    app_id VARCHAR(100)
);

-- Create Reviews Table
CREATE TABLE IF NOT EXISTS reviews (
    review_id VARCHAR(255) PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT,
    rating INT,
    review_date DATE,
    sentiment_label VARCHAR(20),
    sentiment_score FLOAT,
    identified_theme VARCHAR(100),
    source VARCHAR(50)
);

-- Insert Bank Metadata
INSERT INTO banks (bank_name, app_id) VALUES 
('CBE', 'com.combanketh.mobilebanking'),
('BOA', 'com.boa.boaMobileBanking'),
('Dashen', 'com.dashen.dashensuperapp')
ON CONFLICT (bank_name) DO NOTHING;