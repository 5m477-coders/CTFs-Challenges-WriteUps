import os
from hashlib import sha256
 
ct = "868c017b7bef15e04ccc5f2d6b4c372fdff881080155".decode('hex')
 
def H(v):
    return int(sha256(str(v)).hexdigest(), 16)
 
def STEP(v):
    return (31338 * v**3 + 17 * v**2 + 2017 * v + 10) % 2**256
 
 # verify suspicion that as long as the last byte is the same
 # the step function will give us exactly the same sequence
 # of last bytes afterwards

x = H(os.urandom(32))
y = x % 256
for i in range(100):
    if STEP(x) % 256 != STEP(y) % 256:
        print "wrong direction"
print "suspicion verified"
