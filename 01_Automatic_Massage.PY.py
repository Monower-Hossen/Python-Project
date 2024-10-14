import pyautogui
import time

# Start the infinite loop
while True:
    # Wait for 4 seconds before typing
    time.sleep(4)

    # Type the given message
    pyautogui.typewrite("I love you!")

    # Wait for 2 seconds before pressing "Enter"
    time.sleep(2)  # Uncomment this line if you want to add a delay

    # Simulate pressing the "Enter" key
    pyautogui.press("enter")
