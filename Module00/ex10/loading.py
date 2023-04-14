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
    to_print = range(0, len(list), min(int(len(list) / 30) + 1, 30))
    for i2 in list:
        i = abs(i2)
        print("\r[", str("%.2f" % (100 * (i + 1) / len(list))).rjust(6), "% ] [", end="")
        for j in to_print:
            if j <= i:
                print("=", end="")
        print(">", end = "")
        for j in to_print:
            if j > i:
                print(" ", end="")
        elapsedTime = time.time() - timer;
        estimatedRemaining = (len(list) - (i / (abs(list[1] - list[0]) if len(list) > 1 else 1) + 1)) * elapsedTime / (i + 1);
        print("] | ", str((i - abs(list[0])) / (abs(list[1] - list[0]) if len(list) > 1 else 1) + 1).rjust(4), "/", str(len(list)), " |  elapsed time:", str("%.2f" % (time.time() - timer)), 
            " | ETA:", str("%.2f" % estimatedRemaining).rjust(6), end='\r')
        yield i2

    