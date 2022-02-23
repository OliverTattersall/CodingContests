def SieveOfEratosthenes(n): 
    primes=[]
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    # print(len(prime))
    p = 2
    #goes until √n at which point there would be no more composite numbers left True
    while (p * p <= n): 
        #print(prime[p])
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            #print(p)
            primes.append(p)
    #print(primes)
    #print(len(primes))
    return primes

def rotate(str):
    return str[1:]+str[0]



primes = SieveOfEratosthenes(1000000)
setp = set(primes)


count = 4

for i in range(11, 1000001, 1):
    if i in setp:
        flag = True
        temp = str(i)
        for j in range(len(str(i))):
            temp = rotate(temp)
            if int(temp) not in setp:
                flag = False
                break
        if flag:
            count+=1

        
print(count)
