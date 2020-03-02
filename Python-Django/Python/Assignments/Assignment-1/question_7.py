string = "An important  part of my life has been the people who stood by me  ."

str_split = string.split(" ")

res = []

if '' in str_split:
    res.append((False,["Two continuous spaces are not allowed."]))
if not string.endswith('.'):
    res.append((False,["the sentence must end with a full stop(.)","Two continuous uppercase characters are not allowed."]))

hasLower = False
hasUpper = False

for idx in string:
    if idx.islower():
        hasLower = True
        continue
    if idx.isupper():
        hasUpper = True
        continue
    else:
        

print(res)