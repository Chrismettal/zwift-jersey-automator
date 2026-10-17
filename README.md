# Zwift Jersey Automator

A Python script that automates the entry of Zwift jersey promo codes using simulated keyboard input.

## Overview

Entering dozens of promo codes in Zwift one by one can be tedious. This script iterates through a curated list of known Zwift kit unlock codes, simulating the keyboard presses required to enter them quickly and efficiently.

## How It Works

The script follows this automated loop for each code:
1. Presses `p` to open the promo code prompt.
2. Waits for 250ms.
3. Types the promo code.
4. Presses `Enter`.
5. Waits for 5 seconds before moving to the next code.

**Note:** When you start the script, there is an initial 5-second delay to allow you to focus the Zwift game window.

## Prerequisites

- **Python 3.x**
- **pyautogui**: Used for keyboard simulation.
- **A windowed version of Zwift** (running on PC or Mac) to receive the simulated input.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/zwift-jersey-automator.git
   cd zwift-jersey-automator
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install pyautogui
   ```

## Usage

1. Make sure Zwift is running and you are logged in.
2. Run the script:
   ```bash
   python src/press_p.py
   ```
3. **Immediately switch focus to your Zwift window.** You have 5 seconds to do this.
4. Sit back and watch as the codes are entered!

## Disclaimer

This script is provided for convenience. Use it at your own risk. We are not responsible for any issues that may arise from using this automation tool within Zwift.

## License

This project is licensed under the [GNU GPLv3 License](LICENSE).
