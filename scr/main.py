import mining

def main():
    promport = input("1.mining 2.sell 3.buy: ")
    if promport == "mining":
        hashes = mining.mining()  # 함수 끝날 때까지 기다림
        print("채굴 결과:", hashes)
        input("채굴이 끝났습니다. Enter를 눌러 종료하세요: ")


main()