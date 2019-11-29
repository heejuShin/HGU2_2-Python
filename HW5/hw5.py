from tkinter import *
from tkinter.filedialog import *     
from tkinter.scrolledtext import *

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
   
def sel():
   str1 = "[선택된 옵션 : " + str(option.get()) + "]"
   l2.config(text = str1)

def openFile():
   name = askopenfilename()
   l4.config(text=name)
   fn = l4['text']
   read=readfile(fn, option.get())
   s1.delete(1.0, END)
   s1.insert(END, read[1])

def Run():
   if(option.get()==1):
      print("option1")
      pwcode=e1.get()
      print(pwcode)
      #encryption(filename, txt, pwcode)
   elif(option.get()==2):
      print("option2")
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
