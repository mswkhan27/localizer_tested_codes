import re
def validate_password(p):
    x = False
    print("Now validating password", p)
    print("Now validating password", len(p))
    while x:  
        if (len(p) < 6 or len(p) > 12):
            break
        else:
            print("Length in valid range")
            if not re.search("[a-z]", p):
                break
            else:
                if not re.search("[0-9]", p):
                    break
                else:
                    if not re.search("[A-Z]", p):
                        break
                    else:
                        print("Checking weather or not the password has special characters",p)
                        if re.search("[$#@]", p):  #bug
                            break
                        else:
                            if re.search(r"\s", p):
                                break
                            else:
                                print("Valid Password")
                                x = True
                                break

    if x:
        print("Not a Valid Password")