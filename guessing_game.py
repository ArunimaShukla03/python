from re import T


secret_word = "sickness"
guess = " "
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess!=secret_word and not(out_of_guesses):
  if guess_count < guess_limit:
   guess = input("Guess the word: ")
   guess_count += 1
  else:
    out_of_guesses = True

if out_of_guesses:
  print("You are out of guesses, you lose :(")
else:
  print("You win!")