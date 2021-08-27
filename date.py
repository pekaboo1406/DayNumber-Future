class Execute:
    month = ['', 'JAN ', 'FEB ', 'MARCH ', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER',
             'NOVEMBER ', 'DECEMBER ']
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0, 0]

    def __init__(self, dn, year, n, name, password):
        self.dn = dn
        self.year = year
        self.n = n
        self.name = name
        self.password = password

    def input(self):

        while True:
            try:

                self.name = (input("NAME = "))
                self.dn = int(input("DAY NUMBER = "))
                self.year = int(input("YEAR = "))
                self.n = int(input("N = "))
                self.password = input("ENTER THE PASSWORD TO PROTECT YOUR DATA = ")

            except:
                print(" ERROR OCCURRED IN INPUT FORMATS. TRY AGAIN! ")
                print()
                print()

            else:
                if 1 <= self.dn <= 366 and 1 <= self.n <= 100 and len(str(self.year)) == 4:
                    break
                else:
                    print("INVALID INPUT. TRY AGAIN")
                    print()
                    print()

    def display_write(self, dd, mm, yy):

        with open("demofile.txt", mode='a') as f:
            f.write("\n")

            if dd == 1 or dd == 21 or dd == 31:
                print(dd, " ST ", end=" ")
                f.write(str(dd) + " ST ")
            elif dd == 2 or dd == 22:
                print(dd, " ND ", end=" ")
                f.write(str(dd) + " ND ")
            elif dd == 3 or dd == 23:
                print(dd, " RD ", end=" ")
                f.write(str(dd) + " RD ")
            else:
                print(dd, " TH ", end=" ")
                f.write(str(dd) + " TH ")

            print(self.month[mm], " , ", yy, end="")
            f.write(self.month[mm] + " , " + str(yy))

    def view_data(self, x):
        if x == self.password:
            print("PASSWORD MATCHED. LOADING DATA....")
            with open("demofile.txt", 'r') as f:
                f.read()

        else:
            print(" SORRY YOU DON'T HAVE THE CORRECT PASSWORD TO VIEW THE DATA STORED ")

    def Calc(self, x):

        dn = x
        ctr = 1

        if dn > 366:
            dn = dn - sum(self.days)
            self.year += 1

        if self.year % 400 == 0 or (self.year % 4 == 0 and self.year % 100 != 0):
            self.days[2] = 29

        while dn > self.days[ctr]:
            dn = dn - self.days[ctr]
            ctr += 1

        return dn, ctr, self.year

    def main(self):



        self.input()

        print(self.name, ' : ')
        print()

        dd, mm, yy = self.Calc(self.dn)

        print("DATE : ", end="")

        self.display_write(dd, mm, yy)
        print()

        self.dn += self.n
        dd, mm, yy = self.Calc(self.dn)
        print("DATE AFTER N DAYS : ", end="")
        self.display_write(dd, mm, yy)

        print()
        print()

        result = int(input("DO YOU WANT TO VIEW THE STORED DATA ? ENTER 1 FOR YES 0 FOR NO "))

        if result == 1:
            p = input(" ENTER THE PASSWORD : ")

            self.view_data(p)

        else:
            print("THANK YOU FOR USING THE PROGRAM ")


User = Execute(dn=0, year=0, n=0, password="", name="")
User.main()
