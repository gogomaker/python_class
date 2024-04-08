num = int(input("숫자를 입력하세요: "))
if(num%3 == 0) and (num%5 == 0):
    print("3과 5의 배수")
elif(num%3 == 0):
    print("3의 배수")
elif(num%5 == 0):
    print("5의 배수")
else:
    print("3의 배수도 5의 배수도 아닌 수")