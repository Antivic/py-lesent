'''
1. Вывод на экран меню
2. Выбор из списка напитков
3. Выбор объема из списка
4. Выбор количества сахара
5. Выбор добавок
6. Расчет суммы
'''

from utils.console import show_menu_from_collection


def get_coffee_order(drink_dict:dict, add_dict:dict):    

    def get_drink():
        """Функция, которая выводит на экран список напитков и просит сделать выбор.

        Returns:
            str | None: где str - выбранный булочку, None - "отмена"
        """

        return show_menu_from_collection(drink_dict, start_message='Привет!\nВыбери булочку:')

    def get_volume(drink_name: dict) -> str | None:
        """Функция, которая выводит на экран список объемов и просит сделать выбор.

        Args:
            drink_name (dict): выбранный размер

        Returns:
            str | None: str - выбранный размер, None -  "отмена"
        """

        return show_menu_from_collection(drink_dict[drink_name], start_message='Выбери размера:')

    def get_sugar():
        """Функция, которая просит выбрать количество кетчюпа (от 0 до 2)

        Returns:
            int: количество сахара
        """

        return show_menu_from_collection(range(1, 2+1), start_message='Выбери количество керчюпа от 1 до 2 или "выход":', isMenu=False)

    def get_add():
        """Функция, которая выводит на экран список добавок и просит сделать выбор.

        Returns:
            list | None: выбранная добавка или "отмена"
        """

        add_list = []

        while True:
            
            user_choose = show_menu_from_collection(add_dict, start_message='Выбери добавку:')
            
            if user_choose is None:
                return None
            elif user_choose == 'ничего':
                return add_list
            else:
                add_list.append(user_choose)

    def calculate_sum(drink: str, volume: int, sugar: int, add_list: str):
        """Функция, которая генерирует финальный заказ

        Args:
            drink (str): выбранный булочку
            volume (int): размер
            sugar (int): количество керчюпа
            add (str): добавки

        Returns:
            _type_: счет
        """
        # цена напитка в зависимости от объема
        drink_sum = drink_dict[drink][volume]

        add_sum = 0
        for add in add_list:
            add_sum += add_dict[add]

        return {
            'булочка': drink,
            'размер': volume,
            'кетчюп': sugar,
            'сума булочки и размер': drink_sum,
            'сума добавак': add_sum,
            'сума': drink_sum + add_sum
        }

    drink_name = get_drink()
    if drink_name is None:
        return None

    volume = get_volume(drink_name=drink_name)
    if volume is None:
        return None

    sugar = get_sugar()
    if sugar is None:
        return None

    add = get_add()
    if add is None:
        return None

    return calculate_sum(drink=drink_name,
                         volume=volume,
                         sugar=sugar,
                         add_list=add)
