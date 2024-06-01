a = input('ведите строку из цифр')
while True:
    try:
        int(a)
        break
    except:
        input("введите только цифры")
while len(a) > 1:
    a = str(sum([int(i) for i in a]))
print(a)