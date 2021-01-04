from die import Die

# 创建一个 D6
die = Die()

# 投掷几次骰子并将结果存储在列表当中
results = []
for roll_num in range(100):
    results.append(die.roll())

print(results)