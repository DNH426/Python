# Global var are in CAPS
# Python uses Dynamic Typing: Gives the developer the ability to reassign variables to different data types
# Pros of Dynamic Typing:
    # Very easy to work with
    # Faster development time
# Cons of Dynamic Typing:
    # May result in bugs for unexpected data types
    # Need to be aware of type()

# ========================

# # Eaxmples

# # 1

# # data type = int 
# my_dogs = 2

# # data type = list
# my_dogs = ["Cubs", "Sox"]

# # 2

# # What will be logged?
# a = 5
# a = 'dog'
# print(a)
# print(a)
# # Dog because the last data type assigned to a was 'dog'

# # 3

# a = 10
# print(a)
# a = 6
# a = a + a
# print(a)
# print(type(a))

# # 4

# my_income = 150
# tax_rate = 0.1
# my_taxes = my_income * tax_rate

# print(my_taxes)