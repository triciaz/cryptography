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
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = " "

    ciphertext_length = len(ciphertext)

    exp_keyword = keyword
    exp_keywordLength = len(exp_keyword)

    while exp_keywordLength < ciphertext_length:
        exp_keyword = exp_keyword + keyword
        exp_keywordLength = len(exp_keyword)
    keyword_position = 0

    for letter in ciphertext:
        if letter in alphabet:
            index = alphabet.find(letter)
            keyword_char = exp_keyword[keyword_position]
            keyword_char_index = alphabet.find(keyword_char)
            keyword_position = keyword_position + 1
            new_index = index - keyword_char_index
            if new_index > 26:
                new_index = new_index + 26
                new_char = alphabet[new_index]
                result = result + new_char
            else:
                result = result + letter

    return result

#  Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    w = [1]
    z = 1
    for i in range(n):
        total = sum(w[:])
        z = random.randint(total + 1, 2 * total)
        w.append(z)
    assert utils.is_superincreasing(w) == True
    w = tuple(w)

    total = sum(w[:])
    q = random.randint(total + 1, 2 * total)

    for i in range(2, q-1):
        if utils.coprime(i, q) == True:
            r = i
            break
    return (w, q, r)

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: B - a length-n tuple of integers
def create_public_key(private_key):
    B = ()
    for i in range(1, 8):
        B.append((r * w[i]) % q)
    return B

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    C_vals = []
    res = ''.join(format(ord(i), 'b') for i in plaintext)
    M = array.array('m',(0 for m in range(0,8))

    C = 0
    for i in range(1, 8):
        M[i] = res[i]
        M = utils.byte_to_bits(i)
        C_i = M[i] + public_key[i]
        C = C + C_i
        C_vals.append(C)
    return C_vals
    
# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    for i in range(q-1):
        s = 0
        while r*s%q != 1:
            s = s + 1
    for i in len(C_vals):
        C_i = C[i] * s % q

    indices_array = []
    w_i = 0
    while s != 0:
        for x in range(len(w), 1, -1):
            if w[x] > s:
                x = x + 1
            else:
                w_i = w[x]
            indices_array.append(i)
        s = s - w_i
        
    res = ''.join(format(ord(i), '08b') for i in ciphertext)
    decrypt = []
    for i in range(0, len(res), 8):
        ans.append(chr(int(res[i:i+8],2)))
    ''.join(decrypt)

    return decrypt
    
if __name__ == "__main__":
    main()



