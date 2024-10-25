#program to swap two number without using third varieable
def swap1(a, b):
    #code to swap a and b
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print("after swaping...a = ", a, "b = ...", b)
def swap2(a , b):
    a = (a & b) + (a | b) 
    b = a + (~ b) + 1
    a = a + (~ b) + 1
    print("AFTER SWAPPING A =....", a, "B=....", b)
swap1(11, 12)
swap2(13, 14)