from prettyprinter import pprint

def creat_catalog(file):
    with open (file, 'r', encoding='utf-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            dish = line.strip()
            ingridients = []
            for i in range(int(file_obj.readline())):
                keys_list = ['ingredient_name', 'quantity', 'measure']
                values_list = file_obj.readline().strip().split('|')
                ingridient = {key:value for key, value in zip(keys_list, values_list)}
                ingridient['quantity'] = int(ingridient['quantity'])
                ingridients.append(ingridient)
            cook_book[dish] = ingridients
            file_obj.readline()
    return cook_book


def get_shop_list_by_dishes(file: str, dishes: list, person_count: int):
      cook_book = creat_catalog(file)
      shop_list = {}
      for dish, value in cook_book.items():
          if dish in dishes:
            for i in range(len(cook_book[dish])):
              if cook_book[dish][i]['ingredient_name'] in shop_list.keys():
                 shop_list[cook_book[dish][i]['ingredient_name']]['quantity'] += (cook_book[dish][i]['quantity'] * person_count)
              else:
                measures_quantities = {}
                measures_quantities.update({'measure':cook_book[dish][i]['measure']})
                measures_quantities.update({'quantity':cook_book[dish][i]['quantity'] * person_count})
                shop_list.update({cook_book[dish][i]['ingredient_name']:measures_quantities})
      return shop_list

pprint(get_shop_list_by_dishes('recipes.txt', ['Блины', 'Омлет'], 2))