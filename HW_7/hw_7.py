from decimal import Decimal
from colors import bcolors


# SECOND TASK
class frange:
    def __init__(self, start=0, stop=0, step=1, use_decimal=False):
        if use_decimal or any(isinstance(x, Decimal) for x in (start, stop, step)):
            self.current = Decimal(start)
            self.stop = Decimal(stop)
            self.step = Decimal(step)
            self.use_decimal = True
        else:
            self.current = float(start)
            self.stop = float(stop)
            self.step = float(step)
            self.use_decimal = False

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        value = self.current
        self.current += self.step
        return value


#assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])
print('SUCCESS')


for i in frange(1, 100, 3.5):
    print(i)


print('*' * 100)


# THIRD TASK

class TextContent:
    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f'The document was opened with the following arguments: {args}')
        self.opened = True

    def close(self):
        print("The document was closed")
        self.opened = False

    def __del__(self):
        if self.opened:
            print("The document was opened but not closed!")

    @staticmethod
    def action():
        print("The document is being edited")



class TextContent2:
    def __init__(self, *args):
        self.args = args
        self.resource = None

    def __enter__(self):
        self.resource = TextContent()
        self.resource.open(*self.args)
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.resource.close()


#if __name__ == "__main__":
with TextContent2('Hi') as text_content:
    text_content.action()


    #with open('text.txt', 'w') as file:
       # text_content = str(file.write('Hi'))

    print(f"{bcolors.OKBLUE}{text_content}{bcolors.ENDC} ..and bye")
    print(type(text_content))


    print(f" Repeat {bcolors.FAIL} {bcolors.YELLOWBG} {text_content} {bcolors.ENDC} to {'text.txt'}")


