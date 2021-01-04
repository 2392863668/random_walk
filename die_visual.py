from die import Die

# 创建一个 D6
die = Die()

# 投掷几次骰子并将结果存储在列表当中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)