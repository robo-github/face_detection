import streamlit as st
import os
import base64
from utils.video_process import extract_frames
from utils.check import has_face
from utils.detect import detector
import time






def page2():
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

    st.title("Upload Video and Image")
    
  
    upload_dir = 'uploads'     # Define the upload directory
    
   
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir, exist_ok=True)     # Ensure the upload directory exists

    video_uploaded = False
    image_uploaded = False
    detection_completed = False
    
    # Video upload


    video_file = st.file_uploader("Upload Video", type=["mp4", "avi"])
    if video_file is not None:
       
        video_path = os.path.join(upload_dir, video_file.name)    # Save video file to upload folder
        with open(video_path, "wb") as f:
            f.write(video_file.getbuffer())
        
       
        video_content = video_file.read()
        video_base64 = base64.b64encode(video_content).decode('utf-8')   # Encode video file to base64
        
       
        video_html = f"""
            <video width="640" height="480" controls>
                <source src="data:video/{video_file.type};base64,{video_base64}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        """
        st.markdown(video_html, unsafe_allow_html=True)
        
        print("Video saved to:", video_path)
        extract_frames(video_path)
        video_uploaded = True
        
    
    # Image upload


    image_file = st.file_uploader("Upload Image", type=["jpg", "png"])
    if image_file is not None:
        # Save image file to upload folder
        image_path = os.path.join(upload_dir, image_file.name)
        with open(image_path, "wb") as f:
            f.write(image_file.getbuffer())
        st.image(image_path, width=320)  
        has_face_result = has_face(image_path)
        image_uploaded = True
        if has_face_result:
            print("Face detected in the image.")
        else:
            print("No face detected in the image.")
            # Delete the image if no face is detected
            os.remove(image_path)
            print("Image deleted:", image_path)
    
    
        st.markdown("<div style='text-align:center;'><br><br></div>", unsafe_allow_html=True)
        st.markdown("<style> .stButton>button {margin-top: 70px;margin-left: 300px;}</style>", unsafe_allow_html=True) 
    
        # Check if the "Detect" button is clicked
        if video_uploaded and image_uploaded and not detection_completed:
            if st.button("Detect"):   
                progress_text = "Smile while we detect ...."
                st.info(progress_text, icon="ℹ️")
                start_time = time.time()
                
                # Ensure the frames are extracted before calling the detector
                if video_file is not None:
                    # Assuming extract_frames function saves frames in a 'frames' folder
                    frames_folder_path = os.path.join('frames')
                    print(f"Checking for frames folder at: {frames_folder_path}")
                    if os.path.exists(frames_folder_path):
                        print("Frames folder exists.")
                        similar_images = detector(image_path)
                        st.session_state['similar_images'] = similar_images
                        detection_completed = True
                        
                        
                        elapsed_time = time.time() - start_time
                        time.sleep(2)
                        
                        # Redirect to page 3 after detection is completed
                        st.session_state['page'] = 'page3'
                        st.rerun()
                    else:
                        st.error("Please upload a video first to extract frames.")
                else:
                    st.error("Please upload an image first.")
