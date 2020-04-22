from AlgebraicMAC import keyGen, mac, verify

if __name__ == "__main__":
    # hard-coding the deterministic primes
    # we got these primes from PrimeNumberGenerator
    # they are kept to this small toy value because otherwise generating Zq^2 takes too long for a consumer laptop
    prime1 = 18671
    prime2 = 58943

    # we use the hard coded primes to get the group G which we will do all our operations in
    G = prime1 * prime2

    # we use the second prime as q to generate secret key from Zq^2
    sk = keyGen(prime2)
    print('This is the secret key : ', sk)

    # "Hello World!" is the string we generate a MAC for in this example.
    m = "Hello World!"
    MessageAuthCode = mac(sk, m, G)
    print('This is the MAC : ', MessageAuthCode)

    # valid Algebraic MAC
    print(verify(sk, MessageAuthCode[0], MessageAuthCode[1], m, G))

    # invalid Algebraic Mac
    print(verify(sk, MessageAuthCode[0] + 3, MessageAuthCode[1], m, G))
