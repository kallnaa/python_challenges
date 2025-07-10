#Write a function which calculates the average of the numbers in a given array. Note: Empty arrays should return 0.
def find_average(numbers):
   if len(numbers)==0:
    return 0
   avg=0
   sum=0
   for i in numbers:
    sum+=i
    avg=sum/len(numbers)
   return avg
