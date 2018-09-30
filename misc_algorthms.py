#klutix
#this algorithm was created from a programming challenge to multiply 2 equal length vectors modeling the the equation sigma AiBi where n = 1 and A and B vectors
def f(a1,a2):	
    if len(a1)>=1:
        return a1[0] * a2[0] + f(a1[1:], a2[1:]) 
    return 0