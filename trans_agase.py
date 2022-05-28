# Транспортное агентство
# Разработайте программу, имитирующую работу трансагентства.
# Трансагентство имеет сеть филиалов в нескольких городах.
# Транспортировка грузов осуществляется между этими городами тремя видами транспорта: автомобильным, железнодорожным и воздушным.
# Любой вид транспортировки имеет """стоимость единицы веса на и единицу пути скорость доставки."""
# Воздушный транспорт можно использовать только между крупными городами, этот вид самый скоростной и самый дорогой.
# Кроме того, воздушный транспорт зависит от погоды. Доставить груз воздушным путем можно только при условии хорошей
# погоды одновременно в городах отправки и назначения. Хорошая или плохая погода задается случайным образом.
# Железнодорожный транспорт можно использовать между крупными и средними городами, этот вид самый дешевый.
# Автомобильный транспорт можно использовать между любыми городами.
# Заказчики через случайные промежутки времени обращаются
# в один из филиалов трансагентства с заказом на перевозку определенной массы груза и возможным пожеланием о скорости/цене доставки.
# Трансагентство организует отправку грузов одним из видов транспорта с учетом пожеланий клиента.
# Оплату трансагенство получает только после успешной доставки груза.
# Между некоторыми городами для железнодорожного и/или автомобильного транспорта имеются скоростные магистрали,
# на которых скорость соответствующего вида транспорта увеличивается с заданным коэффициентом.
# При перевозке грузов могут происходить аварии, при этом вероятность аварии на автотранспорте больше,
# чем на железнодорожном транспорте, а авиатранспорт имеет аварийность очень низкую. На скоростных магистралях вероятность аварии меньше, чем на обычных дорогах.
# При аварии трансагентство возвращает заказчику двойную стоимость перевозки.
# Процесс имитации может быть остановлен пользователем программы для просмотра параметров объектов:
import random
from typing import List


class TransAgency:
    def __init__(self, name_tran, unit_weight, unit_path, delivery_speed, deliv_price, bad_weather, length, param1,
                 param2):
        self.unit_weight = unit_weight  # единица веса
        self.unit_path = unit_path  # единица пути
        self.delivery_speed = delivery_speed  # скорость доставки
        self.deliv_price = deliv_price  # цена доставки
        self.bad_weather = bad_weather
        self.name_tran = name_tran
        self.length = length
        self.param1 = param1
        self.param2 = param2

    def __int__(self):
        return int(self.unit_weight * self.unit_path * self.delivery_speed)

    def is_work(self, weather):
        _flag = True
        if weather in self.bad_weather:
            _flag = False
        return _flag


class Air(TransAgency):
    def __init__(self, name_tran: str, length: int, unit_path=1.34, unit_weight=1.67, delivery_speed=15,
                 deliv_price=1.67 * 1.34 * 15):
        super().__init__(name_tran, unit_path, unit_weight, delivery_speed, deliv_price,
                         ["ураган", "метель", "пыльные бури"], length, param1= 123, param2=232)

    def __str__(self):
        return f"способ доставки: {self.__class__.__name__}, наценка:{self.param1 * self.param2} скорость достовки:{self.delivery_speed}, цена:{abs(int(self.unit_weight * self.unit_path * self.delivery_speed))}"



class Auto(TransAgency):
    def __init__(self, name_tran: str, length: int, unit_path=1.34, unit_weight=1.67, delivery_speed=15,
                 deliv_price=1.67 * 1.34 * 15):
        super().__init__(name_tran, unit_path, unit_weight, delivery_speed, deliv_price,
                         ["ураган", "метель", "пыльные бури"], length, param1=123, param2=232)

    def __str__(self):
        return f"способ доставки: {self.__class__.__name__}, наценка:{self.param1 * self.param2} скорость достовки:{self.delivery_speed}, цена:{abs(int(self.unit_weight * self.unit_path * self.delivery_speed))}"


class Train(TransAgency):
    def __init__(self, name_tran: str, length: int, unit_path=1.34, unit_weight=1.67, delivery_speed=15,
                 deliv_price=1.67 * 1.34 * 15):
        super().__init__(name_tran, unit_path, unit_weight, delivery_speed, deliv_price,
                         ["ураган", "метель", "пыльные бури"], length, param1=123, param2=232)

    def __str__(self):
        return f"способ доставки: {self.__class__.__name__}, наценка:{self.param1 * self.param2} скорость достовки:{self.delivery_speed}, цена:{abs(int(self.unit_weight * self.unit_path * self.delivery_speed))}"


class Autopark:
    def __init__(self, air, auto, train):
        self.air = air
        self.auto = auto
        self.train = train

    def calc(self, weight, distans, weather):
        global length
        transport = [*self.air, *self.auto, *self.train]
        f_t = []
        for t in transport:
            if t.is_work(weather):
                f_t.append(t)

            if len(f_t) == 0:
                print("погодные условия: <дождливо, ураган, метель, пыльные бури> не подходят")
        _distanses: List[List[TransAgency]] = []
        _distans: List[TransAgency] = []
        for t in f_t:
            _distans.append(t)
            for t1 in f_t:
                if t == t1:
                    continue
                _sum = 0
                for d in _distans:
                    _sum += d.length

                if _sum < distans:
                    _distans.append(t1)
                else:
                    break

            _distanses.append(list(_distans))
            _distans = []

        for d in _distanses:
            print('Variant:')
            for i in d:
                print("\t-", i)
            print('------\n')


park = Autopark(air=[
    Air("Airbus A310", length=500),
    Air("Ан-225", length=300), Air(" MD-11F ", length=250)],
    auto=[
        Auto("Fiat 500", length=50), Auto("Ravon Matiz", length=78), Auto("Hyundai Getz", length=120)],
    train=[
        Train("Ласточка", length=120), Train("Сапсан", length=250), Train("Кузьмв Минин", length=300)
    ])
#######################################################################################################
park.calc(200, 1000, random.choice(["Солнечно", "дождливо", ]))  # "ураган", "метель", "пыльные бури"
