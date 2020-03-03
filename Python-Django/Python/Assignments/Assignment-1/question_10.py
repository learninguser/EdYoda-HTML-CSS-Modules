def adj_sum_even(arr):
    even_copy = arr.copy()
    odd_copy = arr.copy()

    even_count = 0
    odd_count = 0

    for s in arr:
        if s % 2 == 0: 
            even_copy.remove(s)
            even_count += 1
        else:
            odd_copy.remove(s)
            odd_count += 1

    if even_count > odd_count:
        count = odd_count
        ans = odd_copy
    else:
        count = even_count
        ans = even_copy
    return (count, ans)

arr =  [1, 3, 5, 4, 2]
print(adj_sum_even(arr))

arr = [1,4,3,6,8,5,7]
print(adj_sum_even(arr))

arr = [1,4,2,3,6,5]
print(adj_sum_even(arr))

arr = [1,2,2,4,3]
print(adj_sum_even(arr))