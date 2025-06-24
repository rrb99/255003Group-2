#returns the absolute value of any number.
def abs_value(num):
    #if num is less than zero (negative) it gets multiplied by -1 to make it positive
    if num < 0:
        return -num
    # if num already positive it stays the same
    else:
        return num
    
#works with decimals and integers (example using -66.7 below)
print(abs_value(-66.7))
    