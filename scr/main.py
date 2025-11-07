import mining
import sell_and_buy

def promport():
    input("1.mining 2.sell 3.buy 4.exit")
def main():
    if promport == "mining":
        hashes = mining.mining()
        promport()
    elif promport == "sell":
        sell_and_buy.sell()
    elif promport == "buy":
        sell_and_buy.buy()
    elif promport == "exit":
        exit('byebye')
if __name__ == "__main__": 
    main()