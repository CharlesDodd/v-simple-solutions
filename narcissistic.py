def narcissistic( value ):
    s = str(value)
    sums = 0
    for i in range(len(s)):
        sums += int(s[i])**len(s)
    if sums == value:
        return True
    else:
        return False

print(narcissistic(153))