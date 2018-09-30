##Programming Challenge:
##    Numbers can be expressed as stairs.
##    
##    **
##    ***
##    ****
##    *****
##    ******
##
##     = 20

##    some numbers expressed can be expressed in multiple ways

##
##    **
##    ***
##    ****
##    *****
##    ******
##    *******
##
##    ********
##    *********
##    **********
##
##    *************
##    **************
##
##    = 27

##    Build an solution thats accepts an integer
##    and builds all stair possibilities for a given number.




def build_all_stairs(n):
    s = []
    for x in range(1,n):
        for z in range(1,n):
            a = sum(range(x,z+1))
            s.append(list(range (x,z+1))) if a == n else 0
    for e in s:
       for p in e:
           print("*"*p)
       print("")
    print(" = " +str(n))
    
#example  use   
#build_all_stairs(27)

