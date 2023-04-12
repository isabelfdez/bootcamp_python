# The difference between yield and return is that yield returns a value and pauses
# the execution while maintaining the internal states, whereas the return statement
# returns a value and terminates the execution of the function.

#from tqdm import tqdm
#import time
#for i in tqdm(range(20), desc = 'tqdm() Progress Bar'):
#    time.sleep(0.5)

import sys
import time

timer = time.time()

def ft_progress(list):
    to_print = range(0, len(list), int(len(list) / 30))
    for i in list:
        print("[", str("%.2f" % (100 * (i + 1) / len(list))).rjust(6), "% ] [", end = "")
        for j in to_print:
            if j <= i:
                sys.stdout.write("=")
        print(">", end = "")
        for j in to_print:
            if j > i:
                sys.stdout.write(" ")
        elapsedTime = time.time() - timer;
        estimatedRemaining = (len(list) - (i + 1)) * elapsedTime / (i + 1);
        print("] | ", str(i + 1).rjust(4), "/", str(len(list)), " |  elapsed time:", str("%.2f" % (time.time() - timer)), 
            " | ETA:", str("%.2f" % estimatedRemaining).rjust(6), end = '\r')
        yield i

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    time.sleep(0.005)
print()
print(ret)
    