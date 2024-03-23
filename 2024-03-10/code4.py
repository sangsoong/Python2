import matplotlib.pyplot as plt

x = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
y = [93.0, 94.2, 94.9, 95.8, 97.6, 99.1, 99.5, 100.0, 102.5, 107.7, 111.6]

plt.plot(x, y, linestyle="--", marker="^")
plt.show()