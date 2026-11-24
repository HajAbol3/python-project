# width and height


width = int(input("Enter with: "))
height = int(input("Enter height: "))

for row in range(height):
    if row == 0 or row == height - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")



# Click to end


import time
from pynput import keyboard

running = True

def on_press(key):
    global running
    running = False
    return False

listener = keyboard.Listener(on_press=on_press)
listener.start()

counter = 0
print("Press any key to end the program...")

while running:
    counter += 1
    print(f"the project is running. counter: {counter}")
    time.sleep(1)

print("Running Program finished")