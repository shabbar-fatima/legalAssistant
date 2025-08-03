import streamlit as st
from summarize_document import summarize_document
from retrieve_precedents import get_relevant_precedents
from legal_recommendation import generate_legal_recommendation

# Streamlit App Interface
def main():
    st.title("Pakistani Legal Assistant")

    # Sidebar
    st.sidebar.header("Choose an option")
    option = st.sidebar.radio("Select a function", ("Summarize Legal Document", "Ask Legal Question"))

    if option == "Summarize Legal Document":
        st.header("Upload your Legal Document for Summarization")
        uploaded_file = st.file_uploader("Upload a Legal Document", type=["txt"])

        if uploaded_file is not None:
            document_text = uploaded_file.read().decode("utf-8")
            st.text_area("Document Content", document_text, height=200)

            if st.button("Summarize"):
                with st.spinner("Summarizing document..."):
                    summary = summarize_document(document_text)
                st.subheader("Document Summary:")
                st.write(summary)

    elif option == "Ask Legal Question":
        st.header("Ask Your Legal Question")
        user_query = st.text_area("Enter your legal question")

        if st.button("Get Precedents and Recommendation"):
            if user_query:
                with st.spinner("Retrieving precedents..."):
                    precedents = get_relevant_precedents(user_query)
                    recommendation = generate_legal_recommendation(user_query, precedents)
                
                st.subheader("Relevant Precedents:")
                st.write(precedents)
                
                st.subheader("Legal Recommendation:")
                st.write(recommendation)
            else:
                st.warning("Please enter a legal question.")

if __name__ == '__main__':
    main()
