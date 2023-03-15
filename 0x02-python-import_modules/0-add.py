#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

......................................................
.........................................................
vi 1-calculation.py

#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))

