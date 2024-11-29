

'''
Домашнее задание по теме "Интроспекция" Цель задания:

Закрепить знания об интроспекции в Python. Создать персональную функции для подробной интроспекции объекта.

Задание: Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

Создайте функцию introspection_info(obj), которая принимает объект obj.
Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
Верните словарь или строки с данными об объекте, включающий следующую информацию:
Тип объекта.
Атрибуты объекта.
Методы объекта.
Модуль, к которому объект принадлежит.
Другие интересные свойства объекта, учитывая его тип (по желанию).
Пример работы: number_info = introspection_info(42) print(number_info)

Вывод на консоль: {'type': 'int', 'attributes': [...], 'methods': ['abs', 'add', ...], 'module': 'main'}

Рекомендуется создавать свой класс и объект для лучшего понимания
'''

from pprint import pprint
import inspect

class InfoClass():
    def __init__(self, atr):
        self.atr = atr
        pass

# объявление функции исследования интроспекции
def introspection_info(obj):
    # объявление словаря результатов
    i_info = {'metods' : [],
           'attributes' : [],
           'module' : []}
    # цикл извлечения методов и аттрибутов исследуемого
    # объекта и добавления этих данных в словарь
    for i in dir(obj):
        if callable(getattr(obj, i)):
            i_info['metods'].append(i)
        else:
            i_info['attributes'].append(i)
    # извлечение информации о иодулях объекта интроспекции
    module = inspect.getmodule(obj)
    if module is None:
        i_info['module'] = __name__
    else:
        i_info['module'] = module.__name__
    # возврат словаря полученных данных
    return i_info

# исследуемый объект
number_info = introspection_info(42)
word_info = introspection_info('humen')
cl_info = InfoClass('x')
class_info = introspection_info(cl_info)
# вывод на консоль результатов
print('-'*10, 'number_info', '-'*10)
pprint(number_info)
print('-'*10, 'word_info', '-'*10)
pprint(word_info)
print('-'*10, 'class', '-'*10)
pprint(class_info)

print('-'*10, 'ВАРИАНТ 2', '-'*10)
def introspection_info2(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    attrs = [attr for attr in attributes if not callable(getattr(obj, attr))]
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__

    introsp_info = {'type': obj_type, 'attributes': attrs,
                    'methods': methods, 'module': module}

    return introsp_info


class Myclass:
    def __init__(self):
        self.name = 'Myclass'
        self.description = 100
        self.attributes = 1000

    def my_method(self):
        pass

obj = Myclass()

class_info = introspection_info2(obj) # класс
print(class_info)

number_info = introspection_info2(58) # число
print(number_info)

string_info = introspection_info2('Urban') # строка
print(string_info)

list_info = introspection_info2([1, 20, 4.0, 'word']) # список
print(list_info)

tuple_info = introspection_info2((1, 5, 23, 'doc')) # кортеж
print(tuple_info)




