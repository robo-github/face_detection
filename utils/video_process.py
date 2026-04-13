import os
import cv2

import datetime
import threading
import queue

def extract_frames(video_path):
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')   # Initialize the face detector

    output_folder = 'frames'
    os.makedirs(output_folder, exist_ok=True)

    video_capture = cv2.VideoCapture(video_path) # Load the video

    fps = video_capture.get(cv2.CAP_PROP_FPS)   # Frame rate of the video

    frame_interval = int(round(fps)) # Adjust this value to process frames more frequently

    frame_count = 0
   
    last_saved_second = None # Variable to track the last saved frame's timestamp

    frames_queue = queue.Queue()      # Queue for storing frames with faces

    def process_frames(): # Function to process frames and detect faces
        nonlocal last_saved_second # Use nonlocal to access the variable outside the function
        while True:
            frame_data = frames_queue.get()
            if frame_data is None:
                break   

            frame, frame_count = frame_data

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert frame to grayscale for face detection

            faces = detector.detectMultiScale(gray, 1.1, 4) # Detect faces in the frame using cv2
           
            current_second = frame_count / fps  # Calculate the current second

            # Save the frame if a face is detected and its timestamp is different from the last saved one
            # Additionally, if a face is detected, save the frame more frequently
            if len(faces) > 0 and (current_second != last_saved_second or len(faces) > 0):
                current_time = datetime.timedelta(seconds=current_second)
                time_str = str(current_time).replace(':', '.')

                frame_filename = os.path.join(output_folder, f'{time_str}.jpg')
                cv2.imwrite(frame_filename, frame)

                last_saved_second = current_second # Update the last saved frame's timestamp

    # Start a thread for processing frames
    processing_thread = threading.Thread(target=process_frames)
    processing_thread.start()

    # Read and process frames in the main thread
    while True:
        # Read frame
        success, frame = video_capture.read()
        if not success:
            break

        frame_count += 1

        # Check if it's time to extract a frame
        if frame_count % frame_interval == 0:
            # Put frame data into the queue
            frames_queue.put((frame, frame_count))

    # Wait for all frames to be processed
    frames_queue.put(None)
    processing_thread.join()

    video_capture.release() # Release the video capture object


