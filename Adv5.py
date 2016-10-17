m =11*19
xi = 9

def rng():
    global xi
    xi  = (xi*xi)%m
    return xi

#output q1
for i in range(12):
    print(rng())
#output of running this is 81
# 82 36 42 92104 157 196 169 137 168 9



#question 2

from RandomnessTests import RandomnessTester
Bitstr =""
for i in range(120):
    Bitstr += bin(rng())[-1:]

rng_tester = RandomnessTester(None)
val = rng_tester.monobit(Bitstr)
print(val)
#output is 0.0678891548618