import streamlit as st
from utils.delete import delete_folder




def page3():

    st.markdown(
        """
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
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
    # Retrieve the result from the session state
    similar_images = st.session_state.get('similar_images', [])
    
    # Change title based on whether there are matches or not
    if similar_images:
        st.markdown("<h1 style='text-align: center;'>Detected Faces</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center;'>No Match Found</h1>", unsafe_allow_html=True)
    
    # Check if there are similar images
    if similar_images:
        # Display each image and its timestamp
        for image_path, timestamp in similar_images:
            st.image(image_path, width=240, caption=f"Timestamp: {timestamp}")
    else:
        st.write("Sorry :)")

    col1, col2, col3 , col4, col5 = st.columns(5)

    with col1:
        pass
    with col2:
        pass
    with col4:
        pass
    with col5:
        pass
    with col3:
        st.markdown("<div style='text-align:center;'><br><br></div>", unsafe_allow_html=True)
        if st.button("Detect Again"):
            delete_folder()
            st.session_state['page'] = 'page2'
