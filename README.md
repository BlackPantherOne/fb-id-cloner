# FB ID Cloner (Fake Simulator)

This is a **Python-based Facebook ID Cloning Simulator** for educational or entertainment purposes only. It simulates the cloning of FB accounts with random success or failure.

## Features
- Input manual ID and password in format `ID|pass`
- Simulates random clone result (Success, Error, Already Cloned, etc.)
- Saves successful "clones" in `cloned_success.txt`
- 100% offline, no real FB interaction

## Installation (Termux or Linux)
```bash
pkg install python -y
git clone https://github.com/YOURUSERNAME/fb-id-cloner.git
cd fb-id-cloner
python fb_cloner.py
