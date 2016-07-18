def uShift(M,S):
    new=""
    for l in M:
        if l.isalpha() == True:
            if l.isupper() == True:
                translate = ord(l)-S
                if translate < 65:
                    translate = translate+26
                new+=chr(translate)
            elif l.islower() == True:
                translate = ord(l)-S
                if translate < 97:
                    translate = translate+26
                new += chr(translate)
        else:
            new += l
    return new
