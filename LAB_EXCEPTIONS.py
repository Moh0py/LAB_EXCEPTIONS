def additoin(x, y):
    return x + y
try:
    x = 10
    y = 20
    print("Addition:", x + b)
except NameError:
    print("Variable b is not defined")
# if you Use exception (finally) to run code regardless of success or failure.
else:
    print("the operation is successful:",additoin(10, 20))
