import sys
import time

from loading import ft_progress

X = range(1)

ret = 0
for elem in ft_progress(X):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)