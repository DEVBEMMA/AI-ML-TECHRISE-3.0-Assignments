# letter = 'E'
# key = 8
# shifted_number = (ord(letter) - ord('E') + key) % 26 + ord('A')
# shifted_letter = chr(shifted_number)
# print(shifted_letter)  # should print 'I'

# 
# Create a function `encrypt_name(full_name, key)` that shifts each letter by the key value (key = length of your first name).



def encrypt_name(full_name, key):
    encrypted_name =""  #this is an empty string that will be used to store the encrypted name
# Bringing in our for loop to loop through each letter in the full name
    for each_letter in full_name:
        if each_letter.isupper():
            shifted_number = (ord(each_letter) - ord("A") + key) % 26 + ord("A")
            # meaning that the shifted number is calculated by taking the ascii value of the each looped Capital letter, substracting the ascii value of Capital A being 65, 
            # then adding the key which is the length of the first name and then taking its result. the % sign tells that if there is need for a  wrap around the alphabet.
            # (eg, if adding the key to the alphabet will exceed letter z), it will wrap around and continue counting from the beginning of the alphabet which is Capital letter A in this case. 
            # Finally, we add the ascii value of Capital A to get the final shifted number.
            encrypted_name = encrypted_name + chr(shifted_number)
        elif each_letter.islower():
            shifted_number = (ord(each_letter)-ord("a")+ key)%26 +ord("a")
#             this means exactly what is written above for capital letters but this time, for all lower case letters
            encrypted_name = encrypted_name+ chr(shifted_number)
        else:
            encrypted_name = encrypted_name + each_letter # having addressed both upper and lowercase, this means that if any non-letter character is encountered during the loop
            # (like space or punctuation), it will be added to the encrypted name without any change.
        
# THE CODE CHUNK ABOVE  Handle both uppercase and lowercase, AND ALSO Preserves spaces and punctuation.


 # If the key is even, also reverse the entire string after shifting.
    if key % 2 == 0: #if the modulus is 0, after the key is divided by 2, it means the key is even.
        encrypted_name = encrypted_name[::-1] # this is a slicing technique in python that reverses the string. here is a clearer explanation: 
        # the [::-1] slice notation means that we are slicing the string from the beginning(:) to the end(:), but with a step of -1, 
        # in other words, backwards, which effectively reverses the order of the characters in the string.

    return encrypted_name
    
# next is to write a code that will decrypt the encrypted name. in other words, we will write a function that will return the original name.
# but we must note that the encryption process did two things: it shifted letters but it also reversed the string if the key(being the length of the first name) is even. 
# so we must reverse the string first if the key is even, and then shift the letters back to their original position.
def decrypt_name(even_encrypted_name, key):
    if key %2==0:
       even_encrypted_name = even_encrypted_name[::-1]# this will undo the reversal first
    decrypted_name = "" # this is an empty string that will be used to store the decrypted name
    # the code above will check if the key is even, and if it is, it will reverse what happened during encryption. which is that during encryption.
    # the code below will loop through each letter in the encrypted name and shift it back to its original position.
    for each_letter in even_encrypted_name:
        if each_letter.isupper():
            shifted_number = (ord(each_letter) - ord("A") - key) % 26 + ord("A")
            decrypted_name = decrypted_name + chr(shifted_number)
        elif each_letter.islower():
            shifted_number = (ord(each_letter) - ord("a") - key) % 26 + ord("a")
            decrypted_name = decrypted_name + chr(shifted_number)
        else:
            decrypted_name = decrypted_name + each_letter # this will preserve spaces and punctuation like in the encryption function.
    return decrypted_name


def details():
    first_name = input("Enter your first name: ")
    full_name = input("Enter your full name: ")
    key =len(first_name) # the key is the length of the first name
    encrypted_name = encrypt_name(full_name, key)
    print ("Your encrypted name is: ", encrypted_name)
    decrypted_name = decrypt_name(encrypted_name, key)
    print ("Your decrypted name is: ", decrypted_name)
    # another way to do this is to call the enctypt_name function, and for the decryption, we can call the decrypt_name function and pass the result of the encrypt_name function as an argument.
    # print ("Your encrypted name is: ", encrypt_name(full_name, key))
    # print ("Your decrypted name is: ", decrypt_name(encrypt_name(full_name, key), key)) 
details()
# MKINQVWJ TMCVIUUM IS MY ENCRYPTED NAME BECAUSE MY FIRST NAME IS EMMANUEL, IT IS 8 LETTERS LONG, SO THE KEY IS 8, AND ALSO EVEN.
#NVVJWDNUR KXWROJLN  IS MY ENCRYPTED NAME BECAUSE I USED EMMANUELI THIS TIME, IT IS 9 LETTERS LONG, SO THE KEY IS 9, AND ALSO ODD. THE WHOLE NAME IS SHIFTED BY 9..