import time

class Computer:

    def __init__(self, os=None):
        if os == None:
            self.os = 'Linux'
        else:
            self.os = os

    def set_spec(self, cpu, ram, vga, ssd):
        self.cpu = cpu
        self.ram = ram
        self.vga = vga
        self.ssd = ssd
    
    def hardware_info(self):
        print(f'CPU = {self.cpu}')

    def calc_sum(self, a, b):
        return a+b

    def calc_sub(self, a, b):
        return a-b

com = Computer()
print(com.os)


class Calculator:

    def input_expr(self):
        expr = input('수식 입력 >>> ')
        self.expr = expr

    def calculate(self):
        return eval(self.expr)
    
cal = Calculator()
cal.input_expr()
print(cal.calculate())


class Book:

    def set_info(self, title, author):
        self.title = title
        self.author = author

    def print_info(self):
        print(f'책 제목: {self.title}')
        print(f'책 저자: {self.author}')

book1 = Book()
book2 = Book()

book1.set_info('파이썬', 'python')
book2.set_info('자바', 'java')

book1.print_info()
book2.print_info()


class Watch:

    def set_time(self):
        now = time.strftime('%H:%M:%S')
        hms = now.split(':')
        self.hour = int(hms[0])
        self.minute = int(hms[1])
        self.second = int(hms[2])

    def add_hour(self, hour):
        self.hour += hour
        while(self.hour >= 24):
                    self.hour -= 24
    
    def add_minute(self, minute):
        self.minute += minute
        while(self.minute >= 60):
            self.minute -= 60
            self.hour += 1
    
    def add_second(self, second):
        self.second += second
        while(self.second >= 60):
            self.second -= 60
            self.minute += 1
        while(self.minute >= 60):
            self.minute -= 60
            self.hour += 1

    def print_time(self):
        print(f'{self.hour}시 {self.minute}분 {self.second}초')

watch = Watch()
watch.set_time()
watch.print_time()

watch.add_hour(3)
watch.add_minute(72)
watch.add_second(320)
watch.print_time()


class USB:

    def __init__(self, capacity):
        self.capacity = capacity

    def info(self):
        print(f'{self.capacity}GB USB')

usb = USB(32)
usb.info()


class Service:
    
    def __init__(self, service):
        self.service = service
        print(f'{self.service} 서비스를 실행합니다.')

    def __del__(self):
        print(f'{self.service} 서비스를 종료합니다.')

s = Service('길 안내')
del s


class Bag:
    count = 0

    def __init__(self):
        pass

    def acquire(self):
        self.count += 1

    @classmethod
    def sell(cls):
        cls.count -= 1

    @classmethod
    def buy(cls):
        cls.count += 1

    @classmethod
    def remain_bag(cls):
        return cls.count

bag1 = Bag()
bag2 = Bag()
print(Bag.remain_bag())

bag1.acquire()
bag2.acquire()
print(Bag.remain_bag())

bag1.sell()
bag2.sell()
print(Bag.remain_bag())