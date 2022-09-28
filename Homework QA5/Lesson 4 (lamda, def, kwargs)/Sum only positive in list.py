my_list = [4, -12, 0, 9, -3, 1]
print(sum(list(filter(lambda x: x>=0, my_list))))

def positive_sum(arr):
    return sum(map(lambda x: x * 0 if x < 0 else x, arr))

def positive_sum2(arr):
    return sum(x for x in arr if x > 0)


print(positive_sum(my_list))
print(positive_sum2(my_list))