#program returns number of vowels in a sentence

def get_count(sentence):
    vowels="aieou"
    count=0
    for letter in sentence:
        if letter in vowels:
                count+=1
    return count
