# ideal for either 1. importing a list of menu items or 2. importing each menu item manually

# either importing as a list containing the x amount of menu items
from menu_class import pizza_menu   

def calc_item_cost_list(menu_item, menu_item_index) -> float:
    chosen_item = menu_item[menu_item_index]
    return chosen_item.cost 

print(calc_item_cost_list(pizza_menu, 1))


# or importing each menu item manually 
from menu_class import pepperoni, hawaiian 


def calc_item_cost_manual(menu_item) -> float:  
    return menu_item.cost

print(calc_item_cost_manual(hawaiian))  





