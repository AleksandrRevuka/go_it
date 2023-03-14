from temp_1 import get_name


def goodbuy(name):
    print(f"Goodbuy {name}")


def main():
    name = get_name()
    goodbuy(name)


if __name__ == '__main__':
    main()
    