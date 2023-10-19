import os
import requests
 
MODEL = ''
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"
API_TOKEN = os.environ.get('huggingface')
 
headers = {"Authorization": f"Bearer {API_TOKEN}"}
data = {"inputs": "your_input_text_here"}
 
response = requests.post(API_URL, headers=headers, json=data)
 
if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")