def encrypt(text, shift_level): 
    uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercases = 'abcdefghijklmnopqrstuvwxyz'
    
    text_output = ""
    for character in text:
        if character in uppercases: 
            original_pos = uppercases.index(character)
            new_pos = (original_pos + shift_level) % 26
            new_char = uppercases[new_pos]
            text_output += new_char
            
        elif character in lowercases:
            original_pos = lowercases.index(character)
            new_pos = (original_pos + shift_level) % 26
            new_char = lowercases[new_pos]
            text_output += new_char
            
        else: 
            text_output += character
    return text_output

def decrypt(text, shift_level): 
    uppercases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercases = 'abcdefghijklmnopqrstuvwxyz'
    
    text_output = ""
    
    for character in text: 
        if character in uppercases: 
            original_pos = uppercases.index(character) 
            new_pos = (original_pos - shift_level) % 26
            new_char = uppercases[new_pos]
            text_output += new_char
            
        elif character in lowercases: 
            original_pos = lowercases.index(character) 
            new_pos = (original_pos - shift_level) % 26
            new_char = lowercases[new_pos]
            text_output += new_char
        
        else: 
            text_output += character
    
    return text_output

plaintext = input("Give me a text to encrypt: ")
shift = int(input("How many letters do you want to shift your message by?: "))


ciphertext = encrypt(plaintext, shift) 
print("Encrypted Message: ", ciphertext)

ciphertext = decrypt(ciphertext, shift) 
print("Decrypted Message: ", ciphertext)