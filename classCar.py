class Car:
    '''Very cool cars
By default: color = 'black', model = 'Tesla', engine_capacity = '2000' '''
    price = '8000'

    def __init__(self, color='black', model='model_X', engine_capacity='2000'):
        self.__color = color
        self.model = model
        self.engine_capacity = engine_capacity
        self.price

    def price_car(self):
        if self.model == "modelX":
            self.price = '30000'
        elif self.model == 'Q7':
            self.price = '40000'
        else:
            self.price = '25000'
        return self.price

    @classmethod
    def cars_form(Car, model):
        cars_form = Car(model)
        return cars_form

    @staticmethod
    def chet():
        number = int(input())
        if number % 2 == 0:
            print('Chet')
        else:
            print('Nechet')

bmw_x5 = Car('blue', 'X5', '3000')
audi_q7 = Car('white', 'Q7', '3000')
mersedes_eclass = Car('red', 'E30', '2000')
tesla = Car()

class Supercar(Car):
    def __init__(self):
        super().__init__()
        self.power = 0

    def change_power(self, num):
        self.power = num
        print(f'This car power is {self.power}')

lamborgini = Supercar()
lamborgini.change_power(500)

print(lamborgini.change_power(300))
print(dir(Supercar))