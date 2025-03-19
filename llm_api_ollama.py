from ollama import chat
from ollama import ChatResponse
from fastapi import FastAPI, Request, HTTPException
from typing import Union

from pydantic import BaseModel

# 1.setup ollama
# 2.ollama server on cmd
# 3.go to web ollama select some model for your server
# 4.get command to get model set up to cmd
# 5.ollama list to check model have on server
# 6.use this python code to run with fastapi dev name_file.py

#อย่าลืมดูว่า model ที่ใช้หนักขนาดไหน ไม่ใช่ทุกโมเดลที่ คอมธรรมดาจะรันไหว

app = FastAPI()

class Ask(BaseModel):
    question: str = ""
    
   
# request:Request
@app.post("/ask")
async def ask_question(Ask:Ask):
    

   

    response: ChatResponse = chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': Ask.question,
    },
    ])
    print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
    return response.message.content



# from ollama import Client
# client = Client(
#   host='http://localhost:11434',
#   headers={'x-some-header': 'some-value'}
# )
# response = client.chat(model='llama3.2', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   },
# ])