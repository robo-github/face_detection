import os

def delete_folder():
    def delete_files_in_folder(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

    frames_folder = "frames"
    uploads_folder = "uploads"

    delete_files_in_folder(frames_folder)
    delete_files_in_folder(uploads_folder)

    print("Files deleted successfully.")
delete_folder()
