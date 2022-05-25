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


class TransAgency:
    def __init__(self, name_tran, unit_weight, unit_path, delivery_speed, deliv_price, bad_weather):
        self.unit_weight = unit_weight  # единица веса
        self.unit_path = unit_path  # единица пути
        self.delivery_speed = delivery_speed  # скорость доставки
        self.deliv_price = deliv_price  # цена доставки
        self.bad_weather = bad_weather
        self.name_tran = name_tran

    def __int__(self):
        return int(self.unit_weight * self.unit_path * self.delivery_speed)

    def is_work(self, weather=random.choice(["Солнечно", "дождливо", "ураган", "метель", "пыльные бури"])):
        _flag = True
        if weather in self.bad_weather:
            _flag = False


class Air(TransAgency):
    def __init__(self, name_tran: str, unit_path=1.34, unit_weight=1.67, delivery_speed=15,
                 deliv_price=1.67 * 1.34 * 15):
        super().__init__(name_tran, unit_path, unit_weight, delivery_speed, deliv_price,
                         ["ураган", "метель", "пыльные бури"])

    def __str__(self):
        return f"способ доставки: {self.__class__.__name__}, скорость достовки:{self.delivery_speed},cтоимость доставки:{self.deliv_price}, что - то:{self.unit_weight * self.unit_path * self.delivery_speed}, погодные условия:{self.weather}"

    # @staticmethod
    # def random():
    #     pool = [
    #         {
    #             "nit_weight": "1.67",  # random.randint()
    #             "unit_path = unit_path": "1.34",  # random.randint()
    #             "delivery_speed": "15",  # random.randint()
    #             "deliv_price": "10 000 руб",
    #             "city": "Moscva: 15 000 000",
    #             "weather": random.choice(["Солнечно", "дождливо", "ураган", "метель", "пыльные бури"])
    #
    #         }
    #     ]
    #     return TransAgency.random(Air, pool)


class Auto(TransAgency):
    def __init__(self, name_tran: str, unit_path: float = 1.2, unit_weight: float = 1.25, delivery_speed=8,
                 deliv_price=1.2 * 1.25 * 8, ):
        super().__init__(name_tran, unit_path, unit_weight, delivery_speed, deliv_price, ["ураган", "пыльные бури"])


class Train(TransAgency):
    def __init__(self, name_tran: str, unit_path=1, unit_weight=2, delivery_speed=6, deliv_price=1 * 2 * 6):
        super().__init__(name_tran, unit_path, unit_weight, delivery_speed, deliv_price, ["ураган", "пыльные бури"])


class Autopark:
    def __init__(self, air, auto, train):
        self.air = air
        self.auto = auto
        self.train = train

    def calk(self, weight, distans, weather):
        transport = [*self.air, * self.auto, * self.train]
        f_t = []




Autopark(air=[
    Air("Airbus A310"),
    Air("Ан-225"), Air(" MD-11F ")],
    auto=[
        Auto("Fiat 500"), Auto("Ravon Matiz"), Auto("Hyundai Getz")],
    train=[
        Train("Ласточка"), Train("Сапсан"), Train("Наполеон")
    ])
