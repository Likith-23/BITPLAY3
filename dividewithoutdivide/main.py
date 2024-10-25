#program to divde two numbers without division operator
def divide_nums(ourdivident, ourdivisor):
    sign = (-1 if((ourdivident < 0) ^ (ourdivisor < 0))else 1 )#check if divisor is positive or negative
    #make both positive
    ourdivdent = abs(ourdivident)
    ourdivisor = abs(ourdivisor)
    q = 0
    temp = 0
    #go from 31 to 0 and accumulate all 0 bits   
    for i in range(31, -1, -1):
        if (temp +(ourdivisor << i)<= ourdivdent):
            temp += ourdivisor << i
            q |= 1 << i
    #assuming the sign value computed earlier is -1 , negate the quotient value
    if sign == -1:
        q =-q
    return q
a = int(input("ENTER A FOR A/B........."))
b = int(input("ENTER B FOR A/B..."))
print("RESULT OF ", a , "/", b, "is", divide_nums(a, b))