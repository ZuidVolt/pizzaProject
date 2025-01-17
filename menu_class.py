# Abstract class representing a menu item
class MenuItem:
    """Abstract class representing a generic menu item"""

    # Constructor method

    def __init__(self, name: str, description: str, cost: float) -> None:
        self.name = name
        self.description = description
        self.cost = cost


class PizzaMenu(MenuItem):
    """Class representing a pizza menu item"""

    # Method to print the details of the menu item

    # This item is used as the debugging to check if Constructor method is working
    def print_item(self) -> str:
        """prints the info in the object used for debugging"""
        return f"Name: {self.name}\nDescription: {self.description}\nCost: ${self.cost:.2f}\n"


# This is an example of a extension of the menu class Which could be implemented With greater scope of the project
class DrinksMenu(PizzaMenu):
    """Class representing a drinks menu item, extending the PizzaMenu class"""

    # Methods

    def check_if_caffeinated(self):
        """STUB: Check if the drink is caffeinated"""

    def check_if_alcoholic(self):
        """STUB: Check if the drink is alcoholic"""


## Create menu items for Debugging
# pepperoni = PizzaMenu("Pepperoni Pizza", "Delicious pepperoni pizza", 10.99)
# hawaiian = PizzaMenu("Hawaiian Pizza", "Sweet and savory Hawaiian pizza", 12.99)


# Create a list of menu items for Debugging
# menu_list = [pepperoni, hawaiian]

# Print each menu item's details
# print()

# for item in menu_list:
#     print(item.print_item())
