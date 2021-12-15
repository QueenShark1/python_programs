#def rollvalid():
#   r = input("Enter your valid roll number : ")
#    while True:
#        if len(r) == 3:
#            return r
#            break
#        else:
#           r = input("Enter your three digit roll number : ")
#            continue

def rollvalid():
    r = input("enter your valid roll number : ")
    while true:
        if len(r) == 3:
            return r 
            break
        else:
            r = input("enter your threee digit roll number : ")
            continue


def name():
    while True:
        name = input("Enter your full name : ")
        if len(name) >= 3:
            return name
            break
        else:
            print("Name must have atleast three character ")
            name = input("Renter your full name : ")
            continue


def Class():
    cl = int(input("Enter your Class : "))
    while True:
        if cl > 0 and cl <= 12:
            return str(cl)
            break
        else:
            cl = int(input("Enter your Class : "))
            continue


def section():
    sec = input("Enter your section : ")
    while True:
        if sec.isalpha() == True and len(sec) == 1:
            return sec.upper()
            break
        else:
            sec = input("Enter your section : ")
            continue


def dob():
    def dd():
        d = int(input("Enter your birth Date : "))
        while True:
            if d > 0 and d <= 31:
                return str(d)
                break
            else:
                d = int(input("Renter your birth Date : "))
                continue

    def mm():
        m = int(input("Enter your birth Month : "))
        while True:
            if m > 0 and m <= 12:
                return str(m)
                break
            else:
                m = int(input("Renter your birth Month : "))
                continue

    def yy():
        y = int(input("Enter your birth Year : "))
        while True:
            if y > 1990 and y < 3000:
                return str(y)
                break
            else:
                d = int(input("Renter your birth Year : "))
                continue
    return dd()+"/"+mm()+"/"+yy()


def pm():
    while True:
        p = input("Enter your physics marks : ")
        if len(p) == 2 and int(p) >= 0 and int(p) < 100:
            return p
        else:
            p = input("Renter your physics marks : ")
            continue


def cm():
    while True:
        c = input("Enter your chemistry marks : ")
        if len(c) == 2 and int(c) >= 0 and int(c) < 100:
            return c
        else:
            c = input("Renter your chemistry marks : ")
            continue


def mm():
    while True:
        m = input("Enter your mathematics marks : ")
        if len(m) == 2 and int(m) >= 0 and int(m) < 100:
            return m
        else:
            m = input("Renter your mathematics marks : ")
            continue


def em():
    while True:
        e = input("Enter your english marks : ")
        if len(e) == 2 and int(e) >= 0 and int(e) < 100:
            return e
        else:
            e = input("Renter your english marks : ")
            continue


def hm():
    while True:
        h = input("Enter your hindi marks : ")
        if len(h) == 2 and int(h) >= 0 and int(h) < 100:
            return h
        else:
            h = input("Renter your hindi marks : ")
            continue


n = int(input("how many record you want to enter : "))
i = 1
while i <= n:
    f = open("marksheet.txt", "a")
    f.write(rollvalid())
    f.write(name()+"\n")
    cl= Class()
    se=section()
    DOB = dob()
    f.write(se)
    f.write(cl+"\n")
    f.write(DOB+"\n")
    f.write(pm())
    f.write(cm())
    f.write(mm())
    f.write(em())
    f.write(hm()+"\n")
    f.close()
    i += 1
