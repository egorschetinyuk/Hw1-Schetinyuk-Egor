while True:
    try:
       
        with open('input1.txt', 'r') as perviy:
            itog1 = perviy.read().strip()  
        with open('input2.txt', 'r') as vtoroiy:
            itog2 = vtoroiy.read().strip()

        
        vmeste = itog1 + itog2
        sortirovochka = sorted(vmeste)

      
        sortirovochka1 = ''.join(i if i != '"' else ' ' for i in sortirovochka)

     
        with open('output2.txt', 'w') as file:
            file.write(sortirovochka1)

        break  
    except FileNotFoundError:
        print("Файл не найден. Проверьте наличие файлов и попробуйте снова.")
        break 

