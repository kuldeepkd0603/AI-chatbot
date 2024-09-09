'''
author : kuldeep verma
'''
from flask import Flask
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI



load_dotenv()
os.environ['GOOGLE_API_KEY']=os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to hindi. Translate the user sentence.",
    ),
    ("human", "fuck you"),
]
ai_msg = llm.invoke(messages)
ai_msg
print(ai_msg.content)
app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)
    