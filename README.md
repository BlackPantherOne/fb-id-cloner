README.md

FB ID Cloner (Fake Simulator)

This is a Python-based Facebook ID Cloning Simulator for educational or entertainment purposes only. It simulates the cloning of FB accounts with random success or failure.

Features

Input manual ID and password in format ID|pass

Simulates random clone result (Success, Error, Already Cloned, etc.)

Saves successful "clones" in cloned_success.txt

100% offline, no real FB interaction


Installation (Termux or Linux)

pkg install python -y
git clone https://github.com/BlackPantherOne/fb-id-cloner.git
cd fb-id-cloner
python fb_cloner.py

Example Usage

Enter ID|pass: 100011223344|john123
Enter ID|pass: 100011223355|mike456
Enter ID|pass: done

Output:

Cloning ID: 100011223344 => Success
Login: 100011223344 | john123

Cloning ID: 100011223355 => Error

Successful clones saved to cloned_success.txt

Warning

This is not a real cloner — it’s just a fake interface for fun, testing, or training. Do not use it to mislead others or violate terms of service.


---

Author: YOUR NAME GitHub:(https://github.com/BlackPantherOne)]

