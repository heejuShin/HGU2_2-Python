import random

def Encryption(fn,fp,pw):
    fn=fn.split('.')[0]
    try:
        s = fp.read()
    except:
        print("[Error]Can't read this file")
        return 0;
    content=[]
    key=[]
    key_num=random.randrange(100)
    asc_num=0
    for ch in pw:
        asc_num+=ord(ch)
    #print(asc_num)
    #count=0
    count=key_num
    for ch in s:
        check=0
        for i in range(len(content)):
            if content[i]==ch:
                check=1     
        if check==0:
            content.append(ch)
            key.append(count)
            count+=1
    key=random.sample(key,len(content))
    #print(content)
    #print(key)
    key=list(zip(content,key))
    key_dic=dict(key)
    print(key_dic)

    f_enc=open(fn+".enc","w")
    for i in range(len(s)):
        for j in range(len(content)):
            if s[i] == key[j][0]:
                f_enc.write(str(key[j][1])+" ")
    f_enc.close()
    print("\n[System]...암호와 완료...!")

    f_key=open(fn+".key","w")
    for i in range(len(content)):
        f_key.write(str(ord(key[i][0]))+" "+str(key[i][1]+asc_num)+" ")
    f_key.close()
    print("[System]...암호파일 저장 완료...!")
    return 0


def Decryption(fn,pw):
    fn=fn.split('.')[0]
    fp_key = open(fn+".key")
    try:
        s = fp_key.read()
    except:
        print("[Error]Can't read this file")
        return 0;
    asc_num=0
    for ch in pw:
        asc_num+=ord(ch)
    key_content=s.split(" ")
    #print(key_content)
    content=[]
    key=[]
    for i in range(len(key_content)-1):
        if i%2==0:
            content.append(chr(int(key_content[i])))
        else:
            key.append(int(key_content[i])-asc_num)
    #print(content)
    #print(key)
    fp_key.close()
    fp_enc = open(fn+".enc")
    fp_dec=open(fn+".dec","w")

    myzip=list(zip(key,content))
    dic=dict(myzip)
    print(dic)
    s=fp_enc.read()
    content=s.split(" ")
    for el in content:
        for key , value in dic.items():
            if el==str(key):
                fp_dec.write(str(value))
    fp_enc.close()
    fp_dec.close()
    print("\n[System]...복호화 완료...!")
    return 0


def main():
    print("=-=-=-=-=-=-=-=-=-=-=-=\nSecurity Fairy\n당신의 소중한 파일!\n암호-복호화를 도와드립니다.\n=-=-=-=-=-=-=-=-=-=-=-=")
    print("1)암호화, 복호화 중 원하는 옵션을 선택하세요\n2)암호화할 txt파일, 복호화할 enc파일을 선택하세요\n3)비밀번호를 입력하세요\n  암호화시 입력한 비밀번호는 복호화 시 꼭 필요하니 기억해두세요\n4)암호화와 복호화가 이루어집니다. \n")
    while 1:
        print("[option]\n","1)파일 암호화하기\n","2)암호화된 파일 복호하기")
        option=input("\t=>옵션을 선택하세요 : ")
        if option == '1' or option == '2':
            break
        else:
            print("[!]존재하는 옵션을 입력하세요\n")
    filename=input("\n*파일 이름을 입력해주세요: ")
    #filename="test"
    try:
        fp = open(filename)
    except IOError:
        print("[Error]There's no such file")
        return 0
    while 1 :
        check=1
        password=input("*비밀번호를 입력해주세요: ")
        if len(password)!= 4:
            print("비밀번호는 네자리여야합니다.")
            continue
        for ch in password:
            if ch == ' ':
                print("비밀번호에는 공백이 포함되면 안됩니다")
                check=0
                break
                '''
            if not ch.isdigit():
                print("비밀번호는 숫자로만 이루어져야합니다")
                check=0
                break
                '''
        if check==1:
            break

    print("=-=-=-=-=-=-=-=-=-=-=-=\n")
    if option == '1':
        Encryption(filename,fp,password)
    if option == '2':
        Decryption(filename,password)
    fp.close()

main()
print("\n=-=-=-=-=-=-=-=-=-=-=-=\nSecurity Fairy를 종료합니다\n=-=-=-=-=-=-=-=-=-=-=-=")
