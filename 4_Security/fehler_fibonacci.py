def fibonacci(n)
    fib_series = []
    a, b = 0, 1
    for _ in range(n)
        fib_series.append(a)
        a = b # a wird zu b
        a + b # b soll a+b sein
    return fib_series

# Anzahl der Fibonacci-Zahlen, die generiert werden sollen
anzahl = 10  # Du kannst die Anzahl der Zahlen anpassen

# Fibonacci-Zahlen generieren und ausgeben
fib_numbers = fibonacci(anzahl)
for num in fib_numbers
    print(num)
