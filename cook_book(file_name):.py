import os
import pprint

def read_recipes(filepath):
    recipes = {}
    with open(filepath, encoding = 'utf-8') as f:
        recipe_data = []
        current_recipe = None
        for line in f:
            line = line.strip()
            if line:
                if not current_recipe:
                    current_recipe = line
                    recipe_data = []
                elif line.isdigit():
                    num_ingredients = int(line)
                    ingredients = []
                    for i in range(num_ingredients):
                        ingredients_line = f.readline().strip()
                        name, amount, unit = ingredients_line.split(' | ')
                        ingredients.append({'ingredient_name': name, 'quantity': amount, 'measure': unit})
                    recipes[current_recipe] = ingredients   
                    current_recipe = None    
    return recipes      


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = float(ingredient['quantity']) * person_count

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:
                    shop_list[ingredient_name] = {
                     'measure': measure, 'quantity': quantity
                     }    
    return shop_list                        



cook_book = read_recipes('recipes.txt')
pprint.pprint(cook_book)              

print('\nКоличество ингридиентов в заказе:')
pprint.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))