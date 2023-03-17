from functools import lru_cache


# fac = lambda n: n * fac(n - 1) if n else 1

# print(fac(2000))
print('next------->')


@lru_cache
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(497))
