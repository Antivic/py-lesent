from modules.burger_machine_new import get_coffee_order

if __name__ == '__main__':
    drink_dict = {
        'булочка белая': {
            '20см': 100,
            '30см': 150,
            '40см': 200
        },
        'булочка черная': {
            '20см': 150,
            '30см': 250
        },
        'булочка залотая': {
            '20см': 170,
            '30см': 220
        },
        
    }

    add_dict = {
        'катлета': 40,
        'сыр ': 20,
        'огурец и памидор': 30,
        'ничего': 0
    }

    order = get_coffee_order(add_dict=add_dict, drink_dict=drink_dict)
    print(order)
