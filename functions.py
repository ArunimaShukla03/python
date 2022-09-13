phrase = "Random Phrase"

#simply printing
print(phrase)

#changing into lowercase
print(phrase.lower())

#changing into uppercase
print(phrase.upper())

#check if string is upper or not
print(phrase.isupper())

#continuous functions
print(phrase.upper().isupper())

#accessing the elements of a string
print(phrase[0])

#knowing the length of the string
print(len(phrase))

#knowing the index of a character
print(phrase.index("P"))
print(phrase.index("Rand"))

#replacing characters in a string
print(phrase.replace("Random","Specific"))