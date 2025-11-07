import mining

promport = input("1.mining 2.sell 3.buy")
def main():
    if promport == "1" or promport == "mining":
        mining.mining()