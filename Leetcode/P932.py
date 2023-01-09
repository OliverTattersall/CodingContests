

def beautifulArray(N):
        memo = {1: [1]}
        def f(N):
            
            if N not in memo:
                odds = f((N+1)//2)
                evens = f(N//2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            print(memo)
            return memo[N]

        '''
        n=4
        f(4)
        odds=f(2)
        even=f(2)
        f(2)
        odds = f(1) = [1]
        eevn = f(1)=[1]
        f(2)= [1,2]
        f(4) = (2x-1)*[1,2]+(2x)*[1,2]
        f(4) = [1,3]+[2,4] = [1,3,2,4]

        '''
        return f(N)

print(beautifulArray(4))