class MenuItem:
    def __init__(self, item_id, name):
        self.item_id = item_id
        self.name = name

    def __str__(self):
        return self.name

class CourseCategory:
    def __init__(self, category_name):
        self.category_name = category_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

class Menu:
    def __init__(self, menu_name):
        self.menu_name = menu_name
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def get_all_items(self):
        items = []
        for category in self.categories:
            items.extend(category.get_items())
        return items

class SpecialMenu(Menu):
    def __init__(self, menu_name):
        super().__init__(menu_name)
        self.discount = 30

class Branch:
    def __init__(self, location):
        self.location = location
        self.menus = []

    def add_menu(self, menu):
        self.menus.append(menu)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

class RestaurantController:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def total_menu_items(self):
        total = 0
        for branch in self.restaurant.branches:
            for menu in branch.menus:
                total += len(menu.get_all_items())
        return total

    def items_by_course_category(self, category_name):
        items = []
        for branch in self.restaurant.branches:
            for menu in branch.menus:
                for category in menu.categories:
                    if category.category_name == category_name:
                        items.extend(category.get_items())
        return items

    def special_menus(self):
        specials = []
        for branch in self.restaurant.branches:
            for menu in branch.menus:
                if isinstance(menu, SpecialMenu):
                    specials.append(menu)
        return specials


#main
# Restaurant
restaurant = Restaurant("Foodies")

# Branch
b1 = Branch("Bengaluru")
restaurant.add_branch(b1)

# Categories
starter = CourseCategory("Starter")
main = CourseCategory("Main")
dessert = CourseCategory("Dessert")

starter.add_item(MenuItem(1, "Soup"))
starter.add_item(MenuItem(2, "Salad"))

main.add_item(MenuItem(3, "Pasta"))
main.add_item(MenuItem(4, "Pizza"))

dessert.add_item(MenuItem(5, "Ice Cream"))

# Menus
menu1 = Menu("Regular Menu")
menu1.add_category(starter)
menu1.add_category(main)
menu1.add_category(dessert)

special_menu = SpecialMenu("Festive Menu")
special_menu.add_category(starter)
special_menu.add_category(main)
special_menu.add_category(dessert)

b1.add_menu(menu1)
b1.add_menu(special_menu)

# Controller
controller = RestaurantController(restaurant)

print("Total menu items:", controller.total_menu_items())

print("Starter items:")
for item in controller.items_by_course_category("Starter"):
    print(item)

print("Special discount menus:")
for menu in controller.special_menus():
    print(menu.menu_name)
