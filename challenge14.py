#Remove First and Last Character
#Task: Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.
#Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.



def remove_char(s):
   return s[1:-1] if len(s)>=2 else ""
