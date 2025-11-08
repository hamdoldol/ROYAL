

def buy(my_ryl,money,ryl):
    my_ryl = 0
    ryl = ryl(0)
    money = 1000000
    sell_ryl = int(input("what amount of RYL do you want to sell?"))
    if ryl >= my_money:
        print("oh,no! you don't have enough money")
    else:
        print('filnished sellin,you have money is,', my_money - ryl)
        ryl += up_ryl(100)
        my_ryl += 1

def sell(my_ryl,money):
    my_ryl = 0
    promport = int(input("how many RYL do you want to buy?"))
    ryl = 0
    if promport > my_ryl:
        print("oh,no! you don't have enough RYL")
    else:
        my_ryl -= promport
        up_ryl(100)
def up_ryl(ryl):
    ryl += ryl
def down_ryl(ryl):
    ryl -= ryl
def main_ryl():
    if sell == True:
        doun_ryl(100)
    elif buy == True:
        up_ryl(100)
    return up_ryl - down_ryl
def up_or_down_ryl():
    if sell == True:
        print("RYL is 1%down")
    elif buy == True:
        print("RYL is 1%up")