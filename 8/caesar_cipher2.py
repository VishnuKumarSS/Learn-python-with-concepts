alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction=="encode":
    # below function is easy to understand function
    def encrypt(text,shift):
        cipher_text=""
        for letter in text:
            position = alphabet.index(letter)

            new_position = position+shift 
            if new_position >= 26: # if the position becomes greater than 26 # important code
                new_position=position-26+shift # this will make the position to start again from first
                # or we can change the list alphabet by copying the values again like this, below
                """alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']"""
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        print("The encoded text is",cipher_text)
    encrypt(text,shift)


elif direction=="decode":
    # below is the function to decrypt the message given
    def decrypt(text,shift):
        plain_text=""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position-shift
            new_letter = alphabet[new_position]
            plain_text+=new_letter
        print("The decoded text is",plain_text)
    decrypt(text,shift)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.