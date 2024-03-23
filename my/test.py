class TestClass:
    data = 0
    li = [0]
    dic = {
        'val': 0
    }

    def __init__(self):
        self.data = 0
        self.li = [0]
        self.dic = {'val': 0}

# 인스턴스 생성
c1 = TestClass()
c2 = TestClass()

# 값 변경
c1.data = 1
c1.li[0] = 1
c1.dic['val'] = 1

# 딕셔너리만 공유됨
print(f'c1의 data: {c1.data}\t', f'c1의 li: {c1.li[0]}\t', f'c1의 dic: {c1.dic['val']}')
print(f'c2의 data: {c2.data}\t', f'c2의 li: {c2.li[0]}\t', f'c2의 dic: {c2.dic['val']}')