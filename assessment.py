def fibonacci(num):
    list = [0, 1]
    for i in range(num-2):
        list.append(list[i] + list[i+1])
    return list
print(fibonacci(7))