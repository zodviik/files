#Учитывая целое число x, вернуть, true если x это палиндром, и false в противном случае .
def Palindrome( x: int) -> bool:

    if str(x) == str(x)[::-1]:
        return True
    else:
        return False
