def first(size, *args):
    return len(args) + size


def second(size, **kwargs):
    return len(kwargs) + size

first(5, "first", "second", "third")
second(3, comment_one="first", comment_two="second", comment_third="third")