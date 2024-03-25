def get_integer(prompt):
    res = int(input(prompt))
    return res

def exchange(money):
    f_hwon=money//500
    money%=500
    o_hwon=money//100
    money%=100
    f_twon=money//50
    money%=50
    t_twon=money//10
    print("500원 동전의 개수: ", f_hwon)
    print("100원 동전의 개수: ", o_hwon)
    print("50원 동전의 개수: ", f_twon)
    print("10원 동전의 개수: ", t_twon)

money= get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(money)
