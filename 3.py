"""
Functions
"""
def foo():           #no return
    print("Hello")
    

def meaning_of():    #with return
    return 35


def sum(x,y):        #function taking some value
    return x+y


#function also can take default argument for example in above function 
# we can declare value of x or y within function
#declaired variable comes after non-declaired variable

#function scope
#if variable declared in function scope it is not available "outside"

foo() #calling function
print(meaning_of())
print(sum(23,21))
