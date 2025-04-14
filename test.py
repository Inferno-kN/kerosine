import random
count_true = 0
for i in range(100):
    if random.randint(1,100) > 50:
        count_true += 1

print(count_true)


# print(random.randint(1, 100) > 3)
# print(random.randint(1, 1000) > 98)
# print(random.randint(1,100) > 50)