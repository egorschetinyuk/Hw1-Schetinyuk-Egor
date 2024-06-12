file= open('output.txt', 'w')
names = []
grades = []
try:
    ocenki = open('input.txt', 'r')
    for line in ocenki:
        name, grade = line.strip().split(',')
        grade = int(grade)
        grades.append(grade)
        names.append(name)
        print(grades)
        print(names)
        srednya = sum(grades) / len(grades)
        print(srednya)
        for i in range(len(grades)):
            if grades[i] > srednya:
                file.write(f"{names[i]},{grades[i]}\n")
    file.close()
except ValueError:
    print("файл не найден")