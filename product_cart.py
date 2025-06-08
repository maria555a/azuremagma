class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, count in self.products.items():
            total += item.price * count
        return total

    def __str__(self):
        lines = [f"User: {self.user}", "Items:"]
        for item, count in self.products.items():
            lines.append(f"{item.name}: {count} pcs.")
        return "\n".join(lines)


avocado = Item('cucumber', 3, "green", "middle", )
potato = Item('potato', 12, "brown", "small", )
strawberry = Item ('strawberry', 4, "red", 'small')
print(avocado)

buyer = User("Maria", "Ardasheva", "066330078")
print(buyer)

cart = Purchase(buyer)
cart.add_item(avocado, 4)
cart.add_item(potato, 20)
cart.add_item(strawberry, 30)
print(cart)

