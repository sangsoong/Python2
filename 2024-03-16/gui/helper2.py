import sys

class Person:

    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
    
    def info(self)->str:
        print(f'{self.name}, {self.phone}, {self.address}')
        return f'{self.name},{self.phone},{self.address}'

    def print_tel(self):
        pass
    
    def print_addr(self):
        pass

class AddressBook:
    
    def __init__(self):
        self.address_list = []
        self.file_reader()
    
    def file_reader(self):
        try:
            file = open(r'C:\baejunwoo\2024-03-16\gui\data\addressBook.csv', 'rt', encoding='UTF-8')
        except:
            print('addressBook.csv파일이 없습니다.')
        else:
            self.address_list = []
            while True:
                buffer = file.readline()
                if not buffer:
                    break
                name = buffer.split(',')[0]
                phone = buffer.split(',')[1]
                address = buffer.split(',')[2]
                self.address_list.append(Person(name, phone, address))
            print('addressBook.csv파일을 로드했습니다.')
    
    def menu(self):
        print('-' * 30)
        print('1. 주소록 추가 x')
        print('2. 주소록 삭제 x')
        print('3. 특정 주소록 조회 x')
        print('4. 전체 주소록 조회')
        print('0. 프로그램 종료')
        print('-' * 30)

        choice = 0
        while True:
            try:
                choice = int(input('선택 >>> '))
                if choice >= 5:
                    raise KeyError
            except:
                print('입력이 잘못되었습니다.')
                continue
            break
        print()

        return choice
    
    def exit(self):
        print('프로그램을 종료합니다.')
        sys.exit()
    
    def addr_add(self, name, num, addr):
        try:
            file = open(r'C:\baejunwoo\2024-03-16\gui\data\addressBook.csv', 'at', encoding='UTF-8')
        except:
            print('addressBook.csv파일이 없습니다.')
        else:
            file.write(f'{name},{num},{addr}\n')
    
    def addr_remove(self):
        pass
    
    def addr_modify(self):
        pass
    
    def addr_findall(self)->str:
        info = []
        str = ""
        for person in self.address_list:
            info.append(person.info())
        for line in info:
            str += line
        return str

    def run(self):
        while True:
            choice = self.menu()
            if choice == 0: self.exit()
            elif choice == 1: self.addr_add()
            elif choice == 2: self.addr_remove()
            elif choice == 3: self.addr_find()
            elif choice == 4: self.addr_findall()