from secret_key import mytestkey
import openai

openai.api_key = mytestkey

response_message = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "user", "content": "What is the purpose of education?"}
    ])


print(response_message["choices"][0]["message"]["content"])
