
def LetterChanges(str):
  change =""
  for letter in str:
    if letter.isalpha():
      if letter.lower() == 'z':
        letter = 'a'
      else:
        #according to ASCII code 
        letter = chr(ord(letter) + 1)  
    if letter in 'aeiou':
      letter = letter.upper()
    change = change + letter
  return change        

print(LetterChanges(input("Enter a phrase:" )))