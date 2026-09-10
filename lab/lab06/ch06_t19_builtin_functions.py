def distance_from_zero(param:any):
    if type(param) == int or type(param) == float:
        return abs(param)
    else:
        return "Nope"
# 1. First, def a function called distance_from_zero, with one argument (choose any argument name you like).

# If the type of the argument is either int or float, the function should return the absolute value of the function input.
# Otherwise, the function should return "Nope"
