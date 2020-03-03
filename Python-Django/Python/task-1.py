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

# s = "Python is easy to learn"
# s1 = "Python is Easy to Learn"

# if s[0].isupper() and s[1:].islower():
#     print(f"Yes, {s} is a captialise")
# else:
#     print(f"No, {s} is not a captialised string")

# if s1[0].isupper() and s1[1:].islower():
#     print(f"Yes, {s1} is a captialise")
# else:
#     print(f"No, {s1} is not a captialised string")

# s = "aabbccddabcdxyzaaa"
# count = 0
# max_char = ""
# for char in set(s):
#     if s.count(char) > count:
#         count = s.count(char)
#         max_char = char

# print(max_char, count)

# characters = {}
# keys = set(s)
# for key in keys:
#     if key not in characters:
#         characters[key] = 0
#     else:
#         characters[key] = characters[key] + 1

# for char in s:
#     characters[char] = characters[char] + 1

# itemMaxValue = max(characters.items(), key=lambda x : x[1])
 
# print('Max value in Dict: ', itemMaxValue[1])
# print('Key With Max value in Dict: ', itemMaxValue[0])

# arr = [2, 3, 6, 6, 5]
# arr = list(set(arr))
# arr.sort()
# print(arr[-2])

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# print ([[ i, j, k] for i in range( x + 1)\
#                     for j in range( y + 1)\
#                         for k in range( z + 1)\
#                             if ( ( i + j + k ) != n )])

# students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# students = dict(students)
# names = list(students.keys())
# marks = list(students.values())

# test = {k: v for k, v in sorted(students.items(), key=lambda item: item[1])}

# marks_sorted = sorted(set(marks))
# second_min = marks_sorted[1]
# print(second_min)

# print(marks.count(second_min))
# print(marks.index(second_min, 0, 2))
# first_min, second_min = float('inf'), float('inf')

# indices = []

# for idx, x in enumerate(marks):
#     if x <= first_min:
#         first_min, second_min = x, first_min
#     elif x < second_min:
#         second_min = x

# for idx, x in enumerate(marks):
#     if x == second_min:
#         indices.append(names[idx])

# for idx in sorted(indices):
#     print(idx)

# d = {}
# for idx in range(1,11):
#     d.setdefault(idx, idx**2)

# print(d)

# l = [10, 15, 20, 16, 25, 14, 89, 10, 100]

# d = {}

# for idx in range(1, 100, 10):
#     d.setdefault((idx, idx + 9),0)


# for idy in l:
#     for idx in d:
#         if idx[0] < idy <= idx[1]:
#             d[idx] = d[idx] + 1
#             break
# print(d)


# s = "aabbccddabcdxyzaaa"
# d = {}
# for char in set(s):
#     d[char] = s.count(char)

# print(d)

# d = {"maths":55, "phy":35, "chem":25, "eng":80}
# pass_mark = 40

# for idx in d.items():
#     if idx[1] < pass_mark:
#         print(idx[0])

# import random

# def gen_password(length):
#     upper = chr(random.randint(ord('A'),ord('Z')))
#     lower = chr(random.randint(ord('a'),ord('z')))

#     chars = ['!','&','%','$','#']
#     special = random.choice(chars)

#     digits = str(random.randint(10000,99999))

#     password = ''.join([upper, lower, special, digits])
#     password = ''.join(random.sample(password, length))
#     return password

# print(gen_password(5))
# l1 = [[1,2,3],[4,5,6],[7,8,9]]
# l2 = [[100,200,300],[400,500,600],[700,800,900]]
# l4 = []

# for idx in range(len(l1)):
#     l3 = []
#     for idy in range(len(l1[0])):
#         l3.append(l2[idx][idy] + l1[idx][idy])
#     l4.append(l3)
# print(l4)
