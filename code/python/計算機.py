while True:
    b = int(input('一つ目の数字は？'))
    a = input('+,-,*,/を選択してください')
    c = int(input('二つ目の数字は？'))
    if a == '+':
        print('答えは'+str(b+c)+'です')
    if a == '-':
        print('答えは'+str(b-c)+'です')
    if a == '*':
        print('答えは'+str(b*c)+'です')
    if a == '/':
        if c == 0:
            print('0では割れません')
            d = input('終了する際はここにquitと入れてください')
            if d == 'quit':
                break
            continue
        print('答えは'+str(b/c)+'です')
    d = input('終了する際はここにquitと入れてください')
    if d == 'quit':
        break