# EXERCISE ONE - YOUR NAME, YOUR CIPHER
# TASK Exercise 1 — Your Name, Your Cipher
# Topics: Strings · Variables · Loops
#
# Store your full name in a variable. Write a program that shifts every letter forward by the number of characters in your
# first name (wrapping Z → A). Print the encrypted version, then write the reverse function to decrypt it back.







# EXERCISE  - YOUR NAME, YOUR CIPHER
# full_name= "Emmanuel Boniface"
full_name = input("Enter your full name: ")
#Since the first name has a role to play, we extract it from te full name and assign it to a new variable
first_name= full_name.split()[0] #.split function will group each word seperated by spaces in the string above into single strings
# as long as they are .then [0] is index, ofcourse
# to shift items by length of first name, we'll calculate the length to know and
# assign the shift value
shift =len(first_name)#this assigns the length of the first name to the variable "shift"
# we create empty strings to hold our results
encrypted_name = ""
decrypted_name = ""
# ENCRYPTION BELOW
#For each character in first name,
for char in first_name:
 # The code below checks for Upper cases that may be in first name.
 if "A" <= char <= "Z":
  """instead of counting the normal ascii A:65,Z90, a97 etc, the code below brings (the alphabets) down to 0-25 scale, 
  shift it by applying our shift value, wrap it(making sure to continues
  from A whenever it reaches Z), and restore it to make sure it runs for other alphabets""" # (ord(char)) collects the alphabets, and renders their ascii values to the computer. he
  shifted_ascii = ((ord(char) - 65 + shift) % 26) + 65
  # THE CODE BELOW CONVERTS THE ASCII COODE BACK INTO LETTERS. AND ASSIGNS IT TO THE VARIABLE enc... below
  encrypted_name += chr(shifted_ascii)
 # The code below does the same thing but for lowercase items in my first name.
 elif "a" <= char <= "z":
  shifted_ascii = ((ord(char) - 97 + shift) % 26) + 97
  encrypted_name += chr(shifted_ascii)
  # Ascii also represents other special chars and punctuations so,they will be encryped if they appear. So, else statemnt below handles: If it's a space or punctuation, keep it exactly as it is
 else:
  encrypted_name += char
print("Encrypted:", encrypted_name)

 # DECRYPTION HERE:
#  the code below does same thing as the code above but in reverse
for char in encrypted_name:
 # the if statement below. checks if the character is an uppercase letter
 if "A" <= char <= "Z":
  # To decrypt, we SUBTRACT the shift value instead of adding it
  shifted_ascii = ((ord(char) - 65 - shift) % 26) + 65
  decrypted_name += chr(shifted_ascii)
 # Check if the character is a lowercase letter
 elif "a" <= char <= "z":
  shifted_ascii = ((ord(char) - 97 - shift) % 26) + 97
  decrypted_name += chr(shifted_ascii)
print("Decrypted:", decrypted_name)