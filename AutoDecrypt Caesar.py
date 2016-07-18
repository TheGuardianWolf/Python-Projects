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

def sentenceGoodness(M):
    letterGoodness = [.0817,.0149,.0278,.0425,.1270,.0223,.0202,.0609,.0697,.0015,.0077,.0402,.0241,.0675,.0751,.0193,.0009,.0599,.0633,.0906,.0276,.0098,.0236,.0015,.0197,.0007]
    goodnessarray = []
    check=0.0
    for x in range(1,27):
        goodness = 0.0
        decrypt = uShift(M,x)
        for c in decrypt:
            if c.isalpha() == True:
                c = c.upper()
                d = ord(c) - 65
                goodness += letterGoodness[d]
        goodnessarray.append(goodness)
        e=max(goodnessarray)
    return goodnessarray.index(e)

def autodecrypt(M):
    print("Giving best decryption based on deliciousness")
    x=sentenceGoodness(M)+1
    print("shift="+str(x))
    print("message="+str(uShift( M,x)))

print("sentence to decode")
autodecrypt(input())
