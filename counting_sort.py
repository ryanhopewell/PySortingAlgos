unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]

def counting_sort(arr):

    max_value = max(arr)
    count = [0] * (max_value + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

sorted_array = counting_sort(unsortedArr)
print(f"Sorted Array: {sorted_array}")
