#Edited by Joseph Hutchens


def import_dictionary():
    dictionary = []
    try:
        file = open("dictionary.txt", "r")#location of your dictionary or provided wordlist
        fileContents = file.readlines() #read text file and store each new line as a string
    finally:
        file.close()
    for i in range(len(fileContents)):
        dictionary.extend(fileContents[i].split()) #changes the list by removing \n's from line breaks in text file
    return dictionary

def import_scrambled_words():
    scrambledWords = []
    try:
        file = open("scrambled-words.txt", "r") #location of your scrambled word file
        fileContents = file.readlines() #read text file and store each new line as a string
    finally:
        file.close()
    for i in range(len(fileContents)):
        scrambledWords.extend(fileContents[i].split()) #changes the list by removing \n's from line breaks in text file
    return scrambledWords

def unscramble_word(scrambledWord):
    countToMatch = len(scrambledWord)
    matchedWords = []
    string = ""

    for word in dictionary:
        count = 0
        for x in scrambledWord:
            if x in word:
                count += 1
            if count == countToMatch:
                matchedWords.append(word)
                break
    for matchedWord in matchedWords:
        if len(matchedWord) == len(scrambledWord):
            print(matchedWord)
            string = matchedWord
            break #this returns only one unscrambles word
    return string

if __name__ == '__main__':
    finalString = ""
    try:
        scrambled = import_scrambled_words()
        print(scrambled)
        dictionary = import_dictionary()
        for x in scrambled:
            finalString += unscramble_word(x)
            finalString +=", "
        len(finalString)

        print(finalString)

    except Exception as e:
        print(e)
