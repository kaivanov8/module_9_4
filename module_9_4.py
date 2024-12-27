# создание функций на лету
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'
comparison_ = list (map(lambda x,y:x==y,first,second))
print('Совпадение букв ',comparison_)


def get_advanced_writer(file_name): #название файла для записи
    def write_everything(*data_set): # данные любого типа
        with open(file_name,'a',encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i))
    return write_everything
rtw = get_advanced_writer('for_advanced.txt')
rtw('Это строчка',['А','это','уже','число',5,'в','списке'])


class MysticBall:
    def __init__(self,*words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да','Нет','Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


