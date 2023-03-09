def load():
    print("Загружаем")


def save():
    print("Сохраняем")


def default():
    print("Неизвестно как обработать")


def main(value):
    match value:
        case "load":
            load()
        case "save":
            save()
        case _:
            default()


main("load")
main("save")
main("hello")
