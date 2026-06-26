import requests
import time
import os

def fetch_images(url, save_dir, interval=2):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    count = 1
    while True:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                file_path = os.path.join(save_dir, f"{count}.jpg")
                with open(file_path, "wb") as file:
                    file.write(response.content)
                print(f"Saved: {file_path}")
                count += 1
            else:
                print(f"Failed to fetch image, status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching image: {e}")
        
        time.sleep(interval)

# Change this to your correct save path
# save_directory = r"C:\Users\araj8\Downloads\llm_images"
# camera_url = "http://192.168.2.222/camera"

# fetch_images(camera_url, save_directory)
