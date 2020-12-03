code=input("Code: ")
nn={"N":"N", "C":"C", "H":"H"}

def crack(a, b, c):
    nms=["0","1","2","3","4","5","6","7","8","9"]
    for i in nms:
        g=c.replace(a, i)
        l=nms.copy()
        l.remove(i)
        for j in l:
            f=g.replace(b, j)
            print(c, "   ", a, "=", i, " ", b, "=", j)
            print(f)
        

if code.find("C") == -1:
    crack("N", "H", code)
elif code.find("N") == -1:
    crack("C", "H", code)
else:
    crack("C", "N", code)

