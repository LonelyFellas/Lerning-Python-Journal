var = 1
condition = [
    var == 1,
    type(var) == int,
    var > 0,
    var < 10
]

if all(condition):
    print("All conditions are true")
else:
    print("At least one condition is false")