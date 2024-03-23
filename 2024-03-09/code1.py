class Coffee:
    
    def __init__(self, bean):
        self.bean = bean

    def coffee_info(self, price):
        print(f'원두: {self.bean}')
        print(f'가격: {price}')

coffee = Coffee('ethiopia')
coffee.coffee_info(5000)

class Espresso(Coffee):

    # 상속
    def __init__(self, bean, water):
        super().__init__(bean)
        self.water = water

    def espresso_info(self):
        super().coffee_info(7000)
        print(f'물: {self.water}')
    
    # 재정의
    def coffee_info(self, price):
        print(f'원두는 {self.bean} 입니다')
        print(f'가격은 {price} 입니다')

print()
espresso = Espresso('bean', 'water')
espresso.espresso_info()
print()
espresso.coffee_info(7000)
print()
print(espresso.bean)