class Car:

    numberOfCars = 0
    listOfCars = []
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.isOnSale = isOnSale
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        Car.numberOfCars += 1
        Car.listOfCars.append(self)


    @classmethod
    def ReadFromText(cls, aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW*1.36




print('Class level variables BEFORE creating instances: ', Car.numberOfCars, Car.listOfCars)

car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)

print('Class level variables AFTER creating instances: ', Car.numberOfCars, Car.listOfCars)

print('Check if object belongs to class:', isinstance(car_01, Car))
print('Check if object belongs to class using type:', type(car_01) is Car)
print('Check class of an object using __class__:', car_01.__class__)

print('List of instance attribute with values:', dir(car_01))
print('List of class attributes with values:    ', dir(Car))

print('*'*30)
lineOfText = 'Renault:Megane:True:True:False:False'
car_03 = Car.ReadFromText(lineOfText)


