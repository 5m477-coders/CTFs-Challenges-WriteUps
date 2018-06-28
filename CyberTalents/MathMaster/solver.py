#!/usr/bin/env python
from z3 import *
 
a = [Int('a[%d]' %i) for i in range(0,11)]

 
s = Solver()
 
s.add(a[0] > 0, a[2] < 127)
s.add(a[1] > 0, a[2] < 127)
s.add(a[2] > 0, a[2] < 127)
s.add(a[3] > 0, a[3] < 127)
s.add(a[4] > 0, a[4] < 127)
s.add(a[5] > 0, a[5] < 127)
s.add(a[6] > 0, a[6] < 127)
s.add(a[7] > 0, a[7] < 127)
s.add(a[8] > 0, a[8] < 127)
s.add(a[9] > 0, a[9] < 127)
s.add(a[10] > 0, a[10] < 127)
 
s.add(a[0] * a[1] == 4004, a[1] * a[2] == 6032, a[2] * a[3] == 8352, a[3] + a[4] == 167, a[4] + a[5] == 172, a[5] + a[6] == 141, 102 *
      a[6] + 32 * a[7] - 13 * a[8] == 8700, a[0] * a[7] * a[1] == 460460, a[2] * a[8] * a[3] == 968832, a[4] * a[9] * a[5] == 373065, a[2] * a[10] + a[7] == 9627, a[10] == 82)

s.check()
for x in range(len(a)):
print chr(int(str(s.model()[a[x]]))),
