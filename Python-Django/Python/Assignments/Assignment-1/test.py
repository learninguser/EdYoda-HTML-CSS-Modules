def splitterz(text):
    return (''.join(x + ('' if x == nxt else ', ') 
            for x, nxt in zip(txt, txt[1:] + txt[-1])))
 

digit_mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

txt = '99999335533'
split_text = splitterz(txt)
split_text = split_text.split(',')
print(split_text)

decoded = ''

for idx, value in enumerate(split_text):
    val = list(set(value.strip()))
    possibilites = digit_mapping[val[0]]
    if len(value.strip()) > len(possibilites):
        diff = abs(len(value.strip()) - len(possibilites)) - 1
        decoded += possibilites[diff]
    else:
        decoded += possibilites[len(split_text[idx].strip()) - 1]

print(decoded)