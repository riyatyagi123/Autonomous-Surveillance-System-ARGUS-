# import ollama
# import os
# import requests
# import time
# import get_images

# def get_latest_image(save_dir):
#     """Finds the latest image based on the highest numbered filename."""
#     images = [f for f in os.listdir(save_dir) if f.endswith(".jpg")]
#     if not images:
#         return None
#     latest_image = max(images, key=lambda x: int(os.path.splitext(x)[0]))
#     return os.path.join(save_dir, latest_image)

# # ESP32 Camera & Control Settings
# ESP32_IP = "http://192.168.2.222"  # Update this with your actual ESP32 IP
# CAMERA_URL = f"{ESP32_IP}/camera"
# SAVE_DIRECTORY = r"C:\Users\araj8\Downloads\llm_images"

# # Track last command to avoid redundant API calls
# last_command = None

# def send_command(direction):
#     global last_command
#     if direction != last_command:  # Avoid redundant API calls
#         try:
#             response = requests.get(f"{ESP32_IP}/move?dir={direction}", timeout=2)
#             if response.status_code == 200:
#                 print(f"Command sent: {direction}")
#             else:
#                 print(f"Failed to send command ({response.status_code}): {response.text}")
#             last_command = direction
#         except requests.exceptions.RequestException as e:
#             print(f"Error sending command: {e}")

# def chat_with_llava(prompt, image_path):
#     if os.path.exists(image_path):
#         response = ollama.chat(model="LLaVA", messages=[{
#             "role": "user",
#             "content": prompt,
#             "images": [image_path]
#         }])
#     else:
#         response = ollama.chat(model="LLaVA", messages=[{
#             "role": "user",
#             "content": prompt
#         }])
#     return response.message["content"]

# def process_image_and_drive():
#     count = 1
#     while True:
#         # Fetch a single image and save it
#         image_path = os.path.join(SAVE_DIRECTORY, f"{count}.jpg")
#         try:
#             response = requests.get(CAMERA_URL, timeout=5)
#             if response.status_code == 200:
#                 with open(image_path, "wb") as file:
#                     file.write(response.content)
#                 print(f"Saved: {image_path}")
#                 count += 1
#             else:
#                 print(f"Failed to fetch image, status code: {response.status_code}")
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching image: {e}")
            
#         # Process the latest image
#         latest_image = get_latest_image(SAVE_DIRECTORY)
#         if latest_image:
#             prompt = (
#                 "Analyze the image and respond with only one command: move forward, turn left, turn right, stop, or move backward."
#             )
            
#             llava_response = chat_with_llava(prompt, latest_image)
#             print("LLaVA Response:", llava_response)
            
#             # Basic command mapping based on AI response
#             if "move forward" in llava_response.lower():
#                 send_command("forward")
#             elif "turn left" in llava_response.lower():
#                 send_command("left")
#             elif "turn right" in llava_response.lower():
#                 send_command("right")
#             elif "stop" in llava_response.lower():
#                 send_command("stop")
#             elif "move backward" in llava_response.lower():
#                 send_command("backward")
#             elif "obstacle ahead" in llava_response.lower():
#                 send_command("stop")  # Stop to prevent collision
#                 time.sleep(1)
#                 send_command("right")  # Try turning right as an alternative
        
#         time.sleep(1)  # Small delay before capturing next image

# if __name__ == "__main__":
#     print("Starting autonomous RC car control... Avoiding obstacles and exploring!")
#     process_image_and_drive()


import ollama
import os
import requests
import time
import threading

# ESP32 Camera & Control Settings
ESP32_IP = "http://192.168.2.222"
CAMERA_URL = f"{ESP32_IP}/camera"
MOVE_URL = f"{ESP32_IP}/move?dir="
SAVE_DIRECTORY = r"C:\Users\araj8\Downloads\llm_images"
IMAGE_PATH = os.path.join(SAVE_DIRECTORY, "latest.jpg")

# Persistent session for faster API calls
session = requests.Session()

# Shared variable for latest command
current_command = "stop"
command_lock = threading.Lock()
turning = False  # Flag to prevent continuous turning

def send_command():
    """Continuously sends forward/backward commands but turns only once."""
    global current_command, turning
    while True:
        with command_lock:
            command = current_command
        
        # Only repeat forward/backward commands
        if command in ["forward", "backward"]:
            try:
                response = session.get(f"{MOVE_URL}{command}", timeout=2)
                if response.status_code == 200:
                    print(f"Executing: {command}")
                else:
                    print(f"Failed to execute command ({response.status_code}): {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"Error executing command: {e}")
            time.sleep(3)  # Keep sending forward/backward commands
        
        # For turning, send once and stop
        elif command in ["left", "right"] and not turning:
            turning = True  # Prevent continuous turning
            try:
                response = session.get(f"{MOVE_URL}{command}", timeout=2)
                if response.status_code == 200:
                    print(f"Executing: {command}")
                else:
                    print(f"Failed to execute turn ({response.status_code}): {response.text}")
            except requests.exceptions.RequestException as e:
                print(f"Error executing turn: {e}")
            time.sleep(1)  # Allow turn to complete
            with command_lock:
                current_command = "stop"  # Stop after turning
            turning = False  # Reset flag
        
        else:
            time.sleep(0.1)  # Small delay to check for new command

def chat_with_llava(prompt, image_path):
    """Sends the image and prompt to LLaVA for command generation."""
    if os.path.exists(image_path):
        response = ollama.chat(model="LLaVA", messages=[{
            "role": "user",
            "content": prompt,
            "images": [image_path]
        }])
    else:
        response = ollama.chat(model="LLaVA", messages=[{
            "role": "user",
            "content": prompt
        }])
    return response.message["content"]

def fetch_image():
    """Fetches an image from the ESP32-CAM and saves it as 'latest.jpg'."""
    try:
        response = session.get(CAMERA_URL, timeout=2)
        if response.status_code == 200:
            with open(IMAGE_PATH, "wb") as file:
                file.write(response.content)
            print("Image updated.")
        else:
            print(f"Failed to fetch image, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")

def process_image_and_update_command():
    """Processes image and updates movement command."""
    global current_command
    while True:
        fetch_image()  # Get latest image

        prompt = (
    "Analyze the image and respond with exactly one of the following commands: "
    "'move forward', 'turn left', 'turn right', 'stop', or 'move backward'. "
    "Do not say anything else. Respond with only the command."
)

        llava_response = chat_with_llava(prompt, IMAGE_PATH)
        print("LLaVA Response:", llava_response)

        new_command = "stop"  # Default to stop

        # Decision mapping based on AI response
        if "move forward" in llava_response.lower():
            new_command = "forward"
        elif "turn left" in llava_response.lower():
            new_command = "left"
        elif "turn right" in llava_response.lower():
            new_command = "right"
        elif "stop" in llava_response.lower():
            new_command = "stop"
        elif "move backward" in llava_response.lower():
            new_command = "backward"
        elif "obstacle ahead" in llava_response.lower():
            new_command = "stop"
            time.sleep(0.5)
            new_command = "right"  # Try turning right

        # Update command safely
        with command_lock:
            current_command = new_command

        time.sleep(0.5)  # Process image every 0.5 seconds

if __name__ == "__main__":
    print("Starting continuous autonomous RC car control!")

    # Start movement thread (keeps executing last command)
    movement_thread = threading.Thread(target=send_command)
    movement_thread.daemon = True
    movement_thread.start()

    # Start image processing thread
    process_image_and_update_command()
