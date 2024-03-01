import pytest
import sort_utils

from CollectionsEntry import CollectionEntry

# создаем наборы объектов

# набор на позитивный тест
setObj1_src = set({CollectionEntry("car", "К"),
                   CollectionEntry("cup", "З"),
                   CollectionEntry("house", "С"),
                   CollectionEntry("plain", "С"),
                   CollectionEntry("man", "З")})

setObj1_tgt = list()
setObj1_tgt.append(CollectionEntry("cup", "З"))
setObj1_tgt.append(CollectionEntry("man", "З"))
setObj1_tgt.append(CollectionEntry("house", "С"))
setObj1_tgt.append(CollectionEntry("plain", "С"))
setObj1_tgt.append(CollectionEntry("car", "К"))

# набор с лишним цветом
setObj2_src = set({CollectionEntry("sun", "Ж"),
                   CollectionEntry("apple", "З"),
                   CollectionEntry("sky", "С"),
                   CollectionEntry("fire", "К")})

setObj2_tgt = list()
setObj2_tgt.append(CollectionEntry("apple", "З"))
setObj2_tgt.append(CollectionEntry("sky", "С"))
setObj2_tgt.append(CollectionEntry("fire", "К"))

# набор с одинаковыми объектами
setObj3_src = set({CollectionEntry("fox", "К"),
                   CollectionEntry("fox", "К"),
                   CollectionEntry("fox", "К"),
                   CollectionEntry("fox", "К"),
                   CollectionEntry("fox", "К"),
                   CollectionEntry("fox", "К"),
                   CollectionEntry("fox", "К")})
setObj3_tgt = list()
setObj3_tgt.append(CollectionEntry("fox", "К"))
setObj3_tgt.append(CollectionEntry("fox", "К")),
setObj3_tgt.append(CollectionEntry("fox", "К")),
setObj3_tgt.append(CollectionEntry("fox", "К")),
setObj3_tgt.append(CollectionEntry("fox", "К")),
setObj3_tgt.append(CollectionEntry("fox", "К")),
setObj3_tgt.append(CollectionEntry("fox", "К"))

# набор из 1 объекта
setObj4_src = set({CollectionEntry("fox", "К")})

setObj4_tgt = list()
setObj4_tgt.append(CollectionEntry("fox", "К"))

# отсутствие значения
setObj5_src = set()

# набор с пустым параметром color
setObj6 = set({CollectionEntry("fox", None)})

# набор с пустым параметром color
setObj61_src = set({CollectionEntry("fox", "К"),
                    CollectionEntry("fox", None)})

setObj61_tgt = list()
setObj61_tgt.append(CollectionEntry("fox", "К"))

# набор с пустым параметром title
setObj7 = set({CollectionEntry("", "К")})

# набор с передачей пустых параметров
setObj8 = set({CollectionEntry("", "")})

# набор с объектами других цветов
setObj9 = set({CollectionEntry("car", "Ж"),
               CollectionEntry("house", "Ч"),
               CollectionEntry("plain", "Б")})


def test_sort1():
    result = sort_utils.sort(setObj1_src, "З<С<К")
    for i in range(len(result)):
        assert result.__getitem__(i).color == setObj1_tgt.__getitem__(i).color, 'Не соответствует'


def test_sort2():
    result = sort_utils.sort(setObj2_src, "З<С<К")
    for i in range(len(result)):
        assert result.__getitem__(i).color == setObj2_tgt.__getitem__(i).color, 'Не соответствует'


def test_sort3():
    result = sort_utils.sort(setObj3_src, "З<С<К")
    for i in range(len(result)):
        assert result.__getitem__(i).color == setObj3_tgt.__getitem__(i).color, 'Не соответствует'


def test_sort4():
    result = sort_utils.sort(setObj4_src, "З<С<К")
    for i in range(len(result)):
        assert result.__getitem__(i).color == setObj4_tgt.__getitem__(i).color, 'Не соответствует'


def test_sort5():
    result = sort_utils.sort(setObj5_src, "З<С<К")
    assert result.__eq__('Пустая коллекция')


def test_sort5x():
    result = sort_utils.sort(None, "З<С<К")
    assert result.__eq__('Коллекция отсутствует')

def test_sort6():
    result = sort_utils.sort(setObj6, "З<С<К")
    assert result.__eq__('Параметр цвета не передан')


def test_sort61():
    result = sort_utils.sort(setObj61_src, "З<С<К")
    for i in range(len(result)):
        assert result.__getitem__(i).color == setObj61_tgt.__getitem__(i).color


def test_sort0():
    result = sort_utils.sort(setObj1_src, "ЗСК")
    assert result == "Неверно задан прядок сортировки"


def test_sort9():
    result = sort_utils.sort(setObj9, "З<С<К")
    assert result == "Нет объектов необходимых цветов"
