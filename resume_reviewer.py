import os 
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# for m in genai.list_models():
#     print(m.name)

model = genai.GenerativeModel("gemini-2.5-flash")

def load_prompt():
    with open("prompt/reviewer_prompt.txt", "r", encoding="utf-8") as file:
        return file.read()
    
def review_resume(resume_text, job_role):
    base_prompt = load_prompt()
    final_prompt = base_prompt.replace("{{RESUME_TEXT}}", resume_text)
    final_prompt = base_prompt.replace("{{JOB_ROLE}}", job_role)

    response = model.generate_content(final_prompt)
    return response.text
