# 🏷️ Project 30: Sentiment Analyzer (Zero-Shot)

## 📖 Description
This project is a Python-based sentiment analysis tool that utilizes a local **Llama 3** model (via Ollama). It demonstrates **Zero-Shot Learning**, where the model classifies text into specific categories (Positive, Negative, Neutral) based solely on prompt instructions, without prior training on specific examples.

## 🌟 Key Features
* **Local AI Processing:** Runs entirely offline using an RTX 3090.
* **Zero-Shot Classification:** Categorizes input without specific training data.
* **Strict Output Validation:** Ensures the LLM adheres to specific output formats.
* **Visual Feedback:** Uses emoji indicators for sentiment results.

## 🛠️ Technology Stack
* **Language:** Python 3.10+
* **AI Engine:** Ollama (Llama 3)
* **Library:** `ollama`

## 🚀 Setup Instructions
1.  **Prerequisite:** Ensure [Ollama](https://ollama.com/) is installed and running (`ollama serve`).
2.  **Pull Model:** Run `ollama pull llama3` in your terminal.
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Script:**
    ```bash
    python sentiment_classifier.py
    ```

## 👨‍💻 Author
**mmainomad-ship-it**
[GitHub Profile](https://github.com/mmainomad-ship-it)
Part of the "100 Days of AI Engineering" Challenge