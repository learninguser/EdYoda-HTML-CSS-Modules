def findSubarray(a, k): 
    vec=[] 
    for i in range(len(a) - k + 1): 
        temp=[] 
        for j in range(i, i + k): 
            temp.append(a[j]) 
        vec.append(temp)  
    
    ans = vec[0]
    
    for idx in range(1, len(vec)):
        if vec[idx] > ans:
            ans = vec[idx]
    
    return ans

arr = [1,2,3,4,5]
k = 4

print(findSubarray(list(arr), k))
