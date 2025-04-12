import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_fields(text, template="default"):
    prompt = f"Extract fields from this invoice using template: {template}\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return eval(response['choices'][0]['message']['content'])
