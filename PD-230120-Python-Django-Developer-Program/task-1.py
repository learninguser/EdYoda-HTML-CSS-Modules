a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]

count = 0
temp = []

for idx, val in enumerate(a):
    if val == b[idx]:
        continue
    else:
        tInd = idx
        temp.append([tInd, val, b[tInd]])
        count = count + 1
        if count == 3:
            break