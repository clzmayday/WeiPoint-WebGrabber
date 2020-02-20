import os, unibham, bcu
run = True

while run:
    print("Please Enter a selection and Push Enter:")
    print("1. University of Birmingham")
    print("2. Birmingham City College")
    print("0. Exit")
    selection = int(input())
    if selection == 0:
        run = False
        os._exit(0)
    elif(selection == 1):
        executor = unibham.unibham()
        executor.run()
    elif(selection == 2):
        executor = bcu.bcu()
        executor.run()


    else:
        print("Wrong Input! please Enter correct selection")

    print("=============================")
