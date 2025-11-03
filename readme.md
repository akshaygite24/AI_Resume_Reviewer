
# AI Resume Reviewer

## Features
- Upload or paste any resume text
- Specify the job role you're applying for
- AI gives detailed analysis:
    - Strengths relevant to the role.
    - Weaknesses or missing skills.
    - Specific actionable improvements
    - Overall impression and readiness
    - Resume-fit score (1-10)
- Uses Gemini 2.5 Flash model via Google Generative AI
- Runs locally using Streamlit

## Tech Stack
Component|Technology
---------|----------
Frontent|Streamlit
Backend|Python
AI Model|Google Gemini 2.5 Flash
Environment Management|python-dotenv
File Processing|PyPDF2
Version Control|Git & GitHub

## Project Structure
```
AI_Resume_Reviewer/
│
├── app.py                     
├── reviewer.py                
├── prompt/
│   └── reviewer_prompt.txt    
├── resumes/                   
│   ├── Data_Analyst_Sample_Resume.pdf
│   ├── Data_Scientist_Sample_Resume.pdf
│   ├── Full_Stack_Developer_Sample_Resume.pdf
│   └── ML_Sample_Resume.pdf
├── .env              
├── requirements.txt
└── README.md
```

## Setup Instruction
### 1. Clone the repository
```
git clone https://github.com/akshaygite24/AI_Resume_Reviewer.git

cd AI_Resume_Reviewer
```

### 2. Create a virtual environment
```
python -m venv env

env\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Set up your API key
```
Create a .env file in the project root:

GEMINI_API_KEY=your_google_gemini_api_key
```
### 5. Run the app
```
streamlit run app.py
```

## Example Usage
1. Upload your Resume Text
2. Enter the job role (eg. Data Analyst)
3. Click Analyze Resume
4. Get AI-Generated insights

## Prompt Used

```
You are an experienced career consultant and resume optimization expert.

Review the following resume for a candidate applying for the role of: {{JOB_ROLE}}.

IMPORTANT INSTRUCTIONS:
- Do NOT assume, infer, or add any details that are not explicitly mentioned in the resume.
- If some information is missing (e.g., skills, experience, education), clearly state that it is "Not mentioned".
- Base your entire analysis only on the content provided in the resume text.

Provide a detailed, professional analysis including:
1. Strengths relevant to the {{JOB_ROLE}} position.
2. Weaknesses or missing skills for that role.
3. Specific, actionable suggestions to improve the resume.
4. Overall impression and readiness for the {{JOB_ROLE}} position.
5. Score (1–10) indicating how well the resume aligns with the {{JOB_ROLE}} role.

Keep the tone encouraging yet professional and factual.

Resume Text:
{{RESUME_TEXT}}

```


## Author
**Akshay Gite** </br>
Data Science & AI Enthusiast
