""" Cesar Cipher  by Al Sweigart  al@inventwithpython.com
The Cesar Cipher is a Shift ciopher that uses addition and subtraction to
encrypt and decrypt letters.
More info at : https://en.wikipedia.org/wiki/Cesar_cipher
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, cryptography, math"""

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

''' Every possible symbol that can be encrypted/decrypted:
 (!) You can add numbers and punctuation marks to encrypt 
  symbols as well.'''
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Cesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The cesar cipher encrypts leters by shifting them over ba a')
print('key number, For example, a key fo 2 means the letter A is')
print('encrypted into C, the letter B is encrypted into D, and so on.')
print()

# Let the user enter if they are encrypting or decrypting:
while True:     #Keep asking untill the user enters e or d.
    print('Do you want to (e)ncrypt or (d)crypt?')
    response = input('>,').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the leter e or d.')

#Let the user enter the keys to use:
while True:     #Keep asking untill the user enters a valid key:
    maxKey = len(SYMBOLS) - 1
    print('please enter the key (0 to {}) to use,'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

#Let the user enter the message to encrypt/decrypt:
print('Enter the message to {}.'.format(mode))
message = input('> ')

#cezar ciphter only work on uppercase letters:
message = message.upper()

#Stores the encrypted/dcrypted form of the message
translated = ''

#Encrypt/Decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        #get the encrypted (or dcrypted) number of the symbol.
        num = SYMBOLS.find(symbol)  # Get the number of the symbol:
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key


            # Handel the wrap if num is larger than the length of
            # SYMBOLS or les than 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        
        #Add encrypted / dcrypted number's symbol to translate:
        translated = translated + SYMBOLS[num]
    else:
        # Just add the symbol without encrypting:
        translated = translated + symbol

# Display the encrypted/dcrypted message?
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to the clipboard.'.format(mode))
except:
    pass  # Do nothing if pyperclip wasn't installed.