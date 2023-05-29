def in_array(array1, array2):
    
    return sorted(list(set(filter((lambda x : any(x in item for item in array2)), array1))))



a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1, a2))