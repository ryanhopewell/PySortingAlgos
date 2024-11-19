my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def bubble_sort(arr):

    n = len(arr)

    for i in range(n-1):

        for j in range (n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f"Sorted Array: {arr}")

def improved_bubble_sort(arr):

    n = len(arr)

    for i in range(n-1):

        swapped = False

        for j in range (n-i-1):

            if arr[j] > arr[j+1]:
                
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = False

        
        if not swapped:

            break

    print(f"Sorted Array: {arr}")

bubble_sort(my_array)
improved_bubble_sort(my_array)

