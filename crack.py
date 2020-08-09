mode=int(input("Codes: "))

while True:
    c=input("Code: ")
    if mode == 2:
        o=input("Code: ")
        nn={"N":"N", "C":"C", "H":"H"}
        for jj in range(8):
            if c[jj] == "N" or c[jj] == "H" or c[jj] == "C":
                if o[jj].isnumeric():
                    nn[c[jj]]=o[jj]
            if o[jj] == "N" or o[jj] == "H" or o[jj] == "C":
                if c[jj].isnumeric():
                    nn[o[jj]]=c[jj]
        c=c.replace("N", nn["N"])
        c=c.replace("C", nn["C"])
        c=c.replace("H", nn["H"])

        b=["0","1","2","3","4","5","6","7","8","9"]

        if nn["N"]== "N":
            for jjg in b:
                print(c.replace("N", jjg))
        elif nn["C"] == "C":
            for jjg in b:
                print(c.replace("C", jjg))
        elif nn["H"] == "H":
            for jjg in b:
                print(c.replace("H", jjg))
                
    elif mode == 1:
        b=["0","1","2","3","4","5","6","7","8","9"]
        for i in b:
            g=c.replace("C", i)
            l=b.copy()
            l.remove(i)
            for j in l:
                f=g.replace("N", j)
                p=l.copy()
                p.remove(j)
                for z in p:
                    d=f.replace("H", z)
                    print(d)
    else:
        print("No")

