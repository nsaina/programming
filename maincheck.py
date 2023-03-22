from abc import ABC, abstractmethod
import time
class Pizza:
    def __init__(self, name='пицца', testo='тесто', sause='соус', fill='начинка',price=0):
        self.name=name
        self.testo=testo
        self.sause=sause
        self.fill=fill
        self.price=price
    def __str__(self):
        s="Название: {} Тесто: {} Соус: {} Начинка: {} Цена: {}".format(str(self.name),str(self.testo), str(self.sause), str(self.fill), self.price)
        return s
    @property
    def get_pizza(self):
        return NotImplementedError("нет геттера для введенного экземпляра")
    def _progress_bar(self,percent):
        # определение длины полосы загрузки
        bar_length = 20
        block = int(round(bar_length * percent / 100))
        # определение отображения загрузки в виде строки
        text = "\rLoading: [{0}] {1}%".format("#" * block + "-" * (bar_length - block), percent)
        # печать на экран отображения процесса загрузки
        print(text, end="", flush=True)

class Pepperoni(Pizza):
    def __init__(self):
        self.name='Пепперони'
        self.testo='Тонкое'
        self.sause='Кетчуп'
        self.fill='Пепперони, помидоры, сыр'
        self.price=490
        Pizza(self.name, self.testo, self.sause, self.fill, self.price)
    def get_pizza(self):
        return (self.name, self.testo,self.sause,self.fill,self.price)

    def gotovka(self,p1):
        print(f"Готовка теста (%s) - %d шт"%(self.testo, p1))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04*p1)  # для задержки в 0.1 секунды
        print(f"\nДобавление соуса: %s"%(self.sause))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04 * p1)  # для задержки в 0.1 секунды
        print(f"\nДобавление начинки: %s"%(self.fill))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04 * p1)  # для задержки в 0.1 секунды
        print(f"\nГотовка: %s - %d шт"%(self.name,p1))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04 * p1)  # для задержки в 0.1 секунды
        print(f"\nВаша пицца %s %d шт. готова. Приятного аппетита!)"%(self.name, p1))
class Barbequ(Pizza):
    def __init__(self):
        self.name='Барбекю'
        self.testo='Толстое'
        self.sause='Барбекю'
        self.fill='Говядина, сыр, овощи'
        self.price=590
        Pizza(self.name, self.testo, self.sause, self.fill, self.price)
    def get_pizza(self):
        return (self.name, self.testo,self.sause,self.fill,self.fill)
    def gotovka(self,p1):
        print(f"Готовка теста (%s) - %d шт"%(self.testo, p1))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04*p1)  # для задержки в 0.1 секунды
        print(f"\nДобавление соуса: %s"%(self.sause))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04 * p1)  # для задержки в 0.1 секунды
        print(f"\nДобавление начинки: %s"%(self.fill))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04 * p1)  # для задержки в 0.1 секунды
        print(f"\nГотовка: %s - %d шт"%(self.name,p1))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04 * p1)  # для задержки в 0.1 секунды
        print(f"\nВаша пицца %s %d шт. готова. Приятного аппетита!)"%(self.name, p1))
class DaryMorya(Pizza):
    def __init__(self):
        self.name='Дары Моря'
        self.testo='Среднее'
        self.sause='Майонез'
        self.fill='Рыба, сыр, зелень'
        self.price=450
        Pizza(self.name, self.testo, self.sause, self.fill,self.price)
    def get_pizza(self):
        return (self.name, self.testo,self.sause,self.fill,self.fill)
    def gotovka(self,p1):
        print(f"Готовка теста (%s) - %d шт"%(self.testo, p1))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04*p1)  # для задержки в 0.1 секунды
        print(f"\nДобавление соуса: %s"%(self.sause))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04 * p1)  # для задержки в 0.1 секунды
        print(f"\nДобавление начинки: %s"%(self.fill))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04 * p1)  # для задержки в 0.1 секунды
        print(f"\nГотовка: %s - %d шт"%(self.name,p1))
        for i in range(101):
            super()._progress_bar(i)
            time.sleep(0.04 * p1)  # для задержки в 0.1 секунды
        print(f"\nВаша пицца %s %d шт. готова. Приятного аппетита!)"%(self.name, p1))
