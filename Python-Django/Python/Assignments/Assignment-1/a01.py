# don't change any function name write you all code inside the function only for every question solution and return you output as mentioned in problem statement.

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

def question_second_solution(tickets): # complete but test cases are incorrect
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
    return travel_sequence(tickets)

def question_third_solution(states): # complete
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

def question_fourth_solution(brackets): # complete
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

def question_fifth_solution(number): # complete
    # Write your code here
    def int_roman(num):
        val = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]

        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    return int_roman(number)

def question_sixth_solution(code): # complete
    def question_six(code):
        count = 0
        str_split = code.split('\n')
        for value in str_split:
            if value == '' or value.startswith('#'):
                continue
            else:
                count += 1
        return count
    return question_six(code)

def question_seventh_solution(string): # complete but test cases are incorrect

    def password_strength(password):
    
        special_chars = ('!','@','#','$','&')

        hasLower = False
        hasUpper = False
        hasDigit = False
        specialChar = False
        
        res = [[],[]]
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

        if len(password) < 8:
            if hasLower and hasUpper and hasDigit and specialChar:
                res[0] = "InValid"
                res[1].append("The length of the password must be at least 8 characters in length")
            else:
                res[0] = "InValid"
                res[1].append("The length of the password must be at least 8 characters in length")
                if not specialChar:
                    res[1].append("The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)")
                if not hasUpper:
                    res[1].append("The password must contain at least 1 capital letter")
                if not hasLower:
                    res[1].append("The password must contain at least 1 lower case letter")
                if not hasDigit:
                    res[1].append("The password must contain at least 1 digit")
            return tuple(res)

        # if len(password) < 8:
        #     return (["InValid",["The length of the password must be at least 8 characters in length"]])

        elif hasLower and hasUpper and hasDigit and specialChar:
            res[0] = "Valid"

        else:
            res[0] = "InValid"
            if not specialChar:
                res[1].append("The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)")
            if not hasUpper:
                res[1].append("The password must contain at least 1 capital letter")
            if not hasLower:
                res[1].append("The password must contain at least 1 lower case letter")
            if not hasDigit:
                res[1].append("The password must contain at least 1 digit")
        
        return tuple(res)

    password_strength(string)

def question_eighth_solution(string): # complete

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

    return check_sentence(string)

def question_ninth_solution(arr, k): # complete but test cases are incorrect
    def findSubarray(a, k): 
        vec=[] 
        for i in range(len(a) - k + 1): 
            temp=[] 
            for j in range(i, i + k): 
                temp.append(a[j]) 
            vec.append(temp)  
        
        ans = vec[0]
        
        for idx in range(1, len(vec)):
            if vec[idx] > ans:
                ans = vec[idx]
        
        return ans

    return findSubarray(list(arr), k)

def question_tenth_solution(nums): # complete
    def adj_sum_even(arr):
        even_copy = arr.copy()
        odd_copy = arr.copy()

        even_count = 0
        odd_count = 0

        for s in arr:
            if s % 2 == 0: 
                even_copy.remove(s)
                even_count += 1
            else:
                odd_copy.remove(s)
                odd_count += 1

        if even_count > odd_count:
            count = odd_count
            ans = odd_copy
        else:
            count = even_count
            ans = even_copy
        return (count, ans)

    return (adj_sum_even(nums))