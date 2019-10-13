import sys 

def Hours(x):
    if x<0:
        raise ValueError("Input number cannot be negative")
    else:
        print("{} H, {:.2f} M".format(int(x/60),x%60))

try:
    Hours(float(sys.argv[1]))
except:
        print("Parameter Error")


