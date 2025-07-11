#Given a year, return the century it is in.


def century(year):
   return year//100 if year%100==0 else ((year//100)+1)
