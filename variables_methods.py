a = 5
b = 10
my_variable = 56
any_variable = 10

string_variable = "hello"
single_quotes = 'strings can have single quotes'

print(my_variable)
print(string_variable)


##

def my_print_method(my_argument):
    print(my_argument)
    # my_print_method("hello, world! ")


def my_multiply_method(number_one, number_two):
    return number_one * number_two

    result = my_multiply_method(5, 3)


# my_print_method(result)

my_print_method(my_multiply_method(5, 3))


# Complete the method by making sure it returns 42. .
def return_42():
    # Complete method here
    return 42  # 'pass' just means "do nothing". Make sure to delete this!

# Create a method below, called my_method, that takes two arguments and returns the result of its two arguments multiplied together.
def my_method(number_one, number_two):
    return number_one * number_two

    result = my_method(5 * 3)


# my_print_method(result)

print (my_method)
