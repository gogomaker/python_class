'''
p03.py
Author: 22400373 손하용
이 프로그램은 두 개의 실수를 입력받고 
다양한 연산 결과를 출력하는
프로그램이다. 
'''

#첫번째 숫자 입력받기
firstNum = float(input("Input First Number:"))
#두번쨰 숫자 입력받기
secondNum = float(input("Input Second Number:"))
#줄 출력
print("-"*24)
#순서대로 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지, 제곱 연산 후 결과 출력
print("sum:", firstNum + secondNum)
print("sub:", firstNum - secondNum)
print("mul:", firstNum * secondNum)
print("div:", firstNum / secondNum)
print("floor div:", firstNum // secondNum)
print("mod:", firstNum % secondNum)
print("exp:", firstNum ** secondNum)
