# a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
# b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

# count = 0
# temp = []

# for idx, val in enumerate(a):
#     if val == b[idx]:
#         continue
#     else:
#         tInd = idx
#         temp.append([tInd, val, b[tInd]])
#         count = count + 1
#         if count == 3:
#             break
l1 = [[1,2,3],[4,5,6],[7,8,9]]
l2 = [[100,200,300],[400,500,600],[700,800,900]]
l4 = []

for idx in range(len(l1)):
    l3 = []
    for idy in range(len(l1[0])):
        l3.append(l2[idx][idy] + l1[idx][idy])
    l4.append(l3)
print(l4)