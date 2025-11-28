import ollama
import csv
import os
from datetime import datetime

# Configuration
MODEL = "llama3"
CSV_FILE = "sentiment_log.csv"


# Function to append data to CSV
def save_to_csv(text, sentiment):
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Input Text", "Sentiment"])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), text, sentiment])
        print(f"💾 Saved to {CSV_FILE}")


# Strict Zero-Shot Prompt (Definitions, not Examples)
system_prompt = (
    "You are a strict sentiment classifier. "
    "Analyze the input and determine the sentiment based on these rules:\n"
    "1. Positive: Expresses happiness, satisfaction, or praise.\n"
    "2. Negative: Expresses anger, complaints, criticism, or mentions defects/failures.\n"
    "3. Neutral: Factual statements, questions, or time/date mentions with NO emotion/failure.\n"
    "Your ONLY response MUST be one single word: 'Positive', 'Negative', or 'Neutral'."
)

# Main Execution Loop
print(f"\n--- Zero-Shot Sentiment Analyzer ({MODEL}) ---")
print(f"Logging to: {CSV_FILE}")
print("Type 'exit' or 'quit' to stop.")

while True:
    try:
        text_to_analyze = input("\nEnter text to analyze: ")

        if text_to_analyze.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        # API Call
        response = ollama.chat(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text_to_analyze},
            ],
        )

        # Processing
        raw_sentiment = response["message"]["content"]
        clean_sentiment = raw_sentiment.strip().title()

        # Display
        if "Positive" in clean_sentiment:
            print(f"✅ Sentiment: {clean_sentiment}")
        elif "Negative" in clean_sentiment:
            print(f"❌ Sentiment: {clean_sentiment}")
        elif "Neutral" in clean_sentiment:
            print(f"😐 Sentiment: {clean_sentiment}")
        else:
            print(f"⚠️ Raw Output: {raw_sentiment}")

        # Save
        save_to_csv(text_to_analyze, clean_sentiment)

    except Exception as e:
        print(f"Error: {e}")
