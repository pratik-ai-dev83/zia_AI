import os
from openai import OpenAI
from dotenv import load_dotenv
 
load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
def analyze_code(user_code, error_message=None):
    
    if not user_code.strip():
        return"No code provided"
    
    prompt = f""" 
    your are an expert programmmer and debugger.
    
    your task:
    1. Find bugs in the code
    2. Fix them
    3. Explain insimple words (like taeching a beginner)
    
    code:
    {user_code}
    """
    
    if error_message:
        prompt += f"\n{error_message}"
        
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Somting is wrong: {str(e)}"
    
    print("error message")
    