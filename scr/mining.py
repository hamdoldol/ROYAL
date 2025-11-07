import random
import time

def mining():
    hashs = []
    while True:
        ran1 = random.randrange(1, 1000000)
        ran2 = random.randrange(1, 1000000)
        plus = ran1 + ran2
        goal = random.randrange(1, 2000000)

        if plus == goal:
            print("mining hash! hash is", plus)
            hashs.append(plus)
            print("Mining complete! Hash list:", hashs)
            break  # 해시를 찾았으니 반복 종료

        time.sleep(0.1)  # CPU 점유율 낮추기

    return hashs
