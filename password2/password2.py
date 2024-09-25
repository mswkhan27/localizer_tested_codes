import re

def validate_password(p):
    x = True
    print("FIRST")
    if (len(p) < 6 or len(p) > 12):
        print("Not a Valid Password")
        x = False
    else:
        print("SECOND")
        if not re.search("[a-z]", p):
            print("Not a Valid Password")
            x = False
        else:
            if not re.search("[0-9]", p):
                print("Not a Valid Password")
                x = False
            else:
                if not re.search("[A-Z]", p):
                    print("Not a Valid Password")
                    x = False
                else:
                    if re.search("[$#@]", p): #bug
                        print("Not a Valid Password")
                        x = False
                    else:
                        if re.search(r"\s", p):
                            print("Not a Valid Password")
                            x = False
                        else:
                            print("Valid Password")
                            x = False


