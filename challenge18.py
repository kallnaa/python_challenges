#Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
#Note: input will never be an empty string

def fake_bin(x):
    available=['1','2','3','4','5','6','7','8','9']
    result=x
    for item in available:
        if int(item)<5:
           result=result.replace(item,"0")
        elif int(item)>=5:
           result=result.replace(item,"1")
    return result
