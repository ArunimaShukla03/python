# A language where a language is converted into another language, i.e., here vowels are converted into the letter "g"

def translate(phrase):
  translation = " "
  for letter in phrase:
    if letter in "AEIOUaeiou":
      translation += "g"
    else:
      translation += letter
  return translation

print(translate(input("enter a phrase: ")))

# better translator

def translate(phrase):
  translation = " "
  for letter in phrase:
    if letter in "AEIOUaeiou":
      if letter.isupper():
        translation += "G"
      else:
        translation += "g"
    else:
      translation += letter
  return translation

print(translate(input("enter a phrase: ")))

    