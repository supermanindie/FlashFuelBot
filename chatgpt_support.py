# chatgpt_support.py
import openai
openai.api_key = "your_openai_api_key"

def get_support_response(user_question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_question}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return "Error: " + str(e)
