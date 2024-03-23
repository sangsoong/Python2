class Shop:
    total = 0
    menu_list = [{'떡볶이': 3000}, {'순대': 3000}, {'튀김': 500}, {'김밥': 2000}]

    @classmethod
    def sales(cls, food, count):
        for menu in cls.menu_list:
            if food in menu:
                cls.total += (menu[food] * count)

    @classmethod
    def get_total(cls):
        return cls.total

Shop.sales('떡볶이', 3)
Shop.sales('튀김', 4)
print(Shop.get_total())