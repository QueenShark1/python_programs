def rno():
    while True:
        rno = input("Enter your three digit roll number : ")
        if len(rno) == 3:
            return int(rno)
            break
        else:
            rno = input("Renter your three digit roll number : ")
            continue


k = rno()
f = open("marksheet.txt", "r")
while True:
    r = int(f.read(3))
    if r == k:
        print()
        print("\tSubhash Higher Secondary School For Excellence")
        print("\t\t\t ANNUAL REPORT ")
        print("\tRoll number : ", r, "\t Name : ", f.readline())
        sec = f.read(1)
        cl = f.readline()
        print("\tClass   : ", cl,"\tSection : ", sec)
        print("\tDate of Birth : ", f.readline())
        print("\tSubject \tMarks")
        p = int(f.read(2))
        print("\tPhysics    \t", p)
        c = int(f.read(2))
        print("\tChemistry  \t", c)
        m = int(f.read(2))
        print("\tMathematics \t", m)
        e = int(f.read(2))
        print("\tEnglish    \t", e)
        h = int(f.read(2))
        print("\tHindi      \t", h)

        per = (p+c+m+e+h)/5
        print("\n\tPercentage\t", per)
        if per < 34:
            print("\tDivision    \tFAIL")
        elif per < 45:
            print("\tDivision    \tTHIRD")
        elif per < 60:
            print("\tDivision    \tSECOND")
        else:
            print("\tDivision\t FIRST")
        break
    else:
        f.readline()
        f.readline()
        f.readline()
        f.readline()
        continue
