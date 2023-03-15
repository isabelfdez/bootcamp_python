import sys

if (len(sys.argv) == 1):
    quit()

elif (len(sys.argv) == 2):
    txt = sys.argv[1][::-1].swapcase()

else:
    txt = ""
    for x in range(len(sys.argv) - 1, 0, -1):
        txt += sys.argv[x][::-1].swapcase()
        if (x != 1):
            txt += ' '

print(txt)
