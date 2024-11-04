with open("recipe.txt", encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        ingridientName = line.strip() 
        quantity_ingredients = file.readline().strip()
        recipe = []
        for i in range(int(quantity_ingredients)):
            ingridients = file.readline().strip().split('|')
            name, quantity, measure = ingridients
            recipe.append({'ingredient_name': name, 'quantity': quantity, 'measure': measure})   
        file.readline()
        cook_book[ingridientName] = recipe
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient_in in cook_book[dish]:
                ingredient, quantity, measure = ingredient_in.values()
                quantity = int(quantity)
                if ingredient in shop_list:
                    shop_list[ingredient]['quantity'] += quantity * person_count
                else:
                    shop_list[ingredient] = {'measure': measure, 'quantity': quantity * person_count}
    print(shop_list)
                
get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 3)
print()
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
print()
get_shop_list_by_dishes(['Омлет'], 5)
print()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)