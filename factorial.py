fac = lambda n: n * fac(n - 1) if n > 0 else 1

print(fac(5))