# Applied_Crypto_Spring_2020_Project_Signal
This repository contains files that we need to generate a toy Algebraic Message Authentication Code algorithm to verify the integrity of transmitted strings. 

How to run: 

    1. Only two files are needed to run this MAC: "Main.py" and "AlgebraicMAC.py"

    2. Value of the prime q is hardcoded into the Main in line 7 and can be changed with any prime generated from PrimeNumberGenerator

    3. m = "Hello World!" is the hardcoded strong we choose to MAC as an example, this can be replaced  with any string of your choice.

    4. We test the verify function after generating a Message Authentication Code.  

    5. The PrimeNumberGenerator uses the Miller-Rabin primality test to generate large primes. 
       We have borrowed a portion of this code from various StackOverflow posts and combined it with some of our own to generate prime of the size that we need. 
       Real crypto would use a much larger prime, but the quadratic residue group of such a prime would be stored locally. 
       We are doing this every time we run the code and this is the bottleneck in our system but it allows us to test the logic for different prime numbers. 
       This is the reason our code takes 14-16 seconds to compile and give an output. 


The logic for the algebraic MAC is contained in "AlgebraicMAC.py" and it has 3 primary functions: 

    1. keyGen
        Takes a prime number q as inut and returns a secret key tuple of (x0,x1)

    2. mac
        Takes in secret key, message and G (for cyclic group G = p * q)
        Returns the MAC

    3. verify
        Takes in secret key, the MAC, the message received and G and checks if the MAC is valid for the given secret key and message. 