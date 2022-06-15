
encrypted = 'encrypted.txt'
unencrypted = 'unencrypted.txt'
replace = 'replace.txt'

def encrypter(unencrypted = 'unencrypted.txt',replace = 'replace.txt'):
    #unencrypted_file = open(unencrypted_file, 'r')
    unencrypted = open(unencrypted , 'r')
    replace = open(replace , 'r')
    encrypted = open('encrypted_file.txt' , 'w')
    enc_dict = {}
    for line in replace:
        key, value = line.split()
        enc_dict[key] = value

    for line in unencrypted:
        for letter in line:
            if letter in enc_dict:
                #all letters are detected
                new_letter = letter.replace(letter, enc_dict[letter])
                encrypted.write(new_letter)
            else:
                new_letter = letter
                encrypted.write(new_letter)

    # unencrypted_file.close()
    encrypted.close()
    replace.close()
    unencrypted.close()
    return encrypted


def decrypter(encrypted = 'encrypted.txt',replace = 'replace.txt'):
    unencrypted = open('unencrypted.txt' , 'w')
    replace = open(replace , 'r')
    encrypted = open(encrypted , 'r')

    enc_dict = {}
    for line in replace:
        key, value = line.split()
        enc_dict[value] = key

    for line in encrypted:
        for letter in line:
            if letter in enc_dict:
                #all letters are detected
                new_letter = letter.replace(letter, enc_dict[letter])
                unencrypted.write(new_letter)
            else:
                new_letter = letter
                unencrypted.write(new_letter)

    encrypted.close()
    replace.close()
    unencrypted.close()
    return encrypted


#if i didnt do this it would just erase the files, idk why
function = input('do you want to encrypt or decrypt? e or d?')
if function == 'd':
    decrypter(encrypted,replace)
if function == 'e':
    encrypter(unencrypted,replace)
