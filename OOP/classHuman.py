class Human:
    default_name = 'Karen'
    default_age = 33

    def __init__(self, name: str = default_name, age: int = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(self.name, self.age, self.__money, self.__house, sep='\n')

    @staticmethod
    def default_info():
        print(Human.default_name, Human.default_age, sep='\n')

    def earn_money(self, amount: int):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')

    def __make_deal(self, house, price):
        self.__money = self.__money - price
        self.__house = house

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Not enough money')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price: {final_price}')
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price, name):
        super().__init__(SmallHouse.default_area, price)
        self.__name = name

    def __str__(self):
        return self.__name


if __name__ == '__main__':
    Human.default_info()
    serg = Human('Sergik', 19)
    serg.info()
    hrushevka = SmallHouse(7800, "Hrushiovka")
    serg.buy_house(hrushevka, 30)
    serg.earn_money(6000)
    serg.buy_house(hrushevka, 30)
    serg.info()
