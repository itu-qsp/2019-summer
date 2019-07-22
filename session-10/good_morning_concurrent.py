import sys
import platform
import threading
import subprocess
from time import sleep


def say_something(msg, speak=True):
    if speak:
        cmd = f"""osascript -e 'say "{msg}"'"""
        subprocess.run(cmd, shell=True)
    else:
        for letter in msg:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(0.1)
        print()  # Finish with a newline


speak = False  # platform.system() == 'Darwin'
msg1 = 'Good morning! I am just telling you a very very long story!'
msg2 = 'Argh, I forgot, I wanted to tell you an even longer story!'


background_thread1 = threading.Thread(target=say_something, args=[msg1, speak])
background_thread1.start()
background_thread2 = threading.Thread(target=say_something, args=[msg2, speak])
background_thread2.start()
