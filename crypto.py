# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    plaintext = plaintext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = " "
    
    for i in plaintext:
      if i in alphabet:
        i_index = (alphabet.find(letter) + offset) % len(alphabet)
        result = result + alphabet[i_index]  
      else:
        result = result + i    
    return result

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    ciphertext = ciphertext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = " "
                              
    for letter in ciphertext:
        if letter in alphabet:
            letter_index = (alphabet.find(letter) - offest) % len(alphabet)
            result = result + alphabet[letter_index]
        else:
            result = result + letter
    return result

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = " "
    
    plaintext_length = len(plaintext)
    exp_keyword = keyword
    exp_keywordLength = len(exp_keyword)
    
    while exp_keywordLength < plaintext_length:
        exp_keyword += keyword
        exp_keywordLength = len(exp_keyword)
       
    keywordPosition = 0
    
    for letter in plaintext:
        if letter in alphabet:
            letter_index = alphabet.find(letter)
            keyword_char = exp_keyword[keywordPosition]
            keyword_char_index = alphabet.find(keyword_char)
            keywordPosition += 1
            newIndex = letter_index + keyword_char_index
            if newIndex > 26:
                newIndex = newIndex - 26
            new_char = alphabet[newIndex]
            result += letter
        else: 
            result += letter
    return result

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
    # Testing code here
    pass

if __name__ == "__main__":
    main()



