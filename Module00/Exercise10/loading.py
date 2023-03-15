from tqdm import tqdm
import time
for i in tqdm(range(20), desc = 'tqdm() Progress Bar'):
    time.sleep(0.5)

def ft_progress(lst):
    