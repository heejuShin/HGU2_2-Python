from tkinter import *
from tkinter.filedialog import *     
from tkinter.scrolledtext import *
import sys


##ㅇ남은거
#1.파일 잘못읽었을 때 예외처리
#2.잘못된 파일 불렀을 때 예외처리
#3. 외 예외처리
#4. scrolled text 크기 및 GUI ppt랑 확인
#5. 기타 ppt랑 확

def readfile(filepath, choice):
    try:
        # 대상 파일 열기
        inf = open(filepath, encoding='utf-8')
        filetxt = inf.read() 
        inf.close()

        # 복호화의 경우, 키 파일 열기
        encKeys = []
        if choice == 2: # Decryption
            inf = open(filepath.split('.')[0]+'.key')
            encKeys = inf.read()
            inf.close()
            
        # 파일 읽기 성공(True), 읽은 파일 내용, 읽은 키 내용 리턴
        return True, filetxt, encKeys

    except IOError as err:
        # 파일 읽기 실패하면 파일 읽기 실패(False)와 실패 사유 메시지 리턴
        return False, 'I/O Error {}'.format(err)

def encryption(filename, txt, pwcode):
    # 텍스트로부터 고유 글자 뽑아내서 랜덤 번호 암호키 만들기
    import random
    str_to_encode = set(list(txt))
    codeDict = dict(zip(str_to_encode, random.sample(range(len(str_to_encode)), len(str_to_encode))))

    # 텍스트 암호화
    codedText = ''
    for t in txt:
        codedText += str(codeDict[t]) + ' '

    # 암호화된 텍스트 저장
    filename = filename.split('.')[0] # 확장자를 제외하고 따로 저장
    outf1 = open(filename+'.enc', 'w', encoding='utf-8')
    outf1.write(codedText)
    outf1.close()

    # 비밀번호 합을 이용하여 암호키 암호화
    encKeys = ''
    for c in codeDict.items():
        encKeys += str(ord(c[0]) + pwcode) + ' '
        encKeys += str(c[1] + pwcode) + ' '

    # 암호화된 암호키 저장
    outf2 = open(filename+'.key', 'w')
    outf2.write(encKeys)
    outf2.close()

    # 암호키 딕셔너리, 암호화 된 텍스트, 암호화된 암호키를 리턴
    return codeDict, codedText, encKeys

# 복호화 함수 - 파라메터는 파일이름, 암호화 된 파일본문, 비밀번호 합, 암호키(암호화된 상태)
def decryption(filename, txt, pwcode, enkeys):
    enkeys = enkeys.split() # 암호화된 암호키 텍스트를 공백을 이용해 리스트로 분리
    codeDict = {} # 복호키 저장할 dictionary
    decodedText = ''
    try:
        # 암호화된 암호키를 비밀번호합을 이용해 복호키로 복호화
        for i in range(0, len(enkeys), 2):
            codeDict[int(enkeys[i+1])-pwcode] = chr(int(enkeys[i])-pwcode)

        # 암호화된 텍스트를 복호키를 이용해 복호화
        for t in txt.split():
            decodedText += codeDict[int(t)] 
    except:
        # 복호화 실패하면 False를 리턴
        return False

    # 복호화 된 텍스트 저장
    filename = filename.split('.')[0] # 확장자를 제외하고 따로 저장
    outf = open(filename+'.dec', 'w', encoding='utf-8')
    outf.write(decodedText)
    outf.close()
    
    # 복호키 딕셔너리, 복호화 된 텍스트 리턴
    return codeDict, decodedText

def sel():
   str1 = "[선택된 옵션 : " + str(option.get()) + "]"
   l2.config(text = str1)
   
