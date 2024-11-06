import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

# Function to send the prompt to the chat completion endpoint
def send_prompt(prompt):
    url = 'https://api.openai.com/v1/chat/completions'  # Updated endpoint
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "gpt-3.5-turbo",  # Updated model to gpt-3.5-turbo
        "messages": [{"role": "user", "content": prompt}],  # Chat model format
        "max_tokens": 100
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("Response:", response.json()['choices'][0]['message']['content'])
    else:
        print("Error:", response.status_code, response.json())

# Test the function with a prompt
prompt = "Make a list of prompts that I can use to generate leads for my holiday sales for my greeting card company."
send_prompt(prompt)
