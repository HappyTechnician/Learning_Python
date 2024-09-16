'''Cesar Cipher Hacker, by Al Sweigart al@inventwithoythin.com
This program hack messages encryped with the Cesar Cipher by doing
a brute force attack against every possible key.
More infor at: 
https://en.wikipideia.org/wiki/cesar_cipher#Breaking_the_cipher
View this code at  https://nostarch.com/big-book-small-python-projects
Tags: tiny, beginner, cryptography, math'''

print('Cesar Cipher Hacker, by Al Sweigart  al@inventwithpython.com')

# Let the user specify the message to hack:
print('Enter the encrypted Cesar Cipher message to hack.')
message = input('> ')

#Every possible symbol that can be encrypted:
#This must match the symbols used in the encrypted message.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):  #LOOP THROUGH EVERY POSSIBLE KEY.
    translated = ''

    #Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  #Get the number of symbol.
            num = num - key

            #handel the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(SYMBOLS)
            
            #Add decrypted number's symbol to translate
            translated = translated + SYMBOLS[num]
        else:
            #Just add the symbol witout decrypting :
            translated = translated + symbol

    #Display the key being tested, along with it's decrypted texts:
    print('Key #{}: {}'.format(key, translated))
