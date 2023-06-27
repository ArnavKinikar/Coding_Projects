import random
import string
import time

ar = ['', '', '', '', '', ' ', '', '', '', '', '']
a = ''

while True:
    while ar[0] != 'H':
        ar[0] = random.choice(string.ascii_uppercase)
        time.sleep(.05)
        print(*ar)

    while ar[1] != 'E':
        ar[1] = random.choice(string.ascii_uppercase)
        time.sleep(.05)
        print(*ar)

    for i in [2, 3]:
        while ar[i] != 'L':
            ar[i] = random.choice(string.ascii_uppercase)
            time.sleep(.05)
            print(*ar)

    while ar[4] != 'O':
        ar[4] = random.choice(string.ascii_uppercase)
        time.sleep(.05)
        print(*ar)

    while ar[6] != 'W':
        ar[6] = random.choice(string.ascii_uppercase)
        time.sleep(.05)
        print(*ar)

    while ar[7] != 'O':
        ar[7] = random.choice(string.ascii_uppercase)
        time.sleep(.05)
        print(*ar)

    while ar[8] != 'R':
        ar[8] = random.choice(string.ascii_uppercase)
        time.sleep(.05)
        print(*ar)

    while ar[9] != 'L':
        ar[9] = random.choice(string.ascii_uppercase)
        time.sleep(.05)
        print(*ar)

    while ar[10] != 'D':
        ar[10] = random.choice(string.ascii_uppercase)
        time.sleep(.05)
        print(*ar)

    time.sleep(1)
    print("\n\n", *ar)
    break
