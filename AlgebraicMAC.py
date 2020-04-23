import random

from binascii import hexlify


def string_to_int(m):
    # helper function which converts ascii strings to their integer representation to be used in the MAC calculation

    m = m.encode()
    m = hexlify(m)
    m = m.decode()
    message = ''
    for i in range(len(m)):
        message = message + str(int(m[i],16))
    return message

def make_Zq2(q):
    # creates the group of quadratic residues in Zq that we need to select random x0 and x1 from for the keyGen
    # If there is an integer 0<x<q (q is a large prime number) such that:
    #  x^2= a(mod q),
    # then a is said to be a quadratic residue mod q
    zq2 = []
    for i in range(1, q):
        square = pow(i, 2, q)

        # checking if int
        if square % 1 == 0 and square not in zq2:
            zq2.append(square)
    return zq2


def keyGen(q):
    # produces the secret key from Zq^2
    #  choose random (x0,x1) ∈Zq^2, output sk = (x0,x1)
    zq2 = make_Zq2(q)
    x0 = random.choice(zq2)
    x1 = random.choice(zq2)
    return x0, x1


def mac(sk, m, q):
    # produces a MAC from the secret key and P
    # choose random U ∈ G, output σ = (U,U^(x0+x1m))
    u = random.randint(1, q)

    m = int(string_to_int(m))
    x0 = sk[0]
    x1m = sk[1] * m
    sigma = [0, 0]
    sigma[0] = u
    sigma[1] = pow(u, (x0 + x1m), q)
    return sigma


def verify(sk, u, u2, m, q):
    # Verify(sk,(U,U'),m): recompute U'' = U^x0+x1m, output “valid” if U'' = U', and “invalid” otherwise.
    x0 = sk[0]
    m = int(string_to_int(m))
    x1m = sk[1] * m
    newU = pow(u, (x0 + x1m), q)
    if newU == u2:
        return 'This MAC is valid'
    else:
        return 'This MAC is invalid'
