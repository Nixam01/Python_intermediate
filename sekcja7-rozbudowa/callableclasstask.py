class Noduplicates():
    def __init__(self, listofclass):
        self.listofclass = listofclass

    def __call__(self, new_objects):
        for element in new_objects:
            if not element in self.listofclass:
                self.listofclass.append(element)

my_no_dup_list = Noduplicates([])
print(my_no_dup_list.listofclass)
my_no_dup_list(['keyboard','mouse'])
print(my_no_dup_list.listofclass)
my_no_dup_list(['keyboard','mouse','pendrive'])
print(my_no_dup_list.listofclass)
my_no_dup_list(['charger','pendrive'])
print(my_no_dup_list.listofclass)



