for i in range(1,22) :
    for j in range(1,12) :
        if i%10==1 :
            if j%5==1 :
                print("+ ",end='')
            else:
                print("- ",end='')

        elif j%5==1 :
            if i%2==1 :
                print("|         ",end='')
            else:
                print(" ",end='')
    print()   
        