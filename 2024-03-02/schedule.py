import datetime

# 파일 존재 확인, 파일 생성
try:
    f1 = open(r'C:\baejunwoo\2024-03-02\schedule.txt', 'r', encoding='UTF-8')
    if not(f1):
        f2 = open(r'C:\baejunwoo\2024-03-02\schedule.txt', 'w', encoding='UTF-8')
        f2.close()
    f1.close()
except:
    '[except] 파일이 없어 생성합니다'

num = 0
file_mode = 0
now = datetime.datetime.now().strftime('%Y년 %m월 %d일')

# 타임스탬프 (같은날짜일 땐 스탬프 안찍고 이어쓰기)
with open(r'C:\baejunwoo\2024-03-02\schedule.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        if line == f'{now}\n':
            file_mode = 1
            num = int(lines[len(lines)-1][4]) + 1
    if file_mode == 0:
        file_mode = 2
        num = 1

# 스케쥴 추가
with open(r'C:\baejunwoo\2024-03-02\schedule.txt', 'a', encoding='UTF-8') as f:
    # 타임스탬프
    if file_mode == 2:
        f.write(f'\n\n{now}')

    print(file_mode, num)
    
    while True:
        # 입력
        todo = input('오늘 할 일 (종료:아무것도 안적기) >>> ')
        
        # 종료
        if todo == '':
            if num == 1:
                f.write('\n없음')
            break
        
        # 할 일 추가
        f.write(f'\n할 일 {num} : {todo}')
        
        # 인덱스 증가
        num += 1