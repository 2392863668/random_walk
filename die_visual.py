import pygal
from die import Die

# 创建一个 D6
die1 = Die()
die2 = Die()

# 投掷几次骰子并将结果存储在列表当中
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# print(results)
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)
# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')