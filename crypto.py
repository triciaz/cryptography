import random
# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    plaintext = plaintext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = " "

    for i in plaintext:
        if i in alphabet:
            i_index = (alphabet.find(i) + offset) % len(alphabet)
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
           letter_index = (alphabet.find(letter) - offset) % len(alphabet)
           result = result + alphabet[letter_index]
       else:
           result = result + letter
    return result

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    cipher = ""
    for (plain_index, plain_character) in enumerate(plaintext):
        key_index = plain_index % len(keyword)
        key_character = keyword[key_index]
        cipher_character = encrypt_character(plain_character, key_character)
        cipher += cipher_character
    return cipher

def encrypt_character(plaintext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    character_count = len(alphabet)
    key_code = alphabet.index(keyword)
    plain_code = alphabet.index(plaintext)
    cipher_code = (key_code + plain_code) % character_count
    cipher = alphabet[cipher_code]
    return cipher

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
    assert is_superincreasing(w) == True
    w = tuple(w)

    total = sum(w[:])
    q = random.randint(total + 1, 2 * total)

    for i in range(2, q-1):
        if is_coprime(i, q) == True:
            r = i
            break
    return (w, q, r)

def is_superincreasing(w):
    sum = 0
    for i in w:
        if i < sum or i == sum:
            return False
        sum = sum + i
    return True

def is_coprime(i, q):
    if gcd(i, q) == 1:
        return True
    return False

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: B - a length-n tuple of integers
def create_public_key(private_key):
    w, q, r = private_key
    B = ()
    for i in range(len(w)):
        B.append((r * w[i]) % q)
    return B

def extended_gcd(a, b):
    last_remainder, remainder = abs(a), abs(b)
    x, last_x, y, last_y = 0, 1, 1, 0
    while remainder:
        last_remainder, (quotient, remainder) = remainder, divmod(last_remainder, remainder)
        x, last_x = last_x - quotient*x, x
        y, last_y = last_y - quotient*y, y
    return last_remainder, last_x * (-1 if a < 0 else 1), last_y * (-1 if b < 0 else 1)

def modinv(r, q):
	g, x, y = extended_gcd(r, q)
	if g != 1:
		raise ValueError
	return x % q

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    C_vals = []
    byte_arrays = [format(ord(i), '08b') for i in plaintext]
    for i in byte_arrays:
        C = 0
        for j in range(8):
            if i[j] == '1':
                C = C + public_key[j]
        C_vals.append(C)
    return C_vals

# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    w, q, r = private_key
    r_prime = modinv(r, q)
    a = ""
    for j in ciphertext:
        s = 0
        c_prime = (j * r_prime) % q
        for i in reversed(w):
            if i < c_prime or i == c_prime:
                c_prime = c_prime - i
                s = s*2 + 1
            else:
                s = s*2
        print(s)
        a = a + chr(s)
    return a

def main():
    print(encrypt_caesar('B', 25))
    result = encrypt_caesar('B', 25)
    print(decrypt_caesar(result, 25))
    print(encrypt_vigenere("IMHIT", "H"))
    vignere_result = encrypt_vigenere("IMHIT", "H")
    print(decrypt_vigenere("IMHIT", "H"))
    print(encrypt_mhkc("POTATOSALAD", (18, 28, 54, 136, 254, 740, 1714, 3194)))
    print(decrypt_mhkc([164, 5930, 904, 3222, 904, 5930, 5072, 3222, 1022, 3222, 768], ((9, 14, 27, 68, 127, 370, 857, 1597), 4745, 2)))

if __name__ == "__main__":
    main()
