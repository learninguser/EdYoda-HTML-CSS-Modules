def checkSentence(string): 
  
    """
    1. Sentence must start with a Uppercase character (e.g. Noun/ I/ We/ He etc.)
    2. There must be spaces between words.
    3. Then the sentence must end with a full stop(.).
    4. Two continuous spaces are not allowed.
    5. Two continuous uppercase characters are not allowed.
    6. However the sentence can end after an uppercase character.
    """
    res = [[],[]]
    
    length = len(string)
   
    if string[0] < 'A' or string[0] > 'Z':
        res[0] = False
        res[1].append("The sentence must start with a Uppercase character")
  
    if string[length - 1] != '.': 
        res[0] = False
        res[1].append("the sentence must end with a full stop(.)")
   
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
  
        if prev_state == curr_state and curr_state != 0:
            res[0] = False
            res[1].append("Two continuous spaces are not allowed.")
  
        if prev_state == 2 and curr_state == 0: 
            res[0] = False
            res[1].append("Two continuous uppercase characters are not allowed.")
  
        if curr_state == 3 and prev_state != 1: 
            res[0] = True

        prev_state = curr_state 

        index += 1

        if index == length:
            break
        
    res[1] = list(set(res[1]))
    return tuple(res)


string = "AN important part of my life has been the people who stood by me"
print(checkSentence(string))