from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")

if not api_key:
    print("api key not found")
    exit(1)

chatbot=Groq(api_key=api_key)

while True:

    user_query=input("enter your query(or to quit type 'exit'):  ")

    if user_query.lower()== 'exit':
        print("exiting the program")
        break

    chat_completion=chatbot.chat.completions.create(
        messages=[{"role":"user" , "content":user_query}] ,
        model="gemma2-9b-it" ,
    )

    print("response:",chat_completion.choices[0].message.content)

