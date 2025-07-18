
try:
    print(x)
except NameError:
    print("Veriable x is not defined")
else:
    print("Everything went wrong")


x = -7

if x < 0:
    raise Exception("Sorry, no numbers below zero")



















