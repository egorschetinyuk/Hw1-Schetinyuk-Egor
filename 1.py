while True:
    a = input('введите целое число')
    try:
        int(a)
        break
    except:
        input("введите только число")
while len(str(a)) >= 1:
    b = int(a)
    for i in range(1,b*2,2):
        print(('*'*i).center(b*2))
    break
