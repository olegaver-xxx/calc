from inputs import numone, numtoo, operation
from variable import plus, multiply, minus, delit
if plus:
    print(numone + numtoo)
elif minus:
    print(numone - numtoo)
elif multiply:
    print(numone * numtoo)
elif delit:
    print(numone / numtoo)
elif operation != plus or minus or multiply or delit:
    print("Ты ввел некорректные данные")
    while True:
        print("ЛОШАРА")
elif operation == int:
    print("it is int!")
else:
    pass