import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title = "Multipage App")

# page_bg_img = '''
# <style>
# body {
# background-image: url("https://images.wallpapersden.com/image/download/abstract-wave-hd-blue_bWZnbm6UmZqaraWkpJRoaWprrWdnaGk.jpg");
# background-size: cover;
# }
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('Deep Learning Opacity Web Service')
#st.sidebar.success("Select a page above.")

st.markdown("""
    ## ¿Qué es DLO?
    Somos una plataforma Web que predice la probabiliad de Opacidad Pulmonar en una Radiografía de Pecho, apoyando al diagnóstico de los médicos radiólogos
""")
