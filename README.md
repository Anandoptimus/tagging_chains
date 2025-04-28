# 📄 LangChain Text Tagging

This project uses **LangChain** and **OpenAI Function Calling** to automatically **tag a given text** into:

- **Sentiment** (`pos`, `neg`, `neutral`)
- **Language** (ISO-639-1 code)
- **Gender context** (e.g., `self`, `man`, `woman`, `group`, `non-living`)

It showcases how to build a function-calling chain using **Pydantic**, **LangChain**, and **OpenAI models**.

---

## ✨ Features

- Automatic sentiment detection: **positive**, **negative**, or **neutral**.
- Language tagging: returns the **ISO-639-1** two-letter code.
- Gender context detection: based on pronouns or references inside the text.
- **Built with**:
  - LangChain
  - OpenAI GPT-3.5 Turbo
  - Pydantic

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/langchain-tagging.git
cd langchain-tagging
```

### 2. Install Required Packages
pip install -r requirements.txt

### 3. Set Your OpenAI API Key
export OPENAI_API_KEY="your-api-key-here"

### 4. Run the Script
python tagging_chain.py

## 📚 Notes
- This project uses the function-calling feature of OpenAI GPT models.
- The model is forced to call the Tagging function using function_call={"name": "Tagging"}.
- You can extend this by adding more fields (like emotion, entity recognition, etc.)

## 🤝 Contribution
- If you find any improvements or want to add more tagging categories, feel free to raise an Issue or a Pull Request!


