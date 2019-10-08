#klutix
#this algorithm was created from a programming challenge to multiply 2 equal length vectors modeling the the equation sigma AiBi where n = 1 and A and B vectors
def f(a1,a2):	
    if len(a1)>=1:
        return a1[0] * a2[0] + f(a1[1:], a2[1:]) 
    return 0


#klutix programming challenge
#Finish this function
#First_occurence(string,stringtofind)
# return the index of the first occurence of a given string in a string
# NO LOOPS ALLOWED

def first_occ(Str, strtofind):	
   def loop(Str,strtofind, b = 0):     
       if Str == "":
          return False
       if Str[:len(strtofind)] == strtofind:
            return b
       return loop(Str[len(strtofind)-1:], strtofind, b + len(strtofind)-1)             
   a = loop(Str,strtofind)
   if a >= 1:
   	return a
   return -1
