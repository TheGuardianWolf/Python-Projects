def cShift(M,S):
    new=""
    for l in M:
        if l.isalpha() == True:
            if l.isupper() == True:
                translate = ord(l)+S
                if translate > 90:
                    translate = translate-26
                new+=chr(translate)
            elif l.islower() == True:
                translate = ord(l)+S
                if translate > 122:
                    translate = translate-26
                new += chr(translate)
        else:
            new += l
    return new
print("Sentence to Encode then Shift Value")
print(cShift("'"+str(input())+"'",int(input())))
