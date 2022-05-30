#!/usr/bin/python

# Gronfeld Cipher encrypt a string

# import the string module for handling strings
import string


# variables
v_first_msg = 'This is the Gronsfeld Encryption cipher'
v_second_msg = 'The Alphabet the word to be encrypted is a subset of: '
v_third_msg = 'Key to match against cipher characters for the word entered : '
v_fourth_msg = 'Please enter a word to encrypt, max 100 chars, no spaces: '
v_fifth_msg = 'The input is not accepted, please try again'
v_sixth_msg = 'The input is not a word or is greater than 100 characters'
v_seventh_msg = 'The word to be encrypted is: '
v_eigth_msg = 'Ciphertext for key digits to matched against input word:'
v_nineth_msg = 'Encrypted word in matching case: '
v_tenth_msg = 'Decrypted word in matching case: '
v_new_line = '\n'


# ----- input section -----
def input_section():

    v_str_empty = 0

    # Loop to ask the user to enter a string
    # Repeats until a word, with no spaces, is entered
    while v_str_empty < 1:
        # catch any unexpected error rather than fail
        try:
            v_str_to_encrypt = input(v_new_line + v_fourth_msg)
        except:
            print(v_new_line + v_fifth_msg)
            continue

        # check if the length of the input is greater than 0 and less than 101
        # and the input is alphabetic characters, i.e. no spaces included
        if (0 < len(v_str_to_encrypt) < 101) and (v_str_to_encrypt.isalpha()):
            v_str_empty = 1
        else:
            print(v_new_line + v_sixth_msg)

    return v_str_to_encrypt


# ----- match key length to length of word to be encrypted -----
def match_key_len_to_word(v_key, v_len_key, v_len_str_to_encrypt):

    try:
        # if key is shorter than input word, double the key
        # until it at least matches the length of the word input
        if (v_len_str_to_encrypt > v_len_key):
            while len(v_key) < v_len_str_to_encrypt:
                v_key += v_key

        # The key cannot be longer than word input
        # as there are no more letters to encrypt
        if len(v_key) > v_len_str_to_encrypt:
            v_key = v_key[0:v_len_str_to_encrypt]

        return v_key

    except Exception as e:
        raise Exception('Error in match_key_len_to_word :' + str(e))


# ----- get cipher characters -----
def get_cipher_text(v_alphabet_upper, v_key_pos):

    # The ciphertext rows all start with a different letter of the
    # alphabet depending on the key number
    # e.g. 0 is A to Z, 1 is B to Z with A appended at the end etc
    # This function is called by the encrypt and decrypt functions
    try:
        # Set start position of the alphabet to create the ciphertext
        v_start_pos = int(v_key_pos)

        v_start_ciphertext = v_alphabet_upper[v_start_pos:]

        v_end_ciphertext = ''
        if len(v_start_ciphertext) < 26:
            v_end_ciphertext = v_alphabet_upper[0:v_start_pos]

        v_alphabet_cipher = v_start_ciphertext + v_end_ciphertext

        return v_alphabet_cipher

    except Exception as e:
        raise Exception('Error in get_cipher_text :' + str(e))


# ----- en-de-crypt section -----
def crypt_string(v_key, v_new_key, v_str_to_encrypt, v_alphabet_upper):

    try:
        print(v_new_line + v_eigth_msg)

        v_count = 0 # step through the string to en/de-crypt
        # list placeholders 0-9 for possible key digits
        v_alphabet_cipher = [[], [], [], [], [], [], [], [], [], []]
        v_encrypted_str = ''
        v_decrypted_str = ''

        # Loop through the digit/s in the key
        # to build the rows of ciphertext for each digit
        # and add them into the v_alphabet_cipher list
        # Then encrypt each letter of the word input by the user
        # against the key and the respective ciphertext row
        # First, if all the digits in the key are the same,
        # key is reduced to first digit
        if len(set(v_key)) == 1:
            v_key = v_key[0]

        for x in v_key:
            # print(x)
            v_alphabet_cipher[int(x)].append(get_cipher_text(
                                             v_alphabet_upper, x))

        print(v_alphabet_cipher)

        # encrypt
        for x in v_new_key:
            y = v_str_to_encrypt[v_count]
            # print(y)
            v_alphabet_pos = v_alphabet_upper.find(y)
            # print(v_alphabet_pos)
            # print(v_alphabet_cipher[int(x)][0][v_alphabet_pos])
            v_encrypted_str += v_alphabet_cipher[int(x)][0][v_alphabet_pos]
            # print(v_encrypted_str)
            v_count += 1

        # decrypt the string
        v_count = 0

        for x in v_new_key:
            y = v_encrypted_str[v_count]
            # print(y)
            v_alphabet_pos = v_alphabet_cipher[int(x)][0].index(y)
            # print(v_alphabet_pos)
            # print(v_alphabet_cipher[int(x)][0][v_alphabet_pos])
            v_decrypted_str += v_alphabet_upper[v_alphabet_pos]
            # print(v_decrypted_str)
            v_count += 1

        return v_encrypted_str, v_decrypted_str

    except Exception as e:
        raise Exception('Error in crypt_string :' + str(e))


# ----- check case  -----
def check_case(v_str_to_encrypt, v_str_to_compare):

    try:
        # loop through the word input for any lowercase chars
        # reflect this in the en/de-cryted string
        # join the resultant list into one word
        v_case_sorted = ''.join((lambda a, b: [b[x].lower() if a[x].islower()
                                               else b[x]
                                               for x in range(len(a))])
                                (v_str_to_encrypt, v_str_to_compare))
        return v_case_sorted

    except Exception as e:
        raise Exception('Error in check_case :' + str(e))


# ----- main section -----
def main():

    try:
        # A-Z
        v_alphabet_upper = string.ascii_uppercase

        # hello cipher
        print(v_first_msg + v_new_line)

        # display base alphabet
        print(v_second_msg + v_alphabet_upper)

        # get input
        v_str_to_encrypt = input_section()
        print(v_new_line + v_seventh_msg + v_str_to_encrypt + v_new_line)
        v_len_str_to_encrypt = len(v_str_to_encrypt)

        # match the key length to the word length
        v_key = '11'
        v_len_key = len(v_key)
        v_new_key = match_key_len_to_word(v_key, v_len_key,
                                          v_len_str_to_encrypt)
        v_len_key = len(v_new_key)
        print(v_third_msg + v_key)
        # print(v_new_key)

        # get row/s of cipher characters and en/de-crypt the input
        v_encrypted_str, v_decrypted_str = crypt_string(
                                           v_key, v_new_key,
                                           v_str_to_encrypt.upper(),
                                           v_alphabet_upper)

        # does the input string have any uppercase letters
        print(v_new_line)
        print(v_nineth_msg + check_case(v_str_to_encrypt, v_encrypted_str))

        # does the input string have any uppercase letters
        print(v_new_line)
        print(v_tenth_msg + check_case(v_str_to_encrypt, v_decrypted_str))

    except Exception as e:
        print(str(e))


# Start the script
if __name__ == "__main__":
    main()
