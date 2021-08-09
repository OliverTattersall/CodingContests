def findPrimes(n):
    
    primes=[] #list where all primes will go into
    prime=[True for i in range(n+1)] #list intiated with n+1 True values
    p=2

    while p*p<=n: #loops from 2 to √n as the highest possible factor that would not be 
                  #eliminated would be √n. Ex. 36, any factors higher than 6 would have been eliminated already: 18 by 2, 12 by 3
        if prime[p]==True: #tests if the current p value is a prime so it can eliminate all multiples
            
            for i in range(p*p, n+1, p): # loops from 
                prime[i]=False

        p+=1 # increments p to test the next integer

    for i in range(2, n+1, 1): # loops from 2 to n
        if prime[i]==True: # tests to see if that number is prime
            primes.append(i) # if prime appends it to the list primes

    return primes #returns list of primes between 2 and n inclusive




'''
This function finds the sum of the primes between 0 and n
Parameters: Integer n
Conditions: n>2 
'''

def EulerProblem10(n):
    primelst=findPrimes(n)
    return sum(primelst)
# print(EulerProblem10(19))
# print(EulerProblem10(10))
print(EulerProblem10(2000000))
