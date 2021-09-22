import streamlit as st
from PIL import Image
from pathlib import Path


o_dataset = f"""
                # O Conjunto de Dados

                Cras et velit vestibulum, elementum metus sit amet, cursus enim. In id elit aliquet, finibus odio et, commodo dolor. Vestibulum posuere ante nisi, ut tempor urna ultricies vitae. Aliquam sed tincidunt nisl. Curabitur tincidunt sollicitudin eleifend. Aenean tempus vitae sapien vel vestibulum. Donec fringilla ac erat quis accumsan. Vivamus maximus est vel nisl mattis, vel sollicitudin urna maximus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In euismod sed justo at aliquet. Cras congue dictum massa aliquet dignissim. Duis sagittis orci ac leo semper egestas. Quisque pulvinar semper odio in facilisis. Praesent erat sem, ultricies eu lobortis sit amet, accumsan quis tortor. Duis eget lacus urna.
                """


#st.write("The TUEP dataset is a subset of TUEG (The TUH EEG Epilepsy Corpus) that contains 100 subjects epilepsy and 100 subjects without epilepsy, as determined by a certified neurologist. The data was developed in collaboration with a number of partners including NIH. .")


def app():

    header = st.container()

    with header:
        st.write(o_dataset)
