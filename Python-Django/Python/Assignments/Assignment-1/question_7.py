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

# password = "ABC23"
# print(password_strength(password))

password = "Abcd@1234"
print(password_strength(password))

password = "Abc@1"
print(password_strength(password))

password = "abc12"
print(password_strength(password))

password = "aBcD**#&"
print(password_strength(password))