# Título
# input do chat (campo de msg)
# A cada msg que user enviar
    # mostar a msg que user envio no chat
    # pegar a perguntar e enviar para uma IA responder
    # exibir a resposta da IA em tela

# escolher as ferramentas
# Framewworks
# Streamlit -> sempre roda o cod todo a cada atualização, apenas com python consigo criar frontend e backend
# Flask -> obgriga estrutura de uma maneira
# Django -> já tem códigos prontos
# FastAPI 


# vamos usar Streamlit
# a IA que vamos usar: OpenAI
# OpenAI, Gemini, Claude

# pip install openai streamlit

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="")

# st.write() escrever
# st.button() botão

st.write("# Chatbot com IA") # markdown, os textos são escritos com esta formatação
st.write("##### Chatbot criado por Ramavamv")

# criar pré-visualização do site para rodar
# streamlit run main.py // arquivo tem que estar salvo para rodar

# cokies no navegador, se a lista não existir a lista é cria vazia
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []
    # st.session_state["lista_mensagens"] = [{"role": "system", "content": ""}]
    # a outra forma é integrar com langchain

texto_usuario = st.chat_input("Digite sua mensagem.")

# para cada msg que tenho dentro da lista de mensagens quero criar um text
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    # A cada msg que user enviar
        # mostar a msg que user envio no chat
        # pegar a perguntar e enviar para uma IA responder
        # exibir a resposta da IA em tela
    st.chat_message("user").write(texto_usuario)
    # este system prompt tu passa informações para ia, o que pode e nção pode fazer etc
    # mensagem_usuario = {"role": "system", "content": texto_usuario}
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    #  posso parra
    # nome
    # user // icone de user
    # assistant //icone do robô

    # ia respondeu

    # cria uma nova mensagem que completa meu modelo ia
    # # passar lista de msgs e modelo
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
        # model="gpt-5.4-mini"
    )

    print(resposta_ia)
    print(resposta_ia.choices[0].message.content)
    texto_tesposta_ia = resposta_ia.choices[0].message.content


    st.chat_message("assistant").write(texto_tesposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_tesposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

# print(st.session_state["lista_mensagens"])

# soudevpython
# pode ser craido um model 
# Hugging Face -> dá para baixar este modelo e treinar
# posso integrar com banco de dados para armazenar a lista de dicionários

