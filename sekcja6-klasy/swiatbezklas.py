'''
cake_01_taste = 'vanilia'
cake_01_glaze = 'chocolade'
cake_01_text = 'Happy Brithday'
cake_01_weight = 0.7

cake_02_taste = 'tee'
cake_02_glaze = 'lemon'
cake_02_text = 'Happy Python Coding'
cake_02_weight = 1.3


def show_cake_info(taste, glaze, text, weight):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        taste, glaze, text, weight))
show_cake_info(cake_01_taste, cake_01_glaze, cake_01_text, cake_01_weight)
show_cake_info(cake_02_taste, cake_02_glaze, cake_02_text, cake_02_weight)
'''
cake01 = {'taste':'vanilia','glaze':'chocolade','text':'Happy Brithday','weight':0.7}
cake02 = {'taste':'tee','glaze':'lemon','text':'Happy Python Coding','weight':1.3}

def show_cake(a_cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        a_cake['taste'], a_cake['glaze'], a_cake['text'], a_cake['weight']))

cakes = [cake01, cake02]

for cake in cakes:
    show_cake(cake)