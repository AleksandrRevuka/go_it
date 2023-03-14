fibo = lambda n : fibo(n - 1) + fibo(n - 2) if n > 2 else 1

print(fibo(10))