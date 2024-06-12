try:
    with open('input1.txt', 'r') as perviy:
        for lines in perviy:
            itog1 = lines.strip()

    with open('input2.txt', 'r') as vtoroiy:
        for lines in vtoroiy:
            itog2 = lines.strip()
except ValueError:
    print("некорректная строка")
vmeste = itog1 + itog2
sortirovochka = sorted(vmeste)
print(sortirovochka)
sortirovochka1=''
for i in sortirovochka:
    if i != '"' :
        sortirovochka1 += i
    else :
        sortirovochka1 += " "
with open('output2.txt', 'w') as file:
    file.write(str((sortirovochka1)))
