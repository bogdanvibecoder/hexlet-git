with open('res.txt', 'w') as f:
    m = ["Анна", "Иван", "Мария", "Петр"]
    for i in m:
        print(i, file=f)