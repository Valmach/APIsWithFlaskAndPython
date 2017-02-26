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

    @staticmethod
    def go_to_school():
        print("I am going to school. ")
anna = Student("Anna", "MIT ")
rolf = Student("Rolf", "Oxford ")
anna.marks.append(56)
anna.marks.append(76)
Student.go_to_school()

# class Store:
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#         # You'll need 'name' as an argument to this method.
#         # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
#
#     def add_item(self, name, price):
#         # Create a dictionary with keys name and price, and append that to self.items
#         self.items.append({'name': name, 'price': price})
#
#     def stock_price(self):
#         total = 0
#         for stuff in self.items:
#             total += stuff['price']
#         return total
#         # Add together all item prices in self.items and return the total.

@classmethod

and @staticmethod


This
coding
exercise
requires
you
to
complete
two
method
implementations.

The
franchise
method, which
takes in a
store as argument.It
should
return a
new
Store
object,
with a name equal to the argument + " - franchise".
The
store_details
method, which
also
takes in a
store as argument.It
should
return a
string
representing
the
argument.
A
few
examples:

store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

# Store.franchise(store)  # returns a Store with name "Test - franchise"
# Store.franchise(store2)  # returns a Store with name "Amazon - franchise"
#
# Store.store_details(store)  # returns "Test, total stock price: 0"
# Store.store_details(store2)  # returns "Amazon, total stock price: 160"
# When completing the store_details method, you may need to convert the
# output of store.stock_price to an integer.You can do this like so: int(store.stock_price).


class Store:

    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):

        # Return another store, with the same name as the argument's name, plus " - franchise"

        return Store('{} - franchise'.format(store.name))

    @staticmethod
    def store_details(store):

        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

        return '{}, total stock price: {}'.format(store.name,
                store.stock_price())

