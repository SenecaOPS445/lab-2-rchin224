#!/usr/bin/env python3
#Author: Roye
#Author ID: 175210236
#Date Created: 2024/01/15

import sys

# Assign default timer value
if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
