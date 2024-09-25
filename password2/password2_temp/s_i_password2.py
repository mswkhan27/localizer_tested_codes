c[13] += 1
if len(p) < 6 or len(p) > 12:
    c[1] += 1
    print("Not a Valid Password")
else:
    c[2] += 1
    print("SECOND")
    if not re.search("[a-z]", p):
        c[3] += 1
        print("Not a Valid Password")
    else:
        c[4] += 1
        if not re.search("[0-9]", p):
            c[5] += 1
            print("Not a Valid Password")
        else:
            c[6] += 1
            if not re.search("[A-Z]", p):
                c[7] += 1
                print("Not a Valid Password")
            else:
                c[8] += 1
                if re.search("[$#@]", p): #bug
                    c[9] += 1
                    print("Not a Valid Password")
                else:
                    c[10] += 1
                    if re.search(r"\s", p):
                        c[11] += 1
                        print("Not a Valid Password")
                    else:
                        c[12] += 1
                        print("Valid Password")
