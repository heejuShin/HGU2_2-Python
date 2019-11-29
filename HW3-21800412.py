import random
level = 1
repeat1 = 0 #FALSE
repeat2 = 0 #FALSE
print("==== RANDOM GAME ====\n\n당신의 운을 시험해보세요\n\n이 게임은 총 2단계로 나누어져있습니다.\n1단계는 2개이상의 단어를 입력받아\n리스트를 만듭니다.\n컴퓨터가 그 중 한 단어를 랜덤으로 고릅니다.\n그 단어를 맞추어보세요!\n\n2단계는 당신이 입력한 문장을\n여러 단어로 나눕니다.\n컴퓨터가 그 중 몇 번째 단어를 선택했는지 \n맞추어보세요.\n매 단계가 끝날 때마다\n단계반복, 단계수정, 종료\n세 가지 선택이 가능합니다.\n단계 반복을 선택할 시 \n단어들은 바뀌지 않고 컴퓨터가 선택한 단어만\n변경됩니다.\n\n자, 게임을 즐기세요!")

while 1: #전체 반복을 위한 while
    if level == 1 : #level 1
        print("\n=====1단계=====\n")

        if not repeat1 : #같은 단계 반복할 때 리스트를 다시 만들지 않기 위함
            mylist=[] #list 초기화
            while 1 : #계속 입력받기 위한 while
                element=input("리스트 요소를 입력하세요: ")
                if element.isspace() or element == '':
                    if len(mylist) < 2:
                        print("요소가 ",len(mylist),"개 입니다. 리스트 요소가 부족합니다.\n")
                        print("다시 ", end='')
                    else:
                        break #입력 받는 것을 그만둠
                else:
                    mylist.append(element)

        if repeat1 : #같은 단계 반복시 입력받았던 list로 실행
            print("입력받은 list로 반복합니다.")
        print("\n입력하신 리스트입니다.", mylist, "\n")

        computer = random.choice(mylist)
        while 1 : #맞출때까지 확인하기 위한 while
            user = input("컴퓨터가 선택한 단어는 무엇일까요? ")
            if computer == user :
                break
            else:
                print("틀리셨습니다.\n")


        again=input("맞추셨습니다.\n\n다시 한 번 도전하시겠습니까?(y) : ")

        if again != 'y' :
            next1=input("다음 단계에 도전하시겠습니까?(y) : ")
            if next1 == 'y' :
                level = 2
                repeat2 = 0
                continue
            else :
                break #전체 while문 break

        else:
            repeat1 = 1 #TRUE
            continue


    if level == 2 : #level2
        print("\n=====2단계=====\n")

        if not repeat2 :
            mylist=[]
            while 1 : #계속 입력받기 위한 while
                mystr=input("문장을 입력해주세요: ")
                mylist2=mystr.split(' ')
                if len(mylist2) < 2:
                    print("문장 내 단어가 2개 이상이어야 합니다.\n")
                    print("다시 ", end='')
                else :
                    break

        if repeat2 :
            print("입력받은 list로 반복합니다.")
        print("\n입력하신 리스트입니다.", mylist2, "\n")

        computer = random.randrange(0,len(mylist2),1)
        while 1 : #맞출때까지 확인하기 위한 while
            print("[인덱스 번호는 0부터 시작합니다]")
            num = input("컴퓨터가 선택한 단어의 인덱스 번호는 무엇일까요? : ")
            if num.isdigit():
                num=int(num)
            if computer == num :
                break;
            else:
                print("틀리셨습니다.\n")


        again=input("맞추셨습니다.\n\n다시 한 번 도전하시겠습니까?(y) : ")

        if again != 'y' :
            next2=input("이전 단계로 돌아가시겠습니까?(y) : ")
            if next2 == 'y' :
                level = 1
                repeat1 = 0
                continue
            else :
                break #전체 while문 break

        else:
            repeat2 = 1 #TRUE
            continue

print("\n=====종료합니다=====\n")
