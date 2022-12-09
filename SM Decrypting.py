import math
import sys

def decrypt_byte(ys,xs,k, p):
    a0 = 0
    idx = 0
    for xj in xs:
        lj = 1
        for xm in xs:
            if xj != xm:
                lj *= ((-xm)*pow(xj-xm,-1,p) % p)
        a0 += lj*ys[idx]
        idx += 1
    return a0 % p

## Error checking on inputs
num_args = len(sys.argv)
if (num_args == 1):
    print("No arguments specified")
    quit()

elif (num_args <= 3):
    print("Missing args for one of the following:")
    print("Number of destination files (should be k),")
    print("File Name")
    print("Path to destination files")
    quit()
elif (not sys.argv[1].isdigit()):
    print("Number of destination files needs to be integer number")
    quit()
elif (num_args != int(sys.argv[1])+3):
    print("Wrong number of destination files added")
    quit()
elif (int(sys.argv[1]) >=250):
    print("Number of destination files too high (Only support up to 250)")

## Passing inputs 
k = int(sys.argv[1])
f_name = sys.argv[2]
d_files = []
p = 251
for i in range(3,num_args,1):
    d_files.append(sys.argv[i])

df_ptrs = []
xs = []
for d_f in d_files:
    dest = open(d_f, "rb")
    df_ptrs.append(dest)
    st = dest.read(1)
    x = int.from_bytes(st, byteorder='little')
    xs.append(x)

with open(f_name, "ab") as f_ptr:
    byte_arr = []
    for d_ptr in df_ptrs:
        byte = d_ptr.read(1)
        byte_arr.append(byte)
    while byte_arr[0]:
        yvals = []
        for byte in byte_arr:
            yvals.append(int.from_bytes(byte, byteorder='little'))
        byte =bytearray([decrypt_byte(yvals,xs, k, p)])
        f_ptr.write(byte)
        
        byte_arr = []
        for d_ptr in df_ptrs:
            byte = d_ptr.read(1)
            byte_arr.append(byte)
