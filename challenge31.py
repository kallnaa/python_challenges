#A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
#because it uses the letters A-Z at least once (case is irrelevant).Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.



def is_pangram(st):
    return all(letter in st.lower() for letter in "abcdefghijklmnopqrstuvwxyz" )

#all() is an in-built function in python that returns true/false for elements in an iterable. 
# for--> letter in st.lower() for letter in "abcdefghijklmnopqrstuvwxyz" we first conduct our for loop through each letter of the whole alphabets older. For eg we start by a, so letter=a
#and then we check -->letter in st.lower() , we had a string input named st which we had turned into lowercase through st.lower() and since our letter=a we check if a is in our string which 
#is true considering our example of "The quick brown box jumps over the lazy dog" and we go on and on for all alphabets, and finally as our true/false results are combined in all() function
#and since all are TRUE then our all() returns true for our output
