# fb_cloner.py
import random

print("=== Fake FB ID Cloner ===\n")
print("Input format: 100011223344|john123")
print("Type 'done' when finished.\n")

ids = []
while True:
    entry = input("Enter ID|pass: ")
    if entry.lower() == 'done':
        break
    if '|' in entry:
        ids.append(entry)
    else:
        print("Invalid format. Use ID|pass")

results = []
for data in ids:
    fb_id, fb_pass = data.strip().split('|')
    status = random.choice(["Success", "Error", "Try Again", "Already Cloned"])
    if status == "Success":
        result = f"Cloning ID: {fb_id} => Success\nLogin: {fb_id} | {fb_pass}\n"
        results.append(result)
    else:
        print(f"Cloning ID: {fb_id} => {status}")

# Save successful clones
if results:
    with open("cloned_success.txt", "w") as f:
        for r in results:
            f.write(r + "\n")
    print("\nSuccessful clones saved to cloned_success.txt")
else:
    print("\nNo successful clones.")
