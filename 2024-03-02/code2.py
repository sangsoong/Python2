with open(r'C:\baejunwoo\2024-03-02\sample.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    for index, value in enumerate(lines):
        print(index, value)