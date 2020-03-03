def findSubarray(a, k, n): 
    vec=[] 
    for i in range(n-k+1): 
        temp=[] 
        for j in range(i,i+k): 
            temp.append(a[j]) 
        vec.append(temp) 
  
    vec=sorted(vec) 
  
    return vec[len(vec) - 1]

arr = [1,2,3,4,5]
k = 4
n = len(arr)

print(findSubarray(list(arr), k, n))
