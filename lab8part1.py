import random

p = 99999989
a = 11

def main():
    # local picks random ra, remote picks random rb
    Alice = int(random.random() * p)
    Bob = int(random.random() * p)
    print(Alice, Bob)
    # local computes ya, remote computes yb
    ya = pow(a, Alice, p)
    print(ya)
    yb = pow(a, Bob, p)
    print(yb)
    # local and remote exchange ya and yb over the insecure channel
    # local computes key, remote computes key
    print('These two numbers should be the same:')
    localkey = pow(yb, Alice, p)
    print("Local key {0}".format(localkey))
    remotekey = pow(ya, Bob, p)
    print("Remote key {0}".format(remotekey))
    if localkey == remotekey:
        print ("The shared key is {0}".format(localkey))

main()
