class bol():
    def __init__(self, x):
        self.x = x
        if type(x) == str:
            if x == 'True':
                self.x = True
            elif x == 'False':
                self.x = False
            else:
                self.x = res(x)


    def __eq__(self, other):
        if type(other) == str:
            other = res(other)
        if type(other) == type(bol(True)):
            other = other.res()
        return self.x == other


    def __add__(self, other):
        if type(other) == str:
            other = res(other)
        if type(other) == type(bol(True)):
            other = other.res()
        return self.x or other


    def __sub__(self, other):
        if type(other) == str:
            other = res(other)
        if type(other) == type(bol(True)):
            other = other.res()
        return  self.x and other


    def __mul__(self, other):
        if type(other) == str:
            other = res(other)
        if type(other) == type(bol(True)):
            other = other.res()
        return self.x and not other


    def __floordiv__(self, other):
        if type(other) == str:
            other = res(other)
        if type(other) == type(bol(True)):
            other = other.res()
        if self.x:
            return other
        else:
            return not other


    def res(self):
        return self.x



def bolname(s, name):
    s1 = ''
    c = True
    for i in s:
        if i == '(':
            s1 += 'bol'
        s1 += i
    return s1


def res(x):
    global namedict
    return namedict[x]


def split(s, b):
    a = []
    k = ''
    s1 = ''
    s = s + '*'
    c = True
    for i in s:
        if i not in b:
            k += i
            if c:
                s1 += '('
                c = False
        else:
            if k != '':
                s1 += "'" + k + "'"
                if k != 'True' and k != 'False':
                    a.append(k)
                k = ''
                if not c:
                    c = True
                    s1 += ')'
            s1 += i
    s1 = s1[0:-1]
    return a, s1


def f(a, n):
    global dv
    if n == 0:
        try:
            dv.append(a)
        except:
            dv = [a]
    else:
        f(a + [True], n - 1)
        f(a + [False], n - 1)


def provset(s):
    global namedict, dv
    znak = {'∪': '+', '⋂': '-', "\\": '*', '*': '//'}
    a = s.split('=')
    if len(a) > 1:
        try:
            s1 = ''
            for i in s:
                s1 += znak.get(i, i)
                if i == '=':
                    s1 += '='
            name, s1 = split(s1, ['+', '-', '*', ' ', '(', ')', '=', '\\', '//'])
            name = list(set(name))
            s1 = bolname(s1, name)
            c = True
            global dv
            dv = []
            f([], len(name))
            for i in dv:
                namedict = dict()
                for k in range(len(name)):
                    namedict[name[k]] = i[k]
                print(s1)
                try:
                    if not eval(s1):
                        c = False
                        return c
                        break
                except:
                    c = False
                    return 'Ошибка расчёта'
            if c:
                return c
        except:
            s1 = ''
            for i in s:
                s1 += znak.get(i, i)
                if i == '=':
                    s1 += '='
            name, s1 = split(s1, ['+', '-', '*', ' ', '(', ')', '='])
            name = list(set(name))
            if 'bol' in name:
                return 'В вражении нельзя испольовать имя bol'
            else:
                return 'Некорректное выражения'
    else:
        return 'Ошибка количества выражений'


def main():
    return provset(input('Введите, пожалуйста выражение с использованием операторов ∪ или +, ⋂ или -, \\ или * '))

'''
while True:
    try:
        print(main())
    except:
        break
'''

# Программа для создания калькулятора


# Программа, чтобы показать, как создать переключатель
# импорт кивый модуль

import kivy

# Базовый класс вашего приложения наследуется от класса приложения.
# app: всегда ссылается на экземпляр вашего приложения

from kivy.app import App

# это ограничивает kivy версию т.е.
# ниже этой версии вы не можете
# использовать приложение или программное обеспечение

kivy.require('1.9.0')

# для создания нескольких bttons для организации
# их мы используем это

from kivy.uix.gridlayout import GridLayout

# для размера окна

from kivy.config import Config

# Установка размера для изменения размера

Config.set('graphics', 'resizable', 1)


## Config.set ('graphics', 'width', '400')
## Config.set ('graphics', 'height', '400')


# Создание класса Layout

class CalcGridLayout(GridLayout):

    # Функция вызывается при нажатии equals

    def calculate(self, calculation):

        if calculation:

            try:

                # Решить формулу и отобразить ее в записи

                # на который указывает дисплей

                self.display.text = str(provset(calculation))

            except Exception:

                self.display.text = "Error"


# Создание класса приложения

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()


# создание объекта и запуск его

calcApp = CalculatorApp()

calcApp.run()

