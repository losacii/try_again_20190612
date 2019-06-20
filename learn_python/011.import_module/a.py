import os
import mymods
blit = mymods.blit

s = "\nHello {}, \nso you are from {} and \nprepared for this {} job?\n".format("John", 2066, "wonderful")


if __name__ == "__main__":
    blit(s * 2)
    print("\n__file__", __file__ ) # __file__
    x = os.path.dirname(os.path.realpath(__file__)); print(x) # real path
    y = os.path.dirname(os.path.realpath(x)); print(y) # dir name
    z = os.path.dirname(os.path.realpath(y)); print(z) # dir name
    print(__doc__) # __doc__

    print(mymods.__name__)
    mymods.Foo()
    mymods.Bar()

"""
    __name__

    __file__

    __doc__
"""