def checkPW(pw):
    pwcode = False
    # 비밀번호 자리 수 확인
    if len(pw) != 4: 
        # 자리 수 안 맞으면 False 리턴
        return False
    # 비밀번호 합을 구하면서 중간에 공백이 있는지 여부도 같이 확인
    else:
        for p in pw:
            pwcode += ord(p) # 유니코드로 바꿔서 합을 구함
            if p.isspace(): 
                # 하나라도 공백이 있으면 False 리턴
                return False
        # 비밀번호 형식이 잘 맞으면 4자리 합을 리턴
        return pwcode
    
def openFile():
   name = askopenfilename()
   l4.config(text=name)
   fn = l4['text']
   read=readfile(fn, option.get())
   #잘못읽었을 때 예외처리하고 종료하는 것
   if not read[0]:
      print('[err]')
      sys.exit()
   s1.delete(1.0, END)
   s1.insert(END, read[1][0:3000])
   if option.get()==2:
       s2.delete(1.0, END)
       s2.insert(END, read[2][0:3000])

def Run():
    if option.get()==1:
        pw=e1.get()
        pwcode=checkPW(pw)
        if not checkPW(pw):
            print("오류메세지")
            sys.exit()
        fn = l4['text']
        read=readfile(fn, option.get())
        enc = encryption(fn, read[1], pwcode)
        s2.delete(1.0, END)
        s2.insert(END, enc[0])
        s3.delete(1.0, END)
        s3.insert(END, enc[1][0:3000])
        s4.delete(1.0, END)
        s4.insert(END, enc[2][0:3000])
    elif(option.get()==2):
        pw=e1.get()
        pwcode=checkPW(pw)
        if not checkPW(pw):
            print("오류메세지")
            sys.exit()
        fn = l4['text']
        read=readfile(fn, option.get())
        dec = decryption(fn,read[1],pwcode,read[2])
        
        s3.delete(1.0, END)
        s3.insert(END, dec[0])
        s4.delete(1.0, END)
        s4.insert(END, dec[1][0:3000])
        
        
    else:
        print("여기에 에러 메세지 출력")
            #####
   
root = Tk()
root.title("HW5_21800412 Encryption & Decrytion")
root.geometry("700x790")
root.resizable(False,False)
root.configure(background='#ffcccc')

mycolor = '#ffcccc'
#option select
l1=Label(root,text="Choose 1 or 2", bg=mycolor)
l1.pack()
l1.place(x=20,y=20)

option = IntVar()

o1 = Radiobutton(root, text="1-Encryption", variable=option, value=1, command=sel, bg=mycolor)
o1.pack(anchor = W)
o1.place(x=250,y=20)

o2 = Radiobutton(root, text="2-Decryption", variable=option, value=2, command=sel, bg=mycolor)
o2.pack(anchor = W)
o2.place(x=420,y=20)

l2 = Label(root, bg=mycolor)
l2.pack()
l2.place(x=600,y=20)

#file name
l3=Label(root, text="file name: ", bg=mycolor)
l3.pack()
l3.place(x=20, y=50)
l4 = Label(root, bg=mycolor)
l4.pack()
l4.place(x=90, y=50)
b1=Button(root, text="Open file", command=openFile, bg=mycolor)
b1.pack()
b1.place(x=500,y=50)

#password
l5=Label(root, text="password(4 characters): ", bg="#ffcccc")
l5.pack()
l5.place(x=20, y=80)

e1 = Entry(root, width=4)#bd=2 #password e1
e1.pack()
e1.place(x=200, y=80)

b2=Button(root, text="Run", command=Run)
b2.pack()
b2.place(x=500, y=80)

#scrolledText
s1 = ScrolledText(root, width=80, height=10)
s1.pack()
s1.place(x=50,y=120)

s2 = ScrolledText(root, width=80, height=10)
s2.pack()
s2.place(x=50,y=285)

s3 = ScrolledText(root, width=80, height=10)
s3.pack()
s3.place(x=50,y=450)

s4 = ScrolledText(root, width=80, height=10)
s4.pack()
s4.place(x=50,y=615)


root.mainloop()

'''
#scrolledTect
s1 = ScrolledText()
s1.insert(END, "s1")
'''
