import streamlit as st
import base64
from pages.page2 import page2
from pages.page3 import page3


def page1():
    
    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"][aria-expanded="true"]{
                display: none;
            }
            header.stHeader {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    hide_st_style = """
        <style>
        #MainMenu {visibility : hidden;}
        footer {visibility : hidden;}
        header {visibility : hidden;}
        </style>
        """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    video_file_path = "utils/faces.mp4"

    
    with open(video_file_path, "rb") as video_file:  # Read the video file in binary mode
        video_bytes = video_file.read()

   
    video_base64 = base64.b64encode(video_bytes).decode('utf-8')   # Encode the video file to Base64

    
    st.markdown(f"""
    <video autoplay muted loop id="myVideo" style="position:fixed; right:0; bottom:0; min-width:100%; min-height:100%;">
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4"> 
    </video>
    """, unsafe_allow_html=True)   # Embed the video using a data URL

   
    st.markdown("<h1 style='text-align: center; color: white;'>Face Detector</h1>", unsafe_allow_html=True)

   
    st.markdown("<br>", unsafe_allow_html=True) 
    st.markdown("<style> .stButton>button {margin-top: 70px;margin-left : 290px;}</style>", unsafe_allow_html=True) 

    if st.button("Get Started"): 
        st.session_state['page'] = 'page2'



def main():
   
    page = st.session_state.get('page', 'page1')
    
    if page == 'page1':
        page1()
    elif page == 'page2':
        page2()
    elif page == 'page3':
        page3()

if __name__ == "__main__":
    main()
