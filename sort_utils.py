import collections
import string
import re

from CollectionsEntry import CollectionEntry


def printOut(objSet):  # проверка отображения объектов класса
    for entry in objSet:
        print(entry.title + " : " + entry.color)


def sort(collection, order):
    if not re.fullmatch(r'[ЗСК]<[ЗСК]<[ЗСК]', order):
        return 'Неверно задан прядок сортировки'
    if collection is None:
        return 'Коллекция отсутствует'
    if len(collection) == 0:
        return 'Пустая коллекция'


    # создаем пустые наборы для распределения объектов по цветам
    green = list()
    red = list()
    blue = list()

    unionCollection = list()

    for object in collection:  # распределяем по наборам
        if object.color == "З":
            green.append(object)
            continue
        if object.color == "К":
            red.append(object)
            continue
        if object.color == "С":
            blue.append(object)
            continue

        #if object.color != "C" and object.color != "З" and object.color != "К":
           # return 'Нет объектов необходимых цветов'
        #continue

    green_flag: bool = False
    blue_flag: bool = False
    red_flag: bool = False
    for orderEntry in order:  # задаем порядок цветов
        if orderEntry == "З":
            if green_flag is False:
                unionCollection.__iadd__(green)
                green_flag = True
            continue

        if orderEntry == "К":
            if red_flag is False:
                unionCollection.__iadd__(red)
                red_flag = True
            continue

        if orderEntry == "С":
            if blue_flag is False:
                unionCollection.__iadd__(blue)
                blue_flag = True
            continue

    return unionCollection
