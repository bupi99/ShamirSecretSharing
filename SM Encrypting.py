import math
import secrets
import sys

def gen_poly (p, k, a0):
    #generates a poly q of degree k-1, mod p, with q(0) = a0
    q = [a0]
    r = secrets.SystemRandom()
    for i in range(1, k, 1):
        q.append(r.randint(1,p-1))

    return q
def eval_poly (q,x,p):
    s = 0
    for i in range(len(q)):
        s += (q[i]*(x**i)) % p
    return s % p

## Error checking on inputs
num_args = len(sys.argv)
if (num_args == 1):
    print("No arguments specified")
    quit()
elif (num_args <= 4):
    print("Missing args for one of the following:")
    print("Number of destination files,")
    print("k (number needed to merge back to original file),")
    print("File Name")
    print("Path to destination files")
    quit()
elif ( (not sys.argv[1].isdigit()) or  (not sys.argv[2].isdigit())):
    print("Number of destination files, and k need to be integer numbers")
    quit()

elif (num_args != int(sys.argv[1])+4):
    print("Wrong number of destination files added")
    quit()
elif (int(sys.argv[1]) >=250):
    print("Number of destination files too high (Only support up to 250)")

## Passing inputs 
n = int(sys.argv[1])
k = int(sys.argv[2])
f_name = sys.argv[3]
d_files = []
for i in range(4,num_args,1):
    d_files.append(sys.argv[i])

p = 251 # not we skip some ascii characters

for i in range(len(d_files)):
    dest = open(d_files[i], "ab")
    dest.write(bytearray([i+1]))
    dest.close()

with open(f_name, "rb") as f_ptr:
    byte = f_ptr.read(1)
    while byte:
        byte_as_int = int.from_bytes(byte, byteorder='little')
        q = gen_poly(p, k, byte_as_int)
        for i in range(len(d_files)):
            dest = open(d_files[i], "ab")
            y = eval_poly(q,i+1,p)
            y_byte = bytearray([y])
            dest.write(y_byte)
            dest.close()
        byte = f_ptr.read(1)


