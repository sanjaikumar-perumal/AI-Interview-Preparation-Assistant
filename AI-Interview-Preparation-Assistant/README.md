# 🎯 AI Interview Preparation Assistant

An AI-powered interview preparation application built using **Python, Streamlit, and Groq API**. It helps freshers prepare for Python and Generative AI interviews through simple explanations, question generation, mock interviews, and automated feedback.

## 🚀 Features

- **Ask AI:** Get simple explanations for Python, Generative AI, LLMs, RAG, and related topics.
- **Generate Questions:** Create interview questions based on topic, difficulty, and question count.
- **Mock Interview:** Answer AI-generated interview questions and receive feedback.
- **Answer Evaluation:** Get a score, strengths, areas for improvement, and a better sample answer.
- **Structured Output:** Use JSON responses for organized question generation and answer evaluation.
- **Beginner-Friendly:** Designed to help freshers prepare for technical interviews.

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- LLMs
- JSON
- python-dotenv

## 📂 Project Structure

AI-Interview-Preparation-Assistant/

├── app.py
├── requirements.txt

├── .env.example
├── .gitignore
├── README.md
├── assets/
│   └── screenshots/
└── LICENSE

## ⚙️ Installation and Setup

### 1. Create a virtual environment (recommended)

Type this on your vs/any other terminal(new terminal) 
python -m venv .venv


Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

python -m pip install -r requirements.txt


### 4. Configure your API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_actual_api_key_here
```

Get an API key from [Groq Console](https://console.groq.com/).

**Important:** Never upload your real API key or `.env` file to GitHub.

### 5. Run the application

streamlit run app.py

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 💡 How to Use

1. Open **Ask AI** to learn technical concepts.
2. Select a topic and difficulty in **Generate Questions**.
3. Open **Mock Interview** to answer a question.
4. Review your score, strengths, improvements, and suggested answer.

## 🎓 Learning Objectives

- Understand how to integrate an LLM API into a Python application.
- Practice prompt engineering.
- Generate structured JSON responses.
- Maintain conversational history.
- Build an interactive web application with Streamlit.
- Explore AI-powered interview answer evaluation.

## 🔮 Future Enhancements

- Resume-based interview question generation.
- Voice input and spoken answers.
- Interview history and progress tracking.
- Resume and job-description analysis.
- Deployment for public access.

## 👨‍💻 Author

**Sanjaikumar-perumal**

Aspiring Generative AI Developer | Python | LLMs | RAG