class UserInterface:
    '''Реализует взаимодействие с пользователем'''
    piz1 = Pepperoni()
    piz2 = Barbequ()
    piz3 = DaryMorya()
    choice=[]
    def menu(self):
        '''Вывод меню'''
        print('1.', str(self.piz1))
        print('2.',str(self.piz2))
        print('3.',str(self.piz3))
    def kol_vo(self):
        '''Ввод количества товара'''
        count=1
        count=input("Введите количество ")
        if count.isdigit():
            return count
        else:
            print("Некорректный ввод")
            return self.kol_vo()
    def korzina(self,k):
        'к - это корзина пользователя (choice) (формирование корзины)'
        print('Ваш выбор пицца №1, №2, №3 ?\nВведите цифру',end=' ')
        num=input()
        if num!='1' and num!='2' and num!='3':
            print("некорректный ввод")
            return self.korzina(k)
        elif num=='1':
            count=int(self.kol_vo())
            for i in range(count):
                k.append(self.piz1.name)
        elif num=='2':
            count = int(self.kol_vo())
            for i in range(count):
                k.append(self.piz2.name)
        else:
            count = int(self.kol_vo())
            for i in range(count):
                k.append(self.piz3.name)
        print("Желаете еще добавить что-то?, Для добавления введите 1, Иначе будет переход к этапу оплаты заказа")
        num=input()
        if num=='1':
            self.choice = k
            return self.korzina(k)
        else:
            print("далее оплата")
            self.choice = k
            return self.oplata(k)

    def vyvod_korzina(self,zakaz):#вызов этой функции в oplata()
        p1 = zakaz.count("Пепперони")
        p2 = zakaz.count("Барбекю")
        p3 = zakaz.count("Дары Моря")
        print("Ваш заказ: ")
        if p1 != 0:
            print(f"%s - %d шт.; %s рб.* %d шт. = %d" % (self.piz1.name, p1, self.piz1.price, p1, self.piz1.price * p1))
        if p2 != 0:
            print(f"%s - %d шт.; %s рб.* %d шт. = %d" % (self.piz2.name, p2, self.piz2.price, p2, self.piz2.price * p2))
        if p3 != 0:
            print(f"%s - %d шт.; %s рб.* %d шт. = %d" % (self.piz3.name, p3, self.piz3.price, p3, self.piz3.price * p3))
        summa = self.piz1.price * p1 + self.piz2.price * p2 + self.piz3.price * p3
        print(f"К оплате: %d рублей" % (summa))
        return

    def oplata(self,zakaz): #вызов этой функции в korzina()
        self.vyvod_korzina(zakaz)
        print("Для изменения заказа введите 0, иначе будет произведена оплата заказа")
        num=input()
        if num=='0':
            print("Добавить к заказу - 1\nУдалить позиции из заказа - 0")
            num=self.zakaz_change_choice()
            if num=='1':
                return self.korzina(zakaz)#добавление к заказу
            else:
                return self.__delete(zakaz)#удаление позиций из заказа
        return self.__gotovka(zakaz)
    def __delete(self,zakaz):
        self.vyvod_korzina(zakaz)
        print("Изменить количество - 1; Удалить позицию - 0")
        n=self.zakaz_change_choice()
        if n=='1': #изменени еколичества пицц в заказе
            p1 = zakaz.count("Пепперони")
            p2 = zakaz.count("Барбекю")
            p3 = zakaz.count("Дары Моря")
            if p1!=0:
                print("Изменить количество", self.piz1.name,"- 1")
                n=input()
                if n=='1':
                    kol=self.kol_vo()
                    while zakaz.count(self.piz1.name)<int(kol):
                        zakaz.append(self.piz1.name)
                    while zakaz.count(self.piz1.name)>int(kol):
                        zakaz.remove(self.piz1.name)
            if p2!=0:
                print("Изменить количество", self.piz2.name, "- 2")
                n = input()
                if n == '2':
                    kol = self.kol_vo()
                    while zakaz.count(self.piz2.name) < int(kol):
                        zakaz.append(self.piz2.name)
                    while zakaz.count(self.piz2.name) > int(kol):
                        zakaz.remove(self.piz2.name)
            if p3!=0:
                print("Изменить количество", self.piz3.name, "- 3")
                n = input()
                if n == '3':
                    kol = self.kol_vo()
                    while zakaz.count(self.piz3.name) < int(kol):
                        zakaz.append(self.piz3.name)
                    while zakaz.count(self.piz3.name) > int(kol):
                        zakaz.remove(self.piz3.name)

        else: #удаление позиций в заказе
            p1 = zakaz.count("Пепперони")
            p2 = zakaz.count("Барбекю")
            p3 = zakaz.count("Дары Моря")
            if p1 != 0:
                print("Удалить", self.piz1.name, "- 1")
                n = input()
                if n == '1':
                    while zakaz.count(self.piz1.name) > 0:
                        zakaz.remove(self.piz1.name)
            if p2 != 0:
                print("Удалить", self.piz2.name, "- 2")
                n = input()
                if n == '2':
                    while zakaz.count(self.piz2.name) > 0:
                        zakaz.remove(self.piz2.name)
            if p3 != 0:
                print("Удалить", self.piz3.name, "- 3")
                n = input()
                if n == '3':
                    while zakaz.count(self.piz3.name) > 0:
                        zakaz.remove(self.piz3.name)
        self.choice = zakaz
        return self.oplata(zakaz)

    def zakaz_change_choice(self): #
        '''выбор между 1 или 0'''

        n=input()
        if n=='1' or n=='0':
            return n
        else:
            print("Некорректный ввод")
            return self.zakaz_change_choice()

    def __gotovka(self,zakaz):
        '''процесс готовки заказа'''
        print("\r"*10)
        print("Процесс готовки заказа")
        p1 = zakaz.count("Пепперони")
        p2 = zakaz.count("Барбекю")
        p3 = zakaz.count("Дары Моря")
        if p1!=0:
            self.piz1.gotovka(p1)
        if p2!=0:
            self.piz2.gotovka(p2)
        if p3!=0:
            self.piz3.gotovka(p3)
        return
    def start(self):
        self.menu()
        self.korzina(self.choice)
a=UserInterface()
a.start()

'''Дальше нужно написать процесс готовки пиццы
это функция вызывается из oplata()'''






