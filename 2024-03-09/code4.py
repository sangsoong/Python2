try:
    print(4/0)
except ZeroDivisionError as e:
    print(f'[ERROR] 0으로 나누었습니다.')
except Exception as e:
    print(f'[ERROR] {e}')