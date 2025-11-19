def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

F2022 = factorial(2022)
F2023 = factorial(2023)
F2024 = factorial(2024)

result = (F2024 // F2023) / F2022
print(result)