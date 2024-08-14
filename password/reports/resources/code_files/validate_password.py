def validate_password(p):
    if (len(p) < 6 or len(p) > 12):
        return "The password is not within the required length range, so it fails."
    else:
        if not re.search("[a-z]", p):
            return "The password does not contain at least one lowercase letter, so it fails." 
        else:
            if not re.search("[0-9]", p):
                return "The password does not contain at least one number, so it fails."  
            else:
                if not re.search("[A-Z]", p):
                    return "The password does not contain at least one uppercase letter, so it fails."  
                else:
                    if re.search("[$#@]", p): #bug: if not re.search("[$#@]", p): , instead of this
                        return "The password does not contain at least one special character, so it fails."   
                    else:
                        if re.search(r"\s", p):
                            return "The password contains spaces, so it fails."   
                        else:
                            return "The password is valid!"
