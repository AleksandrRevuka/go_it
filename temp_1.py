def get_name():
    name = input("name: ")
    return name


def greet(name):
    print(f"Hello {name}")


def main():
    name = get_name()
    greet(name)


if __name__ == "__main__":
    main()
