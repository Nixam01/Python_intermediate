class Cake:
    '''
    Class representing cakes in bakery
    '''
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        '''

        :param name: name of Cake
        :param kind: kind of Cake
        :param taste: taste of Cake
        :param additives: addtives of Cake
        :param filling: filling of Cake
        '''
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)

    @property
    def full_name(self):
        '''
        input: an instance of an object
        :return: formatted name with kind of given cake
        '''
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)