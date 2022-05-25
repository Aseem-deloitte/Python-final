import sys

d = {}
e = {}
l = []
while True:
    def admin():
        print("**********Welcome Admin**************")
        print("1:Add new movie info")
        print("2:Edit movie title")
        print("3:Delete movies")
        print("4:Logout")
        adminchoice = int(input("Enter the choise: "))
        if adminchoice == 1:
            j = input("Enter movie name: ")
            e[j] = [i for i in input("Enter genre,length,cast,director,rating,language,showtiming,capacity\n").split()]
            print(e)

        if adminchoice == 2:
            s = input("Enter the title to be edited: ")
            t = input("Enter the correct title: ")
            e[t] = e[s]
            del e[s]
            print(e)

        if adminchoice == 3:
            u = input("Enter the movie to be deleted: ")
            del e[u];
            print(e)

        if adminchoice == 4:
            print("*********Logout Sucessfull*************")
            sys.exit()


    def user():
        print("welcome {}".format(userid))
        l = 1
        p = []
        for k in e:
            print("{} : {}".format(l, k))
            p.append(k)
            l += 1
        f = int(input("Enter Movie: "))
        h = p[f - 1]
        for b in e[h]:
            print(b)

        print("1.Book Ticket")
        print("2.Cancel Ticket")
        y = int(input("your choice...: "))
        if y == 1:
            print("Timings: ")
            t = 1
            for o in range(6, 9):
                print("{} : {}".format(t, e[h][o]))
                t += 1
            z = int(input("select timing: "))
            if z == 1:
                print("Timing: {}".format(e[h][6]))
            if z == 2:
                print("Timing: {}".format(e[h][7]))
            if z == 3:
                print("Timing: {}".format(e[h][8]))

            print("Remaining seats: {}".format(e[h][9]))

            seats = int(input("Enter the number of seats: "))
            c = int(e[h][9]) - seats
            print("Remaining seats: {}".format(c))

            print("Thanks for booking..........")

        if y == 2:
            cancel = int(input("Number of seats to be cancelled: "))
            print("Thank you book again..........")


    print("*****************Welcome To Book My Show****************************")
    print("1:Login")
    print("2:Register new account")
    print("3:Exit")
    flag = 0
    choice = int(input("Enter your choice: "))
    if choice == 1:
        userid = input("Enter user name: ")
        password = input("enter the password: ")
        if userid == "admin@123" and password == "myapp":
            admin()
        else:
            for i in d:
                if d[i] == password:
                    flag = 1
            if flag == 1:
                user()
            else:
                print("Enter correct username and password")
                print("if you are a new user then please register")

    if choice == 2:
        print("*****************Create new Account******************")
        x = input("Enter name: ")
        email = input("Enter emailid: ")
        phone = input("Enter phone number: ")
        age = input("enter the age: ")
        y = input("Create a password: ")
        d[x] = y
        print("***Account created***")

    if choice == 3:
        sys.exit()