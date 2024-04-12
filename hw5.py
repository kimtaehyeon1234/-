def read_single_digit(prompt):
    if prompt=="1":
        return "일"
    elif prompt =="2":
        return "이"
    elif prompt=="3":
        return "삼"
    elif prompt=="4":
        return "사"
    elif prompt=="5":
        return "오"
    elif prompt=="6":
        return "육"
    elif prompt=="7":
        return "칠"
    elif prompt=="8":
        return "팔"
    elif prompt=="9":
        return "구"
    elif prompt=="0":
        return "영"

def read_number(x):
    one= read_single_digit(x[0])
    two= read_single_digit(x[1])
    three= read_single_digit(x[2])
    print(one, two, three)
num= input("세 자리 정수 입력: ")
read_number(num)
