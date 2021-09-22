import streamlit as st
from PIL import Image
from pathlib import Path


intro = f"""
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ac lacus sed ligula scelerisque condimentum at eget libero. Morbi bibendum, tortor ac hendrerit ultricies, urna neque blandit nulla, at rhoncus lacus sapien in sapien. Suspendisse eu dui non lorem consectetur mattis. Suspendisse rhoncus risus et dolor consectetur pharetra. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed convallis est ac lectus convallis finibus. Phasellus at convallis diam. Proin tempor malesuada urna in posuere. Nam id dolor auctor, hendrerit libero nec, tempus ligula. Sed est metus, efficitur eget gravida id, maximus in mi. Duis sit amet lectus ut libero laoreet sagittis euismod faucibus sem. Etiam eleifend magna ut enim semper, id gravida nulla condimentum. Vivamus vulputate lectus ac leo bibendum, non tincidunt est pharetra. 
                """

release_notes = f"""
---
**Páginas**
- 🧠 Selecione uma das páginas do site para compreender mais sobre o projeto
- Na página Modelo você poderá realizar a classificação de um arquivo EEG, alguns arquivos já estão disponíveis para os testes\n
**O código do projeto**
- 🪄 O código do modelo de classificação ainda não está disponível, desta forma este projeto está conectado ao modelo já treinado. Isso ocorre pois ainda estamos em fase de desenvolvimento
desta aplicação. Caso deseje saber mais, entre em contato pelo email: clarissalloures@gmail.com\n
**Outras Considerações**
- É possível acessar o vídeo apresentado sobre este projeto no Youtube! ([#Acesse o link](https://github.com/streamlit/streamlit/pull/3467))
"""


def app():

    image = Image.open('Images/comunidades.png')
    st.image(image)

    header = st.container()

    with header:
        st.write(
            f"""
            # Bem-vinda(o) ao projeto de análise de CNPJ! Projeto desenvolvido no Hackathon da A3Data!👋
            """
        )
        st.write(intro)

        st.write(release_notes)
