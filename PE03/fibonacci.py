def fibonacci(position):
    a = 0
    b = 1
    sequence = []

    for i in range(position + 1):
        sequence.append(a)
        next_number = a + b
        a = b
        b = next_number

    return sequence


position = int(input("What position of Fibonacci number you want to see? "))

result = fibonacci(position)

print(", ".join(map(str, result)))