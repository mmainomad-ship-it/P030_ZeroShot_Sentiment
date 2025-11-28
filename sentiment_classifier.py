# Step 1: Import the library to communicate with your local Ollama instance
import ollama

# Define the model name (Ensure you have run 'ollama pull llama3')
MODEL = "llama3"

# Step 2: Get the text input from the user via the terminal
print("\n--- Zero-Shot Sentiment Analyzer ---")
text_to_analyze = input("Enter a sentence (review/tweet) to analyze: ")

# Step 3: Define the strict System Prompt for Zero-Shot classification
# We explicitly tell the model strictly what words it is allowed to output.
system_prompt = (
    "You are a strict, zero-shot sentiment classifier. "
    "Analyze the user's input and determine the sentiment. "
    "Your ONLY response MUST be one single word: 'Positive', 'Negative', or 'Neutral'."
)
# Step 4: Call the Ollama API to generate the classification
print(f"Analyzing using {MODEL}...")
response = ollama.chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text_to_analyze},
    ],
)

# Extract the raw text from the response object
raw_sentiment = response["message"]["content"]

# Step 5: Clean output and display visual results
# We normalize the string to Title Case (e.g., "positive " -> "Positive")
clean_sentiment = raw_sentiment.strip().title()

print("\n--- Result ---")
if clean_sentiment == "Positive":
    print(f"✅ Sentiment: {clean_sentiment}")
elif clean_sentiment == "Negative":
    print(f"❌ Sentiment: {clean_sentiment}")
elif clean_sentiment == "Neutral":
    print(f"😐 Sentiment: {clean_sentiment}")
else:
    # Fallback in case the model ignored instructions
    print(f"⚠️ Unexpected Output: {raw_sentiment}")
