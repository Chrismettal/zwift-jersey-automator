# Zwift Jersey Automator <!-- omit in toc -->

[![License: GPLv3](https://img.shields.io/badge/license-GPLv3-red?style=flat-square)](https://www.gnu.org/licenses/gpl-3.0.html)
[![Donations: Coffee](https://img.shields.io/badge/donations-Coffee-brown?style=flat-square)](https://github.com/Chrismettal#donations)

A Python script that automates the entry of Zwift jersey promo codes using simulated keyboard input.

**If you like my work please consider [supporting me](https://github.com/Chrismettal#donations)!**

## Table of contents <!-- omit in toc -->

- [Concept](#concept)
  - [Overview](#overview)
  - [How It Works](#how-it-works)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Donations](#donations)
- [License](#license)

## Concept

### Overview

Entering dozens of promo codes in Zwift one by one can be tedious. This script iterates through a curated list of known Zwift kit unlock codes, simulating the keyboard presses required to enter them quickly and efficiently.

### How It Works

The script follows this automated loop for each code:
1. Presses `p` to open the promo code prompt.
2. Waits for 250ms.
3. Types the promo code.
4. Presses `Enter`.
5. Waits for 5 seconds before moving to the next code.

**Note:** When you start the script, there is an initial 5-second delay to allow you to focus the Zwift game window.

## Setup

### Prerequisites

- **Python 3.x**
- **pyautogui**: Used for keyboard simulation.
- **A windowed version of Zwift** (running on PC or Mac) to receive the simulated input.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Chrismettal/zwift-jersey-automator.git
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

### Usage

1. Make sure Zwift is running and you are logged in.
2. Run the script:
   ```bash
   python -m zwift_jersey_automator
   ```
3. **Immediately switch focus to your Zwift window.** You have 5 seconds to do this.
4. Sit back and watch as the codes are entered!

## Donations

**If you like my work please consider [supporting me](https://github.com/Chrismettal#donations)!**

## License

<a rel="GPLlicense" href="https://www.gnu.org/licenses/gpl-3.0.html"><img alt="GPLv3" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under the <a rel="GPLlicense" href="https://www.gnu.org/licenses/gpl-3.0.html">GNU GPLv3 License</a>.
