from src.utils import Count 

def validate_password(p):
    Count.incC(13)
    if len(p) < 6 or len(p) > 12:
        Count.incC(1)
        print("Not a Valid Password")
    else:
        Count.incC(2)
        print("SECOND")
        if not re.search("[a-z]", p):
            Count.incC(3)
            print("Not a Valid Password")
        else:
            Count.incC(4)
            if not re.search("[0-9]", p):
                Count.incC(5)
                print("Not a Valid Password")
            else:
                Count.incC(6)
                if not re.search("[A-Z]", p):
                    Count.incC(7)
                    print("Not a Valid Password")
                else:
                    Count.incC(8)
                    if re.search("[$#@]", p): #bug
                        Count.incC(9)
                        print("Not a Valid Password")
                    else:
                        Count.incC(10)
                        if re.search(r"\s", p):
                            Count.incC(11)
                            print("Not a Valid Password")
                        else:
                            Count.incC(12)
                            print("Valid Password")
