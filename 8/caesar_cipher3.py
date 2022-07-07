alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction):
    final_text=""
    if direction=="decode":
        shift*=-1 # we used this outside the loop, this line is written inside the loop as shift = abs(shift) * -1 ...
    for letter in text:
        position=alphabet.index(letter)
        '''if direction=="decode":
            shift = abs(shift) * -1 '''
            # why we use abs() function in the last line is because in the next iteration loop the shift 
            # value will get multipliced again with -1... then it becomes +5...so we used absolute function.'''
        new_position = position + shift
        if direction=="encode" and new_position >= 26:
            new_position=position-26+shift
        new_letter = alphabet[new_position]
        final_text += new_letter
    print(f"The {direction}d text is {final_text}")

caesar(text=text,shift=shift,direction=direction)