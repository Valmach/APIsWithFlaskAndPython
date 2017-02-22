# my_variable = "hello"
# for character in my_variable:  # iterable are strings, lists, sets, tuples , and more
#
#     print(character)
# my_list = [1, 3, 5, 7, 9]
#
# for number in my_list:
#     print(number ** 2)

# user_wants_number = True
# while user_wants_number == True:
#     print(10)
#     user_wants_number = False
#
#     user_input = input("Should we print again? (y/n) ")
#     if user_input == 'n':
#         user_wants_number = False

# known_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
#
# if person in known_people:
#     print("You know {} ! ".format(person))
# else:
#     print("You do not know {}! ".format(person))
#

## Exercise
def who_do_you_know():  # method
    people = input("Enter the people you know, separated by commas: ")
    people_list = people.split(",")
    people_without_spaces = []
    for person in people_list:
        people_without_spaces.append(person.strip())
        # remove a white space, beginning, middle, end.. using Strip
    return people_without_spaces


#  Ask the user for a list of people they know
# Split the string into a list
# Return the list

def ask_user():
    person = input("Enter the name of someone you know: ")
    if person in who_do_you_know():
        print("You know! {} ".format(person))

        # Ask user for their name
        # See if their name is in the people they know
        # Print out that they know the person


ask_user()
