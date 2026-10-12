

import os
import json
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# 1. Setup
load_dotenv()

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🎯",
    layout="wide"
)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Add GROQ_API_KEY to your .env file.")
    st.stop()

client = Groq(api_key=api_key)
MODEL = "openai/gpt-oss-20b"


# 2. One function for every AI request
def ask_ai(prompt, history=None, json_mode=False):
    messages = [
        {
            "role": "system",
            "content": (
                "You are a friendly interview coach for freshers. "
                "Use simple English, examples, and accurate answers."
            )
        }
    ]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": prompt})

    options = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.3
    }

    if json_mode:
        options["response_format"] = {"type": "json_object"}

    response = client.chat.completions.create(**options)
    answer = response.choices[0].message.content

    if json_mode:
        return json.loads(answer)

    return answer


# 3. Website layout
st.title("🎯 AI Interview Preparation Assistant")
st.caption("Learn Python and Generative AI step by step")

ask_tab, questions_tab, mock_tab = st.tabs(
    ["💬 Ask AI", "📝 Generate Questions", "🎤 Mock Interview"]
)


# 4. Ask AI
with ask_tab:
    if "chat" not in st.session_state:
        st.session_state.chat = []

    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    question = st.chat_input("Ask anything about Python or GenAI")

    if question:
        history = st.session_state.chat.copy()

        st.session_state.chat.append(
            {"role": "user", "content": question}
        )

        try:
            with st.spinner("Thinking..."):
                answer = ask_ai(
                    question,
                    history=history
                )

            st.session_state.chat.append(
                {"role": "assistant", "content": answer}
            )
            st.rerun()

        except Exception as e:
            st.error(f"AI request failed: {e}")

    if st.button("Clear chat"):
        st.session_state.chat = []
        st.rerun()


# 5. Generate Questions
with questions_tab:
    topic = st.selectbox(
        "Topic",
        ["Python", "Generative AI", "LLMs", "RAG",
         "Prompt Engineering", "LangChain", "SQL"]
    )

    level = st.selectbox(
        "Difficulty",
        ["Beginner", "Intermediate", "Advanced"]
    )

    count = st.slider("Number of questions", 3, 10, 5)

    if st.button("Generate questions"):
        prompt = f"""
        Create exactly {count} interview questions for freshers.
        Topic: {topic}
        Difficulty: {level}

        Return a JSON object with a "questions" list.
        Each item must have:
        "question", "answer", "explanation", "difficulty".
        Keep answers accurate and explanations simple.
        """

        try:
            with st.spinner("Creating questions..."):
                result = ask_ai(prompt, json_mode=True)

            st.session_state.questions = result["questions"]

        except Exception as e:
            st.error(f"Question generation failed: {e}")

    for i, q in enumerate(
        st.session_state.get("questions", []), start=1
    ):
        with st.expander(f"{i}. {q['question']}"):
            st.write("**Suggested answer:**", q["answer"])
            st.write("**Simple explanation:**", q["explanation"])
            st.caption(q["difficulty"])


# 6. Mock Interview
with mock_tab:
    topic = st.selectbox(
        "Interview topic",
        ["Python", "Generative AI", "LLMs", "RAG"],
        key="mock_topic"
    )

    if st.button("Get a question"):
        prompt = f"""
        Create one {topic} interview question for a fresher.
        Return JSON with "question" and "ideal_answer".
        """

        try:
            st.session_state.mock = ask_ai(
                prompt, json_mode=True
            )
            st.session_state.pop("feedback", None)
            st.session_state.pop("candidate_answer", None)

        except Exception as e:
            st.error(f"Could not create question: {e}")

    mock = st.session_state.get("mock")

    if mock:
        st.write("### Interview question")
        st.write(mock["question"])

        answer = st.text_area(
            "Your answer",
            key="candidate_answer"
        )

        if st.button("Evaluate my answer"):
            if not answer.strip():
                st.warning("Please enter your answer first.")
            else:
                prompt = f"""
                Evaluate this fresher's interview answer fairly.

                Question: {mock['question']}
                Expected answer: {mock['ideal_answer']}
                Candidate answer: {answer}

                Return JSON with:
                "score" (integer from 0 to 10),
                "strengths" (list of strings),
                "improvements" (list of strings),
                "better_answer" (string).
                Give partial marks for partially correct answers.
                """

                try:
                    with st.spinner("Checking your answer..."):
                        st.session_state.feedback = ask_ai(
                            prompt, json_mode=True
                        )

                except Exception as e:
                    st.error(f"Evaluation failed: {e}")

    feedback = st.session_state.get("feedback")

    if feedback:
        st.metric("Your score", f"{feedback['score']}/10")

        st.write("**Strengths**")
        for item in feedback["strengths"]:
            st.write(f"- {item}")

        st.write("**Improvements**")
        for item in feedback["improvements"]:
            st.write(f"- {item}")

        st.write("**A stronger answer**")
        st.write(feedback["better_answer"])
