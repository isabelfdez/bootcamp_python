import sys

morse = {
'A' : '.-',
'B' : '-...',
'C' : '-.-.',
'D' : '-..',
'E' : '.',
'F' : '..-.',
'G' : '--.',
'H' : '....',
'I' : '..',
'J' : '.---',
'K' : '-.-',
'L' : '.-..',
'M' : '--',
'N' : '-.',
'O' : '---',
'P' : '.--.',
'Q' : '--.-',
'R' : '.-.',
'S' : '...',
'T' : '-',
'U' : '..-',
'V' : '...-',
'W' : '.--',
'X' : '-..-',
'Y' : '-.--',
'Z' : '--..',
' ' : '/',
'0' : '-----',
'1' : '.----',
'2' : '..---',
'3' : '...--',
'4' : '....-',
'5' : '.....',
'6' : '-....',
'7' : '--...',
'8' : '---..',
'9' : '----.'
}

if (len(sys.argv) < 2):
    print("No arguments were given")
    sys.exit(0)
if (len(sys.argv) > 2):
    txt = ' '.join(sys.argv[1:len(sys.argv)])
else:
    txt = sys.argv[1]
for c in txt:
    if (morse.get(c.upper()) == None):
        print("Invalid characters. Text cannot be converted into Morse code")
        sys.exit(0)
for c in txt:
    print(morse.get(c.upper()), end = " ")
print()