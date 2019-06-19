import os
import x_mod
blit = x_mod.blit

s = "hello {}, nice to meet you! so you are from {} and prepared for this {} job?".format("John", 2066, "wonderful")


if __name__ == "__main__":
    blit(s * 2)
    print("\n__file__", __file__ )
    x = os.path.dirname(os.path.realpath(__file__))
    y = os.path.dirname(os.path.realpath(x))
    z = os.path.dirname(os.path.realpath(y))
    print(x)
    print(y)
    print(z)
    print(__doc__)

"""
    __name__

    __file__

    __doc__
"""