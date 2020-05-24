# iterator & generator works same.
# Only diff. iterator use (__iter & __next method) generator uses (Yield)
# iterator uses __iter & __next if complex logic.
# generator keep state of execution(i.e.keep track of last step)
# Difference between RANGE & XRANGE - XRANGE used in Python 2.X but in Python 3.X XRANGE act as RANGE
# Range gives list object & XRange gives generator object

def get_cube():  # Its Special generator object in python
    # i = 0
    # while i < 10000:
    #     i = i + 1
    #     yield i, i ** 3  # Yeild creates generator object.
    #     # Yeild (add) maintains __iter__ & __next__ method
    ############## OR ################
    gen = ((x, x ** 3) for x in range(10000))
    obj = range(100)
    print("obj", type[obj])
    obj = (x ** 3 for x in range(100))
    # for i, c in gen:
    #     print("i = {},c={}".format(i, c))
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())
    print(gen.__next__())


if __name__ == "__main__":
    # gen_obj = get_cube()
    get_cube()
    # for i, c in gen_obj:
    #     print("i = {},c={}".format(i, c))

# print(gen_obj.__next__())
# print(gen_obj.__next__())
