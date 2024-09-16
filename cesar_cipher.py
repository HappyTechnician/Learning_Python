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
SYMBOLS =   'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,?!/"'

print('Cesar Cipher, by Al Sweigart al@inventwithpython.com')
print('The cesar cipher encrypts leters by shifting them over ba a')
print('key number, For example, a key fo 2 means the letter A is')
print('encrypted into C, the letter B is encrypted into D, and so on.')
print()

