def buy(it):
    print("[구입]")
    item=input("상품명? ")
    if item =="":
        return False
    count=int(input("수량은? "))
    it[item]=count
    print(f"장바구니에 {item} {count}개가 담겼숩나다.\n")

def show(it):
    print(f"\n>>> 장바구니 보기: {it}")


def find(it):
    print("\n[검색]")
    find=input("장바구니에서 확인하고자 하는 상품은? ")
    if find in shopping_bag:
        print(f"{find}은(는) {it[find]}개 담겨 있습니다.")
    else:
        print(f"장바구니에 {find}은(는) 없습니다.")


shopping_bag={}

while True:
    if buy(shopping_bag)== False:
        break
show(shopping_bag)
find(shopping_bag)
