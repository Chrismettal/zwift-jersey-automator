import pyautogui
import time
from .data.codes import ZWIFT_JERSEY_CODES

def run_code_entry():
    print("Starting code entry in 5 seconds...")
    print("Please focus your game window.")
    time.sleep(5)
    
    for code in ZWIFT_JERSEY_CODES:
        print(f"Attempting code: {code}")
        pyautogui.press('p')
        time.sleep(0.250)  # Wait 250ms
        pyautogui.write(code)
        pyautogui.press('enter')
        print(f"Code {code} entered. Waiting 10 seconds before next attempt...")
        time.sleep(10)
    
    print("All codes have been processed. Exiting.")

if __name__ == "__main__":
    run_code_entry()
