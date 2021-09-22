import streamlit as st
from multiapp import MultiApp
# import your app modules here
from apps import home, nosso_dataset, model, dataanalisy


st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox(
    'Selecione uma página', ['Página Inicial', 'Visualização dos Dados', 'Descrição do Projeto', 'Sobre o Time'])


if(paginaSelecionada == 'Página Inicial'):
    home.app()

elif(paginaSelecionada == 'Visualização dos Dados'):
    dataanalisy.app()

elif(paginaSelecionada == 'Descrição do Projeto'):
    nosso_dataset.app()

elif(paginaSelecionada == 'Sobre o Time'):
    model.app()
