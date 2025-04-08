from decimal import Decimal
import time
from colors import bcolors


# SECOND TASK
class frange:
    def __init__(self, start, stop, step):
        self.start = Decimal(str(start))
        self.stop = Decimal(str(stop))
        self.step = Decimal(str(step))

    def __iter__(self):
        flow_number = self.start
        while flow_number <= self.stop:
            yield flow_number
            flow_number += self.step

assert(list(frange(0, 4, 1)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 4, 1)) == [2, 3, 4])
assert(list(frange(2, 9, 2)) == [2, 4, 6, 8])
#assert(list(frange(10, 4, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
#assert(list(frange(0, 0, 1)) == [])
print('SUCCESS')

for i in frange(1, 100, 3.5):

    print(i)
    time.sleep(1)

# THIRD TASK

with open('text.txt', 'w') as file:
    text_content = file.write('Hi')

    print(f"{bcolors.OKBLUE}{str(text_content)}{bcolors.ENDC} ..and bye")
    print(type(text_content))

print(f" Repeat {bcolors.FAIL} {bcolors.YELLOWBG} {text_content} {bcolors.ENDC} to {'text.txt'}")