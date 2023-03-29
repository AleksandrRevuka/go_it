def recursive_yield(n):
    if n == 0:
        yield 0
    else:
        yield from recursive_yield(n-1)
        yield n
    
r = ''.join(str(i) for i in recursive_yield(10))
print(r)