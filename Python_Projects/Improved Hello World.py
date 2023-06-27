import random
import string
import time

ar = ['', '', '', '', '', ' ', '', '', '', '', '']
Completed = ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

for i in range(11):
    while ar[i] != Completed[i]:
        ar[i] = random.choice(string.ascii_uppercase)
        time.sleep(.05)
        print(*ar)

time.sleep(1)
print("\n\n", *ar)
