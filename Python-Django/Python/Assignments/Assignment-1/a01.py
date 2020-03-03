# don't change any function name write you all code inside the function only for every question solution and return you output as mentioned in problem statement.

def question_first_solution(input_seq):
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
            decoded += possibilites[diff]
        else:
            decoded += possibilites[len(split_text[idx].strip()) - 1]
    
    return decoded

def question_second_solution(tickets):
    def travel_sequence(travel_trip):

        keys = set(travel_trip.keys())
        values = set(travel_trip.values())

        diff_values = keys.symmetric_difference(values)

        for idx in diff_values:
            if idx not in keys:
                end_trip = idx
            else:
                start_trip = idx

        start = True
        trip = {}

        while start:
            city = travel_trip[start_trip]
            trip[start_trip] = city
            if city == end_trip:
                start = False
            else:
                start_trip = travel_trip[start_trip]

        return trip
    travel_sequence(tickets)

def question_third_solution(states):
    # Write your code here
    cities = list(states.values())

    output = {}
    flat_list = []

    for sublist in cities:
        for item in sublist:
            flat_list.append(item)

    flat_list = set(flat_list)

    for idx in flat_list:
        output.setdefault(idx, [])

    tempVar = list(states.items())

    for value in tempVar:
        for val in value[1]:
            if val in output:
                output[val].append(value[0])
    return output

def question_fourth_solution(brackets):
    open_tup = tuple('({[') 
    close_tup = tuple(')}]') 
    map = dict(zip(open_tup, close_tup)) 
    queue = [] 
  
    for i in brackets: 
        if i in open_tup: 
            queue.append(map[i]) 
        elif i in close_tup: 
            if not queue or i != queue.pop(): 
                return False
    return True

def question_fifth_solution(number): # need to work on this
    # Write your code here
    given_int = number

    if given_int == 1:
        roman = 'I'
    elif given_int == 2:
        roman = "II"
    elif given_int == 3:
        roman = "III"
    elif given_int == 4:
        roman = "IV"
    elif given_int == 5:
        roman = "V"
    elif given_int == 6:
        roman = "VI"
    elif given_int == 7:
        roman = "VII"
    elif given_int == 8:
        roman = "VIII"
    elif given_int == 9:
        roman = "IX"
    return roman

def question_sixth_solution(code): 
    count = 0
    str_split = code.split('\n')
    for value in str_split:
        if value == '' or value.startswith('#'):
            continue
        else:
            count += 1
    return count

def question_seventh_solution(string): # not yet complete

    def password_strength(password):
    
        special_chars = ('!','@','#','$','&')

        hasLower = False
        hasUpper = False
        hasDigit = False
        specialChar = False
        
        res = []
        count = 0

        for idx in password:
            if idx.islower():
                hasLower = True
                continue

            if idx.isupper():
                hasUpper = True
                continue

            if idx.isdigit():
                hasDigit = True
                continue

            if idx in special_chars:
                specialChar = True
            else:
                count += 1
        
        if count > 0:
            specialChar = False

        # if len(password) < 8:
        #     if hasLower and hasUpper and hasDigit and specialChar:
        #         res.extend(["InValid",["The length of the password must be at least 8 characters in length"]])
        #     else:
        #         res.extend(["InValid",["The length of the password must be at least 8 characters in length","The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)","The password must contain at least 1 capital letter"]])
        #     return res

        if len(password) < 8:
            return ("InValid",['The length of the password must be at least 8 characters in length'])

        if hasLower and hasUpper and hasDigit and specialChar:
            res.extend(['Valid',[]])

        elif hasLower and hasDigit:
            res.extend(["InValid",["The length of the password must be at least 8 characters in length","The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)","The password must contain at least 1 capital letter"]])

        elif not specialChar and not hasDigit:
            res.extend(["InValid",["The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)","The password must contain at least 1 digit"]])

        return res

    password_strength(string)

def question_eighth_solution(string):
    # Write your code here
    pass

def question_ninth_solution(arr, k):
    def findSubarray(a, k, n): 
        vec=[] 
        for i in range(n-k+1): 
            temp=[] 
            for j in range(i,i+k): 
                temp.append(a[j]) 
            vec.append(temp) 
    
        vec=sorted(vec) 
    
        return vec[len(vec) - 1]
    
    return findSubarray(list(arr), k, len(arr))


def question_tenth_solution(nums):
    # Write your code here
    pass