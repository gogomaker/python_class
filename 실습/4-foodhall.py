pocket = int(input("주머니에 얼마나 있나요?: "))

print("당신이 먹을 수 있는 음식은")
if pocket >= 17000:
    print("치킨")
if pocket >= 14000:
    print("떡볶이")
if pocket >= 7000:
    print("국밥")
if pocket >= 5000:
    print("한정식")
if pocket > 0:
    print("짜장면")
