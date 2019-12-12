#21800412 heejushin

import sys
# 파일 읽기 함수 - 파라메터는 파일경로, 암호화(1)인지 복호화(2)인지 여부
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


def unique(filename, txt):
    str_to_encode = set(list(txt))
    return str_to_encode

def encryption(filename, txt):
    import random
    str_to_encode = set(list(txt))
    codeDict = dict(zip(str_to_encode, random.sample(str_to_encode,len(str_to_encode))))

    codedText = ''
    codedText2 = ''
    for t in txt:
        buff = str(ord(codeDict[t]))
        codedText += str(codeDict[t]) + ' '
        codedText2 += buff + ' '

    # 암호화된 텍스트 저장
    filename = filename.split('.')[0] # 확장자를 제외하고 따로 저장
    outf1 = open(filename+'.enc', 'w', encoding='utf-8')
    outf1.write(codedText2)
    outf1.close()

    # 비밀번호 합을 이용하여 암호키 암호화
    encKeys = ''
    for c in codeDict.items():
        encKeys += str(ord(c[0]) ) + ' '
        encKeys += str(ord(c[1])) + ' '

    # 암호화된 암호키 저장
    outf2 = open(filename+'.key', 'w')
    outf2.write(encKeys)
    outf2.close()

    # 암호키 딕셔너리, 암호화 된 텍스트, 암호화된 암호키를 리턴
    return codeDict, codedText, encKeys 

def decryption(filename, txt, enkeys):
    enkeys = enkeys.split() # 암호화된 암호키 텍스트를 공백을 이용해 리스트로 분리
    codeDict = {} # 복호키 저장할 dictionary
    codeDict2 = {}
    decodedText = ''
    try:
        # 암호화된 암호키를 비밀번호합을 이용해 복호키로 복호화
        for i in range(0, len(enkeys), 2):
            codeDict[int(enkeys[i+1])] = chr(int(enkeys[i]))
            codeDict2[chr(int(enkeys[i+1]))] = chr(int(enkeys[i]))

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
    return codeDict2, decodedText

# 1번
print("=-=-=-=-=-=-=-=-=-=-=-=\nSecurity Fairy\n당신의 소중한 파일!\n암호-복호화를 도와드립니다.\n=-=-=-=-=-=-=-=-=-=-=-=")
print("1)먼저 암호화가 진행됩니다. 암호화하고 싶은 파일을 고르세요.\n2)고유글자와 암호화 딕셔너리가 출력되고 암호화 파일이 만들어집니다.\n3)복호화를 선택할 것인지 묻습니다\n4)복호화하기를 선택했다면 파일 이름을 묻습니다\n5)복호화 딕셔너리가 출력되고 복호화 파일이 만들어집니다\n6)원한다면 처음부터 암호화를 시작할 수 있습니다. \n")

# 2번
# 2-A
while 1 :
    while 1:
        filename_full = input('파일이름: ')
        result = readfile(filename_full, 1)
        txt = ''
        enKeys = ''
        if result[0]:
            txt = result[1]
            print("파일 읽기에 성공했습니다.")
            print("파일의 크기(글자수): ",len(result[1]))
            break
        else:
            print("Error: {}".format(result[1]))
    save = len(result[1])
    #2-B
    print("\n아래는 읽어온 파일의 고유글자 (unique characters)들 입니다.")
    uc=unique(filename_full, txt)
    print(uc)

    #2-C
    print("\n아래는 암호화 딕셔너리입니다.")
    en=encryption(filename_full, txt)
    print(en[0])

    print("\n암호화가 성공적으로 끝났습니다. 암호화된 내용의 전체 크기: ",len(result[1]))

    #3
    con1 = input('복호화를 진행하시겠습니까? (종료 : !) : ')
    if con1 == '!':
        print("종료합니다.")
        sys.exit()

    # 4-A 
    while 1:
        filename_full = input('\n파일이름: ')
        result = readfile(filename_full, 2)
        txt = ''
        enKeys = ''
        if result[0]:
            txt = result[1]
            enKeys=result[2]
            print("파일 읽기에 성공했습니다.")
            print("파일의 크기(글자수): ",save)
            break
        else:
            print("Error: {}".format(result[1]))
    
    #4-B 
    de=decryption(filename_full, txt, enKeys)
    print("\n아래는 복호화 딕셔너리입니다.")
    if de[0]:
        print(de[0])
    else :
        print("복호화가 실패했습니다.")

    #4-c
    print("\n암호화가 성공적으로 끝났습니다. 암호화된 내용의 전체 크기: ",save)

    # 5
    con2 = input('암호화를 진행하시겠습니까? (종료 : !) : ')
    if con2 == '!':
        print("종료합니다.")
        sys.exit()
