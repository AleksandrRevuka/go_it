import os

def get_max_depth(path):
    """
    Returns the greatest folder nesting depth for the given path.
    """
    max_depth = 0
    for root, dirs, files in os.walk(path):
        depth = root.count(os.sep)
        if depth > max_depth:
            max_depth = depth
    return max_depth


print(get_max_depth('/home/alex/Desktop/garbage'))


# напиши функцію которая будет возвращать найбільшу глубину вложених папок
# навпаки найбільшу глубину вложених папок