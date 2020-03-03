def checkSentence(string): 
  
    res = []
    
    length = len(string) 
   
    if string[0] < 'A' or string[0] > 'Z': 
        return False
  
    if string[length-1] != '.': 
        return False
   
    prev_state = 0
    curr_state = 0
  
    index = 1
  
    while (string[index]): 
   
        if string[index] >= 'A' and string[index] <= 'Z': 
            curr_state = 0
  
        elif string[index] == ' ': 
            curr_state = 1
  
        elif string[index] >= 'a' and string[index] <= 'z': 
            curr_state = 2
  
        elif string[index] == '.': 
            curr_state = 3
  
        if prev_state == curr_state and curr_state != 2: 
            return False
  
        if prev_state == 2 and curr_state == 0: 
            return False
  
        if curr_state == 3 and prev_state != 1: 
            return True
  
        index += 1
  
        prev_state = curr_state 
  
    return False


string = "An important  part of my life has been the people who stood by me  ."

str_split = string.split(" ")

res = []

if '' in str_split:
    res.append((False,["Two continuous spaces are not allowed."]))
if not string.endswith('.'):
    res.append((False,["the sentence must end with a full stop(.)","Two continuous uppercase characters are not allowed."]))

hasLower = False
hasUpper = False

res = checkSentence(string)

print(res)