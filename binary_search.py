from bisect import bisect_left

def find_number(a, x):
    index = bisect_left(a, x)
  
    if index < len(a) and a[index] == x:
        return index
    else:
        return "такого числа нет"

# Ручная реализация

def binary_search(a, x):
    left, right = 0, len(a) - 1
  
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
          
    return "такого числа нет"
