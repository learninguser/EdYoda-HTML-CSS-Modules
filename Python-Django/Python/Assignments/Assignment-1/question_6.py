def question_sixth_solution(code):
    count = 0
    str_split = code.split('\n')
    for value in str_split:
        if value == '' or value.startswith('#'):
            continue
        else:
            count += 1
    return count

code = """
#Linear search implementation
#Takes list and a key as input and returns True or False as answer
'''Time complexity is O(n)'''

@classmethod
def linear_search(l,key):
    for value in l:
        if key == value:
            return True #Return True is key exist
    else:
        return False #Return False if key does not exist


l = [100,200,300,400,500,600]
key = 500
result = linear_search(l,key)


print(result)
"""

print(question_sixth_solution(code))