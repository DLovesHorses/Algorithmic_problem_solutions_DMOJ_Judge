#get password string
password = input()
pass_validity = False

if(len(password) >= 8 and len(password) <= 12):
    lower = 0
    upper = 0
    digit = 0
    invalid = 0

    for i in range(len(password)):
        if(password[i].islower()):
            lower += 1
        elif(password[i].isupper()):
            upper += 1
        elif(password[i].isdigit()):
            digit += 1
        else:
            invalid += 1


    if (lower >= 3 and upper >= 2 and digit >= 1 and invalid == 0):
        pass_validity = True
    else:
        pass_validity = False


if(pass_validity == True):
    print('Valid')
else:
    print('Invalid')