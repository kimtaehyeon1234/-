shopping_bag={}

print("[구입]")
while True:
    item=input("상품명? ")
    
    if item =="":
        break
    count=int(input("수량은? "))
    shopping_bag[item]=count
    print(f"장바구니에 {item} {count}개가 담겼숩나다.\n")

print(f"\n>>> 장바구니 보기: {shopping_bag}")

print("\n[검색]")
find=input("장바구니에서 확인하고자 하는 상품은? ")
if find in shopping_bag:
    print(f"{find}은(는) {shopping_bag[find]}개 담겨 있습니다.")
else:
    print(f"{find}은(는) 장바구니에 없습니다.")
