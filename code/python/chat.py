name = input('名前を入力してください')
while True:
    chat = input()
    if chat != 'quit':
        print(name+':'+chat)
    else:
        break