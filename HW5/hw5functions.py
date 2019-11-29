# 암호화 함수 - 파라메터는 파일이름, 암호화 할 파일본문, 비밀번호 합
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

# 비밀번호 형식 체크 함수
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
