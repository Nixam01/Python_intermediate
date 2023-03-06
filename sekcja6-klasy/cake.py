import pickle
import glob
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
    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
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
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('its not a cake')

    def show_info(self):
        print('{} - main taste: {} with additives of [{}], filled with {}, gluten free {}, Text: {}'.format(self.name.upper(), self.taste, self.additives, self.filling, self.__gluten_free, self.__text))


    def set_filling(self, fillingname):
        self.filling = fillingname

    def add_additives(self, listofadditives):
        self.additives.extend(listofadditives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on the cake')

    def save_to_file(self, path):
        with open(path, "wb") as f:
            pickle.dump(self, f)
            f.close()
    @classmethod
    def read_from_file(cls, path):
        with open(path, "rb") as f:
            cake = pickle.load(f)
            cls.bakery_offer.append(cake)
            f.close()
        return cake
    @staticmethod
    def get_bakery_files(dir):
        listofbakeryfiles = glob.glob(dir+'/*.bakery')
        return listofbakeryfiles




cake01 = Cake('Cheesecake', 'Cheesecake', 'sweet', ['sour'], 'raisins', True, 'very good cake')
cake02 = Cake('Murzynek', 'cake', 'sweet', ['chocolate'], 'cheery', False, 'delicious cake')
cake03 = Cake('Super Sweet Maringue', 'Meringue', 'very sweet', ['strawberries'], '', False, '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', True, 'special waffle')


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

for cake in Cake.bakery_offer:
    cake.show_info()

cake01.save_to_file('C:/Users/marci/PycharmProjects/Python_sredniozaawansowany/data/cake01.bakery')
cake02.save_to_file('C:/Users/marci/PycharmProjects/Python_sredniozaawansowany/data/cake02.bakery')
cake05 = Cake.read_from_file('C:/Users/marci/PycharmProjects/Python_sredniozaawansowany/data/cake02.bakery')

for cake in Cake.bakery_offer:
    cake.show_info()


print(Cake.get_bakery_files('C:/Users/marci/PycharmProjects/Python_sredniozaawansowany/data'))