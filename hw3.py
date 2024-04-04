def get_fixed_price(sale_price):
    fixed_price=sale_price /(1-rate/ 100)
    return fixed_price



rate = int(input("할인율은? "))
sale_price_A=int(input("A상품의 할인된 가격은? "))
sale_price_B=int(input("B상품의 할인된 가격은? "))

print("A상품의 정가는", get_fixed_price(sale_price_A), "원")
print("B상품의 정가는", get_fixed_price(sale_price_B), "원")
