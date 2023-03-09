def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)


# M = {0: 0, 1: 1}
#
#
# def fib(n):
#     if n in M:
#         return M[n]
#     M[n] = fib(n - 1) + fib(n - 2)
#     return M[n]
#
#
# print(fib(999))

# fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
# def fib(n: int) -> int: return fib(n - 1) + fib(n - 2) if n > 2 else 1
#
#
# print(fib(20))


# def fibonacci(n):
#     global count
#     count += 1
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# count = 0
# print(fibonacci(10))
#
# num = 40
# fibo = []
# count = 0
# for i in range(0, num):
#     fibo_1 = fibonacci(i)
#     fibo.append(fibo_1)
# print(fibo)
# print(count)


# fib1 = fib2 = 1
# n = 1000000
# fibo = [0, fib1, fib2]
#
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     fibo.append(fib2)
# print(fibo[10000])

# fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
# print(fib(10))