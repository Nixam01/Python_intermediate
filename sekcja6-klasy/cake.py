class Car:
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print(car_01.brand)

class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    def __init__(self, name, kind, taste, additives, filling, gluten_free):
        self.__gluten_free = gluten_free
        self.bakery_offer.append(self)
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def show_info(self):
        print('{} - main taste: {} with additives of [{}], filled with {}, gluten free {}'.format(self.name.upper(), self.taste, self.additives, self.filling, self.__gluten_free))


    def set_filling(self, fillingname):
        self.filling = fillingname

    def add_additives(self, listofadditives):
        self.additives.extend(listofadditives)


cake01 = Cake('Cheesecake', 'Cheesecake', 'sweet', ['sour'], 'raisins', True)
cake02 = Cake('Murzynek', 'Chocolate', 'sweet', ['chocolate'], 'cheery', False)
cake03 = Cake('Super Sweet Maringue', 'Meringue', 'very sweet', ['strawberries'], '', False)
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', True)


print('Today in our offer: \n')
for cake in Cake.bakery_offer:
    print('{} - main taste: {} with additives of [{}], filled with {}'.format(cake.name, cake.kind, cake.taste, cake.additives, cake.filling))
    print('*'*30)

for cake in Cake.bakery_offer:
    cake.show_info()
print('*' * 30)

cake03.set_filling('cream')


for cake in Cake.bakery_offer:
    cake.show_info()
print('*' * 30)

listofadditivesforcake01 = ['eggs', 'sugar']
cake01.add_additives(listofadditivesforcake01)

for cake in Cake.bakery_offer:
    cake.show_info()

print('-'*30)
print('Is cake01 an instance of class Cake: ', isinstance(cake01, Cake))
print('Is cake01 an instance of class Cake: ', type(cake01) is Car)
print('Info about cake01 instance: ',dir(cake01))
print('Info about Cake class: ',dir(Cake))

print('-'*30)
cake01.__gluten_free = False
for cake in Cake.bakery_offer:
    cake.show_info()
print(dir(cake01))
cake01._Cake__gluten_free = False
cake01.show_info()
print(dir(cake01))
