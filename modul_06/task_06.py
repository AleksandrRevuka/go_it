"""Створіть функцію get_recipe(path, search_id), яка повертатиме
словник для рецепта із зазначеним ідентифікатором MongoDB."""


def get_recipe(path: str, search_id: str) -> dict:
    """get recipe"""
    parameters = ['id', 'name', 'ingredients']
    recipe = []
    with open(path, 'r') as file:
        for line in file:
            if line.startswith(search_id):
                line_cliner = line.strip('\n')
                data = line_cliner.split(',')
                recipe.append(data.pop(0))
                recipe.append(data.pop(0))
                recipe.append(data)
                return dict(zip(parameters, recipe))
            else:
                return None



print(get_recipe("modul_06//task_06.txt", "60b90c3b13067a15887e1ae4"))
