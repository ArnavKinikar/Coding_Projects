import time


def coutdown(t):
    while t != -1:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\r", timer, end=' ')
        time.sleep(1)
        t -= 1

    print("\n\nTimer finished!")


t = input("Enter time in Seconds: ")

coutdown(int(t))
