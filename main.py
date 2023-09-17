import platform
import pwd
import os
from cols import *

username = pwd.getpwuid(os.getuid()).pw_name
system = platform.system()
computer_name = "Unknown"
with open('/etc/hostname', 'r') as file:
    computer_name = file.readline().strip()

if system != "Linux":
    print(f"Unsupported system: {system}")

while True:
    user_input = input(f"{bold+red+username+reset+magenta}@{reset+bold+green+computer_name+reset} ~> ")