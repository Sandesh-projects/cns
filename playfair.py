import string

def preprocess_text(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")
    if len(text) % 2 != 0:
        text += "Z"
    return text

def generate_playfair_matrix(key):
    alphabet = string.ascii_uppercase.replace("J", "")

    key = key.upper().replace("J", "I")
    matrix = []
    for char in key:
        if char not in matrix and char in alphabet:
            matrix.append(char)

    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    
    for _ in playfair_matrix:
        print(_)
    return playfair_matrix

def find_position(matrix, char):
  
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def encrypt_playfair(plaintext, key):
    plaintext = preprocess_text(plaintext)
    
    playfair_matrix = generate_playfair_matrix(key) 
    ciphertext = []

    for i in range(0, len(plaintext), 2):
        char1 = plaintext[i] # H
        char2 = plaintext[i + 1] # I
        
        row1, col1 = find_position(playfair_matrix, char1)
        row2, col2 = find_position(playfair_matrix, char2)

        if row1 == row2:
            ciphertext.append(playfair_matrix[row1][(col1 + 1) % 5])
            ciphertext.append(playfair_matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            ciphertext.append(playfair_matrix[(row1 + 1) % 5][col1])
            ciphertext.append(playfair_matrix[(row2 + 1) % 5][col2])
        else:
            ciphertext.append(playfair_matrix[row1][col2])
            ciphertext.append(playfair_matrix[row2][col1])

    return ''.join(ciphertext)

def decrypt_playfair(ciphertext, key):
    playfair_matrix = generate_playfair_matrix(key)
    plaintext = []

    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        
        row1, col1 = find_position(playfair_matrix, char1)
        row2, col2 = find_position(playfair_matrix, char2)

        if row1 == row2:
            plaintext.append(playfair_matrix[row1][(col1 - 1) % 5])
            plaintext.append(playfair_matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(playfair_matrix[(row1 - 1) % 5][col1])
            plaintext.append(playfair_matrix[(row2 - 1) % 5][col2])
        else:
            plaintext.append(playfair_matrix[row1][col2])
            plaintext.append(playfair_matrix[row2][col1])

    
    if plaintext[-1] == 'Z':
        plaintext.pop()

    return ''.join(plaintext)


key = "October"
plaintext = "sandesh"
ciphertext = encrypt_playfair(plaintext, key)
print("Encrypted:", ciphertext)

decrypted_text = decrypt_playfair(ciphertext, key)
print("Decrypted:", decrypted_text)
