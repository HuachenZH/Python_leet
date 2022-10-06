
def isprime(n:int) -> bool:
	if n == 0 or n==1: return False
	for i in range(2,n):
		if n%i==0: return False
	return True


def listprime(n:int) -> bool:
	res = []
	for i in range(n+1):
		if isprime(i): res.append(i)
	return res

if __name__ == "__main__":
	print(listprime(53))
