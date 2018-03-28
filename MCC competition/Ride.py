def func(line):
    mult = 1
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for character in line:
        for i in range(26):
            if character == alphabet[i]:
                mult *= i


for line in input().readlines():
    func(line.strip())
