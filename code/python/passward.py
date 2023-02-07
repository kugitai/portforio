passward = 'asked'
while True:
    inpass = input('パスワードを入力してください')
    if inpass != passward:
        print("異なります")
    else:
        print("承認しました")
        break
        