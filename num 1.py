try:
    with open('output.txt', 'a') as file:
        names = []
        grades = []
        with open('input.txt', 'r') as ocenki:
            for line in ocenki:
                name, grade = line.strip().split(',')
                grade = int(grade)
                grades.append(grade)
                names.append(name)
        srednya = sum(grades) / len(grades)
        print(srednya)
        for i in range(len(grades)):
            if grades[i] > srednya:
                file.write(f"{names[i]},{grades[i]}\n")
except FileNotFoundError:
    print("Файл не найден")
