numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
small_letters = [str(chr(ch)) for ch in range(97, 124)]
big_letters = [str(chr(ch)) for ch in range(65, 92)]
symbols = ['$', '#', '@']
sl = False
bl = False
nl = False
syml = False
clen = True
password = input('Enter a string')
for char in password:
    if 6 < len(password) < 16:
        if char in small_letters:
            sl = True
        if char in big_letters:
            bl = True
        if char in numbers:
            nl = True
        if char in symbols:
            syml = True
    else:
        clen = False
if sl and bl and nl and syml and clen:
    print('Valid Password')
else:
    print('Not a Valid Password')
