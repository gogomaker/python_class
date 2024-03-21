number = int(input("input integer = "))
mod_3= number % 3
mod_5 = number % 5

match(mod_3, mod_5):
    case(0,0): print("3, 5의 배수")
    case(0, _): print("3의 배수")
    case(_, 3): print("5의 배수")
    case _: print("3, 5의 배수 아님", number)

if mod_3 == 0 and mod_5 == 0:
    print("3, 5의 배수")
elif mod_3 == 0:
    print("3의 배수")
elif mod_5 == 0:
    print("5의 배수")
else:
    print("3, 5의 배수 아님", number)
