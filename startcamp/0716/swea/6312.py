def check(*args):
    result = 1
    for i in args:
        if(type(i) != int):
            print("에러발생")
            return
        result *= i
    return result

result = check(1, 2, 3, 4)