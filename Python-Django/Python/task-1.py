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
# l1 = [[1,2,3],[4,5,6],[7,8,9]]
# l2 = [[100,200,300],[400,500,600],[700,800,900]]
# l4 = []

# for idx in range(len(l1)):
#     l3 = []
#     for idy in range(len(l1[0])):
#         l3.append(l2[idx][idy] + l1[idx][idy])
#     l4.append(l3)
# print(l4)

# s = "aaaaaavsdfasddddddddddddddddfasersdffffadg"
# unique_chars = []
# max_char = ""
# max_count = 0
# for idx in s:
#     if idx in unique_chars and s.count(idx) > max_count:
#         max_char = idx
#         max_count = s.count(idx)
#     else:
#         unique_chars.append(idx)

# print(f"{max_char} occurred {max_count} times")

# l1 = [10,20,30,40,100,50,80,65]
# l2 = [100,75,20,85,20]

# l1.extend(l2)
# l1.sort()
# l4 = []
# for idx in l1:
#     if idx not in l4:
#         l4.append(idx)
# print(l4)

# int x= 5;
# int y= -2;
# int z = 2;
# cout << (x + y * z <= x + z * z - x) << endl;


# l3 = list(set(l1).union(set(l2)))
# print(sorted(l3))


# def linear_search(l:list, key:int):
#     for value in l:
#         if value == key:
#             ans = True
#             break
#         else:
#             ans = False
#     return ans

# def find_max(l, which_max):
#     l = sorted(set(l))
#     return l[-which_max]
# l1 = [10,20,30,40,100,50,80,65]
# which_max = 3
# print(find_max(l1, which_max))

import random

special_chars = ['!','@','#','$','&']
lower_case_chars = list(range(ord('a'), ord('z') + 1))
upper_case_chars = list(range(ord('A'), ord('Z') + 1))
numbers = range(10000,100000)

def gen_password():
    special_char = random.choice(special_chars)
    lower_case = chr(random.choice(lower_case_chars))
    upper_case = chr(random.choice(upper_case_chars))
    number = str(random.choice(numbers))
    password = [special_char, lower_case, upper_case, number]
    password = ''.join(random.sample(password, 4))
    return password

if __name__ == "__main__":
    print(gen_password())