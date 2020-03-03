# def min_elimination(n, arr): 
#     countOdd = 0 
#     for i in range(n):  
#         if (arr[i] % 2): 
#             countOdd += 1
#     return min(countOdd, n - countOdd)


# arr = [1,4,3,6,8,5,7]
# n = len(arr)
# print(min_elimination(n,arr))

def check_even(arr):
    if arr == []:
        return False

    for idx in range(len(arr)-1):
        if (arr[idx] + arr[idx + 1]) % 2 == 0:
            continue    
        else:
            return check_even(arr[idx +1 :])

arr = [1,4,3,6,8,5,7]
# new_list = arr.copy()
# for idx in range(len(arr)-1):
#     if (arr[idx] + arr[idx + 1]) % 2 == 0:
#         continue
#     else:
#         new_list.remove(arr[idx])

print(check_even(arr))