#find sum of first nth number for series 1 + 1/4 + 1/7 + 1/10 + 1/13 + ...



def series_sum(n):
    if n==0:
        return "0.00"
    total=0
    for j in range(1,n+1):
          total+= (1/((3*j)-2))
    return f"{total:.2f}"
