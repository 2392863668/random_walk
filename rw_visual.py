import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 程序处于活动状态时，就不断模拟随机漫步
while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make a another walk? (y/n): ")
    if keep_running == 'n':
        break