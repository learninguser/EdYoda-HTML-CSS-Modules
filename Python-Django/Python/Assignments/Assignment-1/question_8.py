def check_sentence(string):
    res = [[],[]]
    count = 0

    end_str, no_space ,no_upper = False, False, False

    for i in string:
        if(i.isupper()):
            count += 1

    string_split = string.split(' ')

    if '' in string_split:
        res[0] = False
        res[1].append("Continuous spaces are not allowed.")
    else:
        no_space = True

    if string[-1] != '.':
        res[0] = False
        res[1].append("Sentence must end with a full-stop.")
    else:
        end_str = True

    if count > 1:
        res[0] = False
        res[1].append("Continuous uppercase characters are not allowed.")
    else:
        no_upper = True

    if no_space and no_upper and end_str:
        res[0] = True
        res[1].append("Your sentence is syntactically correct!")

    return tuple(res)


string = "An important part of my life has been the people who stood by me."
print(check_sentence(string))

string = "AN important part of my life has been the people who stood by me"
print(check_sentence(string))

string = "An important  part of my life has been the people who stood by me  ."
print(check_sentence(string))