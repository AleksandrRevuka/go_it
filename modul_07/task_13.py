def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        lines = file.readlines()
        result = ''
        for line in lines:
            if profession in line:
                name, _ = line.strip().split(' ', 1)
                result += name + ' '
    file.close()
    profession = profession.replace(profession, "")
    return result.strip()
    
print(get_employees_by_profession('modul_07//emploee.txt', 'programmer'))