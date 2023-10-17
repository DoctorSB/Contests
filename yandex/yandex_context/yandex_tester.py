result = int(input())
interactor = int(input())
cheker = int(input())
if interactor == 0:
    if result != interactor:
        print(3)
    else:
        print(cheker)
elif interactor == 1:
    print(cheker)
elif interactor == 4:
    if result != 0:
        print(3)
    else:
        print(4)
elif interactor == 6:
    print(0)
elif interactor == 7:
    print(1)
else:
    print(interactor)
