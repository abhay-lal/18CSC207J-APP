string = input('Enter a string')
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = [str(chr(ch)) for ch in range(97, 124)]
ncar = 0
nlet = 0
for char in string:
    if char in numbers:
        ncar += 1
    if char.lower() in letters:
        nlet += 1
print("Number of letters are ", nlet)
print("Number of letters are ", ncar)
