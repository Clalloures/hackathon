import streamlit as st
from PIL import Image
from pathlib import Path


o_dataset = f"""
                # Hiienei jajd

                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus risus ex, semper quis ante sed, congue bibendum purus. Morbi accumsan, erat venenatis viverra aliquet, sem elit dictum nisi, sit amet venenatis nibh velit nec quam. Donec sodales viverra purus ac ultricies. Praesent quam justo, venenatis ut finibus at, ullamcorper sed purus. Nullam nulla dui, finibus id est non, ultricies malesuada magna. Nam libero elit, commodo molestie molestie quis, malesuada sed mauris. Nunc et suscipit nibh. Nam vitae odio vel ante aliquam ornare sollicitudin et dui. Praesent consectetur ex id dignissim euismod. Nam finibus neque massa, sit amet ornare tortor egestas in. Pellentesque suscipit, metus quis ornare euismod, diam sapien interdum nulla, euismod elementum odio orci non purus. Proin laoreet, nisi finibus commodo elementum, ipsum ante imperdiet augue, eu feugiat dolor odio elementum lectus. Nunc sodales orci id tincidunt vulputate. Etiam ac interdum velit. Nunc scelerisque, felis non euismod ornare, ligula justo tincidunt massa, sed finibus nisl odio a dui. Suspendisse lectus libero, tincidunt a auctor eu, rutrum ut lorem.
                """


#st.write("The TUEP dataset is a subset of TUEG (The TUH EEG Epilepsy Corpus) that contains 100 subjects epilepsy and 100 subjects without epilepsy, as determined by a certified neurologist. The data was developed in collaboration with a number of partners including NIH. .")


def app():

    header = st.container()

    with header:
        st.write(o_dataset)
