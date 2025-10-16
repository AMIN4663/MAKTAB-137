class ShoppingCart:
    def __init__(self):
        self.__items = []
    def add_item(self, item):
        self.__items.append(item)
        print(f"{item} added to the basket")
    def remove_item(self, item):
        try:
            self.__items.remove(item)
            print(f"{item} removed from basket")
        except ValueError:
            print(f"{item} didn't found in the basket")
    def show_items(self):
        if not self.__items:
            print("The basket is empty")
        else:
            print("Basket items :")
            for i, it in enumerate(self.__items, 1):
                print(f"{i}. {it}")

