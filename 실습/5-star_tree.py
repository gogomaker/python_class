##이 프로그램은 사용자에게 몇 줄짜리 트리를 만들어 줄 지 정하는 프로그램이다. 

lineNum = int(input("몇 줄짜리 트리를 만들까요?: "))
blanknum = (lineNum*2-1)//2
starnum = 1

for i in range(lineNum):
    print(' '*blanknum+'*'*starnum+' '*blanknum)
    starnum+=2
    blanknum-=1