def get_dict():
    return {'status': 200, 'data': 'success'}


# Поскольку зависимых импортов нет, мы можем исполнить этот код для проверки
# Т.е. в качестве входной точки использовать нашу функцию
# Данный код исполнится только, когда этот файл будет исполняемым(не импортируемым)
print('example2.py outer')
if __name__ == '__main__':
    print('example2.py')
    print(get_dict())