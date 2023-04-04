import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

question = input("Digite sua pergunta: ")

if question == '': 
    question = "O que e grafeno?" # pergunta padrão
    print(question)
    
try:
    answer = openai.Completion.create(
                              model="text-davinci-003",
                              prompt=question,
                              max_tokens=2000,
                              temperature=0
                                )
except BaseException as exception:
    print(f"Exception Name: {type(exception).__name__}")
    print(f"Exception Desc: {exception}")

print("Resposta: ")
print(answer.choices[0].text.strip())