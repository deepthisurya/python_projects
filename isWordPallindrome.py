#Check if the word given by the user is Pallindrome or not
#A pallindrome reads the same from start and end , eg LOL ABBA

#Get the word from the user


#Reverse the word using [::-1] - Slicing and compare  using ==
def check_pallindrome(theWord):
    #print(theWord[::-1])
    first_word = theWord
    rever_word = theWord[::-1]
    #print(first_word,rever_word)
    if (first_word == rever_word):
        return"Yes! , Its a Pallindrome!"
    else:
        return"Normal word, Bro!"

#Take user input

def getWord():
    theWord = input("Give the word you want to check , if Pallindrome!  - ")
    #print(theWord)
    print(check_pallindrome(theWord))

#Main Function
if __name__ == '__main__':
    getWord()