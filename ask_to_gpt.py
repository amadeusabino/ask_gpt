import os
import openai

def alinhar_texto(texto, largura_coluna):
    """Função para alinhar o texto de acordo com o limite de colunas especificado"""
    
    # Dividir o texto em palavras
    palavras = texto.split()
    
    # Inicializar a linha atual e a lista de linhas
    linha_atual = ''
    linhas = []
    
    # Percorrer todas as palavras
    for palavra in palavras:
        
        # Se a palavra cabe na linha atual, adicioná-la
        if len(linha_atual + ' ' + palavra) <= largura_coluna:
            if linha_atual == '':
                linha_atual = palavra
            else:
                linha_atual += ' ' + palavra
        # Senão, adicionar a linha atual à lista de linhas e começar uma nova linha
        else:
            linhas.append(linha_atual)
            linha_atual = palavra
    
    # Adicionar a última linha à lista de linhas
    if linha_atual != '':
        linhas.append(linha_atual)
    
    # Juntar as linhas em uma única string separada por quebras de linha
    texto_alinhado = '\n'.join(linhas)
    
    # Retornar o texto alinhado
    return texto_alinhado


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

r = alinhar_texto(answer.choices[0].text.strip(), 60)

print(r)