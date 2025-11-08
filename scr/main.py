import mining
import sell_and_buy
import wallet

def promport():
    input("1.mining 2.sell 3.buy 4. view my wallet 6.view coin 7.exit")
def main():
    promport()
    if promport == "mining":
        hashes = mining.mining()
        promport()
    elif promport == "sell":
        sell_and_buy.sell()
        promport()
    elif promport == "buy":
        sell_and_buy.buy()
        promport()
    elif promport == "view my wallet":
        wallet.my_walletw()
        promport()
    elif promport == "view coin":
        print(sell_and_buy.main_ryl())
        print(up_or_down_ryl())
        promport()
    elif promport == "exit":
        exit('bye bye')
if __name__ == "__main__": 
    main()