lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 10, 15, 3, 7, 52)

}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 10, 15, 3, 7, 52)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer("Rolf")
player_one.numbers = (1, 3, 6, 9, 4)
player_two = LotteryPlayer("John")


# print(player_one.name == player_two.name)
##

class Student:
    def __int__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(76)
print(anna.average())


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        total = 0
        for stuff in self.items:
            total += stuff['price']
        return total
        # Add together all item prices in self.items and return the total.
