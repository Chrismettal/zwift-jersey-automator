import pyautogui
import time

# Zwift Jersey Promo Codes
ZWIFT_JERSEY_CODES = [
    "ATOC2015",
    "BICYCLINGMAG",
    "BIKERADAR",
    "BIKEANDBEER",
    "CANBERRACCKIT",
    "CRCANYC",
    "DOCOMO",
    "GOALIENWARE",
    "GEARPATROL",
    "GEELONGCCKIT",
    "GOLONGRIDERS",
    "GOLDCOAST",
    "GOAMGENTOC",
    "GOBATTENKILL",
    "GOCIS",
    "GOCYCLEOPS",
    "GOELITE",
    "GOFREESPEED",
    "GOGCN",
    "GOPEARSON",
    "GOVISION",
    "GOSKRYE",
    "GOWBR",
    "GOWSR",
    "GOUSMES",
    "HIKKIT32616",
    "JENSIE",
    "LAFUGA.CC",
    "LAVA",
    "MDCCKIT",
    "MGCCKit",
    "MTSKIT",
    "NCCMAKIT",
    "PCGKIT32516",
    "RADAVIST",
    "RIDEAUSTRALIA",
    "RIDEPOWERTAP",
    "RIDEQUARQ",
    "ROAD.CC",
    "SIGMASPORT",
    "SLOWTWITCH",
    "SOIGNEURDK",
    "STKILDA2015KIT",
    "SYDNEYCCKIT",
    "GOTACX",
    "TDP2015",
    "GOTRAINSHARP",
    "TRIATHLETEMAG",
    "TSBIKES",
    "VCGHKIT",
    "WAHOOFITNESS",
    "ZTHKIT",
    "GOINGAMBA"
]

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
