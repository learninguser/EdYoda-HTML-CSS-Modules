
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
        return (["InValid",["The length of the password must be at least 8 characters in length"]])

    if hasLower and hasUpper and hasDigit and specialChar:
        res.extend(['Valid',[]])

    elif hasLower and hasDigit:
        res.extend(["InValid",["The length of the password must be at least 8 characters in length","The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)","The password must contain at least 1 capital letter"]])

    elif not specialChar and not hasDigit:
        res.extend(["InValid",["The password must contain at least 1 special character and allowed special characters are (!,@,#,$,&)","The password must contain at least 1 digit"]])

    return res

password = "ABC23"
print(password_strength(password))

# password = "Abc@1"
# print(password_strength(password))

# password = "abc12"
# print(password_strength(password))

# password = "aBcD**#&"
# print(password_strength(password))