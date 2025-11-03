import streamlit as st
from resume_reviewer import review_resume
import PyPDF2

st.title("AI Resume Reviewer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_role = st.text_input("Enter the job role you are targeting")

if uploaded_file is not None and job_role:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Resume Text:")
    st.text_area("Resume Content", text, height=200)

    if st.button("Analyze Resume"):
        with st.spinner("Reviewing your resume..."):
            review = review_resume(text, job_role)
        st.subheader("AI Review:")
        st.write(review)
elif uploaded_file and not job_role:
    st.warning("please enter you target job role.")
else:
    st.info("Upload a resume and enter a job role to begin.")