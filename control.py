import requests
import keyboard  # Install with: pip install keyboard
import time

# Set the IP address of your ESP32
ESP32_IP = "http://192.168.2.222"  # Update this with your actual ESP32 IP

# Track last command to avoid repeated requests
last_command = None

def send_command(direction):
    global last_command
    if direction != last_command:  # Avoid redundant API calls
        try:
            response = requests.get(f"{ESP32_IP}/move?dir={direction}", timeout=2)
            if response.status_code == 200:
                print(f"Command sent: {direction}")
            else:
                print(f"Failed to send command ({response.status_code}): {response.text}")
            last_command = direction
        except requests.exceptions.RequestException as e:
            print(f"Error sending command: {e}")

def main():
    print("Control the car using the following keys:")
    print("W - Forward | A - Left | S - Backward | D - Right | X - Stop")
    print("Press ESC to exit.")

    while True:
        try:
            if keyboard.is_pressed('w'):
                send_command("forward")
            elif keyboard.is_pressed('a'):
                send_command("left")
            elif keyboard.is_pressed('s'):
                send_command("backward")
            elif keyboard.is_pressed('d'):
                send_command("right")
            elif keyboard.is_pressed('x'):
                send_command("stop")
            elif keyboard.is_pressed('esc'):
                send_command("stop")  # Ensure car stops before exit
                print("Exiting...")
                break
            else:
                last_command = None  # Reset if no key is pressed

            time.sleep(0.1)  # Delay to prevent spamming requests

        except KeyboardInterrupt:
            send_command("stop")
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
