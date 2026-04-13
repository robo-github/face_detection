from deepface import DeepFace
import os
from datetime import timedelta

def detector(target_image_path):
 
    # Function to extract time from filename and format it
    def format_time_from_filename(filename):
        # Extract the time part from the filename
        parts = filename.split('.')
        # Join the first three parts to get the desired format
        time_str = '.'.join(parts[:3])
        return time_str

    # Initialize a list to store the names of similar images along with their timestamps
    similar_images = []

    # Iterate over each image in the 'frames' folder
    frames_folder_path = "frames"
    for filename in os.listdir(frames_folder_path):
        if filename.endswith(".jpg"): 
            image_path = os.path.join(frames_folder_path, filename)
            
            try:
                # Compare the target image with the current image
                result = DeepFace.verify(target_image_path, image_path, enforce_detection=False)
                
                # If the faces are similar, add the image path and timestamp to the list
                if result["verified"]:
                    formatted_time = format_time_from_filename(filename)
                    similar_images.append((image_path, formatted_time))
            except Exception as e:
                print(f"Error processing {filename}: {e}")

   
    return similar_images
