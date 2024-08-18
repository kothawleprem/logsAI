import requests

AI_API_URL = os.getenv('AI_API_URL', 'https://api.example.com/analyze')
AI_API_KEY = os.getenv('AI_API_KEY', 'your_api_key')

# def analyze_log(content):
    # headers = {'Authorization': f'Bearer {Config.AI_API_KEY}'}
    # response = requests.post(Config.AI_API_URL, json={"logfile": content}, headers=headers)
    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     return {"error": "AI service failed"}