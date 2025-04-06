import streamlit as st
import random
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Pakistani Law RAG System", layout="centered")
st.title("🇵🇰 Legal Intelligence Assistant")
st.markdown("Enter a query related to Pakistani law to receive analysis and support.")

# Simulated legal database
legal_knowledge = [
    {
        "section": "Article 23",
        "summary": "Every citizen shall have the right to acquire, hold and dispose of property.",
        "topic": "Property rights",
        "prediction": "Petitioner likely to succeed based on ownership documents and Article 23."
    },
    {
        "section": "Section 295-C PPC",
        "summary": "Whoever by words, gestures or insinuation defiles the name of Prophet Muhammad (PBUH) shall be punished with death or life imprisonment.",
        "topic": "Blasphemy",
        "prediction": "High risk of capital punishment; defense must prove lack of intent."
    },
    {
        "section": "Muslim Family Laws Ordinance 1961",
        "summary": "Daughters are entitled to inherit property from deceased parents.",
        "topic": "Inheritance rights",
        "prediction": "Daughter's inheritance claim is valid under 1961 Ordinance."
    },
    {
        "section": "Article 25",
        "summary": "All citizens are equal before law and entitled to equal protection of law.",
        "topic": "Gender equality",
        "prediction": "Discriminatory treatment likely to be struck down by court."
    },
    {
        "section": "Section 302 PPC",
        "summary": "Punishment for murder (Qatl-e-Amd).",
        "topic": "Criminal law",
        "prediction": "Accused likely to face life imprisonment under Section 302."
    }
]

# -------------------------
# Functions
# -------------------------
def retrieve_summary_and_issues(query):
    matches = [item for item in legal_knowledge if query.lower() in item["topic"].lower() or query.lower() in item["summary"].lower()]
    if not matches:
        return None
    match = random.choice(matches)
    return match

def decision_support():
    tips = [
        "Use landmark cases to reinforce legal position.",
        "Consider gender-sensitive and minority rights approach.",
        "Focus on constitutional protections to strengthen your case."
    ]
    return random.choice(tips)

# -------------------------
# UI + Logic
# -------------------------
query = st.text_input("🔍 Enter your legal issue (e.g. property, blasphemy, inheritance):")

if query:
    match = retrieve_summary_and_issues(query)
    if match:
        st.subheader("📑 Legal Summary")
        st.info(match["summary"])

        st.subheader("⚖️ Relevant Law Section")
        st.success(f"{match['section']} — Related to {match['topic']}")

        st.subheader("🔎 Predicted Case Outcome")
        st.warning(match["prediction"])

        st.subheader("🧠 Decision Support Suggestion")
        st.code(decision_support())

        # Evaluation Metrics (Simulated)
        st.subheader("📊 Evaluation Metrics (Simulated)")
        metrics = {"Accuracy": 0.87, "Precision": 0.83, "Recall": 0.79, "F1-Score": 0.81}
        fig, ax = plt.subplots()
        sns.barplot(x=list(metrics.keys()), y=list(metrics.values()), palette="viridis", ax=ax)
        ax.set_ylim(0, 1)
        st.pyplot(fig)

    else:
        st.error("No legal knowledge found for that query. Try another keyword.")
