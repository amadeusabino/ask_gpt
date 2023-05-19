import pytest
import openai, os
from ask_to_gpt import alinhar_texto, initialize_openai

def test_alinhar_texto():
    # Teste com um texto que não precisa de alinhamento
    texto1 = "Este é um texto curto."
    largura_coluna1 = 30
    resultado1 = alinhar_texto(texto1, largura_coluna1)
    assert resultado1 == texto1

    # Teste com um texto que precisa de alinhamento
    texto2 = "Este é um texto longo que precisa ser alinhado em várias linhas."
    largura_coluna2 = 20
    resultado2 = alinhar_texto(texto2, largura_coluna2)
    assert resultado2 == "Este é um texto\nlongo que precisa\nser alinhado em\nvárias linhas."

    # Teste com um texto vazio
    texto3 = ""
    largura_coluna3 = 20
    resultado3 = alinhar_texto(texto3, largura_coluna3)
    assert resultado3 == ""

    # Teste com uma largura de coluna menor do que qualquer palavra do texto
    texto4 = "texto"
    largura_coluna4 = 10
    resultado4 = alinhar_texto(texto4, largura_coluna4)
    assert resultado4 == "texto"

    # Teste com uma única palavra que excede a largura da coluna
    #texto5 = "palavramuitolonga"
    #largura_coluna5 = 20
    #resultado5 = alinhar_texto(texto5, largura_coluna5)
    #assert resultado5 == "palavramui\ntolonga"

# Teste para a função initialize_openai
def test_initialize_openai():
    initialize_openai()
    # Verificar se a chave da API foi definida corretamente
    assert openai.api_key == os.getenv("OPENAI_API_KEY")