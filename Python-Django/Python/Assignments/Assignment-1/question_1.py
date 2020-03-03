def question_first_solution(input_seq): # complete
    def splitterz(txt):
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

    split_text = splitterz(str(input_seq))
    split_text = split_text.split(',')

    decoded = ''

    for idx, value in enumerate(split_text):
        val = list(set(value.strip()))
        possibilites = digit_mapping[val[0]]

        if len(value.strip()) > len(possibilites):
            diff = abs(len(value.strip()) - len(possibilites)) - 1
            decoded += possibilites[len(split_text[idx].strip()) - 2]
            decoded += possibilites[diff]
        else:
            decoded += possibilites[len(split_text[idx].strip()) - 1]
    
    return decoded


print(question_first_solution(866676665556664999))