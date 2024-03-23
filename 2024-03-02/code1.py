import datetime

# 읽기1
f = open(r'C:\baejunwoo\2024-03-02\sample.txt', 'rt', encoding='UTF-8')
print(f.read())
f.close()

# 읽기2
with open(r'C:\baejunwoo\2024-03-02\sample.txt', 'rt', encoding='UTF-8') as f:
    print(f.read())

# 쓰기1 : 시간
with open(r'C:\baejunwoo\2024-03-02\sample.txt', 'at', encoding='UTF-8') as f:
    f.write(f'\n\n=====[{str(datetime.datetime.now())}]=====\n\n')

# 쓰기2
with open(r'C:\baejunwoo\2024-03-02\sample.txt', 'a', encoding='UTF-8') as f:
    for i in range(0, 10):
        f.write(f'line {i+1}\n')

# 쓰기3 : 구구단
with open(r'C:\baejunwoo\2024-03-02\sample.txt', 'a', encoding='UTF-8') as f:
    for dan in range(2, 10):
        for gop in range(1, 10):
            f.write(f'{dan}*{gop}={dan*gop}\t')
        f.write('\n')

# 쓰기 4 : 입력
get = input('파일에 추가할 텍스트 >>> ')
with open(r'C:\baejunwoo\2024-03-02\sample.txt', 'a', encoding='UTF-8') as f:
    f.write(get + '\n')

# 쓰기 5 : 입력 및 예외처리
while True:
    get = input('파일에 추가할 정수 >>> ')
    try:
        get = int(get)
        get = str(get)
        break
    except ValueError:
        print('정수만 입력 가능')
    except:
        print('예기치 않은 오류')
with open(r'C:\baejunwoo\2024-03-02\sample.txt', 'a', encoding='UTF-8') as f:
    f.write(get + '\n')