def BinarySearch(data, target):
    lower = 0
    upper = len(data)-1
    while True:
        mid = (lower + upper) // 2
        if data[mid] == target:
            return mid
        elif mid == lower or mid == upper: return None
        elif data[mid] > target: upper = mid
        else: lower = mid

l = [1,2,3,4]
print(BinarySearch(l, -1))