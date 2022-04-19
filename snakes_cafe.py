# Welcome Message
welcome = \
    '**************************************' \
    '\n**    Welcome to the Snakes Cafe!   **' \
    '\n**    Please see our menu below.    **' \
    '\n**' \
    '\n** To quit at any time, type \"quit\" **' \
    '\n**************************************\n' \

# Menu Categories
appetizers = 'Appetizers \n----------' '\nWings' '\nCookies' '\nSpring Rolls'
entrees = 'Entrees \n-------' '\nSalmon' '\nSteak' '\nMeat Tornado' '\nA Literal Garden'
desserts = 'Desserts \n-------' '\nIce Cream' '\nCake' '\nPie'
drinks = 'Drinks \n-------' '\nCoffee' '\nTea' '\nunicorn Tears'
menu = [appetizers, entrees, desserts, drinks]

# Order Request
order_request = \
    '***********************************'\
 \
    '\n** What would you like to order? **'\
 \
    '\n***********************************'

# Another Request
another_request = \
    '****************************************'\
 \
    '\n** What else would you like to order? **' \
 \
    '\n**    type \"total\" when finished**    ' \
 \
    '\n****************************************'

# Print Menu
print(welcome)
for category in menu:
    print(f'{category}\n')
print(order_request)

# Accept Input
items = {}
while True:
    order = input('> ')
    if order == 'quit':
        break
    if order == 'total':
        print(items)
        break
    elif order not in items and order != 'total':
        items[order] = 0

    if order != 'total':
        items[order] += 1

    if items[order] > 1 and order != 'total':
        print(f"** {items[order]} orders of {order} have been added to your meal **")
        print(another_request)
    if items[order] == 1 and order != 'total':
        print(f"** {items[order]} order of {order} has been added to your meal **")
        print(another_request)

