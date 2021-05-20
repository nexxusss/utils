import random 
random.seed('ILGNL')


numbers = []
for _ in range(100):
    numbers.append(random.randint(0, 500))

numbers.sort()
print(numbers)


def binary_search(num_list, target, left, right):
    if left > right:
        return -1

    mid = (left + right)// 2
    if target == num_list[mid]:
        return mid

    elif target < num_list[mid]:
        return binary_search(num_list, target, left, mid + 1)

    elif target > num_list[mid]:
        return binary_search(num_list, target, mid + 1, right)

    else:
        pass

print(binary_search(numbers, 234, 0, len(numbers)))