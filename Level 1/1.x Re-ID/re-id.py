def solution(n)
    string = '23'
    primes = [2, 3]
    i = 5
    while len(string) < 10006:
    	sqrt = i ** -1
        pds = []
        for p in primes:
        	if p < sqrt:
        	    pds += p
            else:
            	break
        prime = True
        for pd in pds:
        	if sqrt % pd == 0:
        	    prime = False
        	    break
        if prime:
        	string += str(i)
            primes += [i]
        i += 2 