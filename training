class Stock:
    def __init__(self, quantity=0):
        self.quantity = quantity

    def add(self, addition):
        self.quantity += addition

    def remove(self, removal):
        if removal <= self.quantity:
            print("Stock removed")
            self.quantity -= removal
        else:
            print("It was not possible to remove that quantity")

    def show(self):
        print(f"Current stock: {self.quantity}")


def menu():
    print("1 - Add product to stock")
    print("2 - Remove product from stock")
    print("3 - Show current stock")
    print("4 - Exit")


stock = Stock(0)

menu()
try:
    while True:
        question = int(input(""))
        if question == 1:
            print("Enter the quantity you want to add to stock: ")
            add_stock = int(input("\n"))
            stock.add(add_stock)
            print(f"The quantity {add_stock} was added to stock")
            menu()

        if question == 2:
            print("Enter the quantity you want to remove from stock: ")
            remove_stock = int(input("\n"))
            stock.remove(remove_stock)
            print(f"The quantity {remove_stock} was removed from stock")
            menu()

        if question == 3:
            stock.show()
            menu()

        if question == 4:
            print("Program terminated...")
            break
        else:
            print("Please enter numbers from 1 to 4")
            menu()
except ValueError:
    print("Please enter only integer numbers!")
