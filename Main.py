from AlgebraicMAC import keyGen, mac, verify

if __name__ == "__main__":
    # hard-coding the deterministic prime
    # we got this prime from PrimeNumberGenerator
    # It is kept to this small toy value because otherwise generating Zq^2 takes too long for a consumer laptop
    q = 52919

    # we use the second prime as q to generate secret key from Zq^2
    sk = keyGen(q)
    print('This is the secret key : ', sk)

    # "Hello World!" is the string we generate a MAC for in this example.
    m = "Hello World!"
    MessageAuthCode = mac(sk, m, q)
    print('This is the MAC : ', MessageAuthCode)

    # valid Algebraic MAC
    print(verify(sk, MessageAuthCode[0], MessageAuthCode[1], m, q))

    # invalid Algebraic Mac
    print(verify(sk, MessageAuthCode[0] + 3, MessageAuthCode[1], m, q))
