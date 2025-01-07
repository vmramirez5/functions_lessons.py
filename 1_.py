from determineEligibilty import determineEligibilty_toGraduate, listOfMovies
# # functions are ways to wrap your code into reusable units

# function = A block of reusable code 
#            place () after the function name to invoke it

# #define a function with def
# # only define the function once
# # when I pass ini a parameter,
# # I am passing in a place holder
# # for future information
# def say_hello(name,age,address):
#     print (f"Hello {name}!")
#     print (f"How are you {name}?")
#     print(f"{name} is {age} years old")
#     print(f"{name} lives in {address}")

# #call the function
# #pass in the information called an argument
# say_hello("Dom", 12, '123 Main St')
# say_hello("Paul", 192,'456 Main St')
# say_hello("Bob", 3000, '789 Main St')



determineEligibilty_toGraduate("Alice", 120, 2.0, 800)
determineEligibilty_toGraduate("Bob", 119, 1.9, 799)

listOfMovies("The Matrix", 10, "action")
listOfMovies("The Hangover", 5, "comedy")
listOfMovies("The Ring", 3, "horror")
listOfMovies("Mufasa", 2, "animated")

# the return statement is used to return a value from a function

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# return = statement used ti end a function  and send a result back to caller

def add(x,y):
    z = x + y
    return z

def subtract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))
