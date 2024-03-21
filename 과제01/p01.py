'''
p01.py
Author: 22400373 손하용
이 프로그램은 사용자로부터 이름과 학번을 입력받고
사용자의 이름과 입학년도를 출력하는
프로그램입니다. 
'''

#이름 입력받기
name = input("Input your name:")
#학번 입력받기
stu_num = input("Input student number:")
#입학년도 추출하기
admission_year = int(stu_num[1:3])
#만약 24년보다 큰 숫자가 들어오면 1900년대로 설정
if admission_year > 24: 
    admission_year += 1900
else: #그렇지 않으면 2000년대로 설정
    admission_year += 2000
#이름 출력하기
print("Name:"+name)
#입학년도 출력하기
print("Year of admission:"+str(admission_year))