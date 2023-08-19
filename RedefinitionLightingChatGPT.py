import openai
openai.api_key = 'Your_Secret_Key'

messages = [ {"role": "system", "content": 
              "I am your Smart Home Lighting Controller"} ]
while True:
    message = input("Question : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
