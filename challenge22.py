#training on mumbling in python. if input is abcd output should A-Bb-Ccc-Dddd

def accum(st):
   result2=[]
   for i,item in enumerate(st):
        result1= item.upper()+item.lower()*(i)
        result2.append(result1)
   return "-".join(result2)
