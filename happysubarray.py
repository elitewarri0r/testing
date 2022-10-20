## input ##
t = int(input())

for ti in range(t) :
	n = int(input())
	l = []
	inputlist = input().split(' ')
	for i in range(n) :
		l.append(int(inputlist[i]))

	## prefix sums starts ##
	prefixsums = 0
	for i in range(n) :
		element = l[i]

		if element < 0: continue
		
		adder = element
		for j in range(i,n) :
			print('l[j]',l[j])

			if j == i :
				adder = element

			elif element + l[j] >= 0 :
				adder += l[j]

			else : # if the sum becomes negative then this quits this for loop
				print('Broken')
				break
			
			print('adder after ---',adder)
			prefixsums += adder
	
	print('Case #{}: {}'.format(ti+1,prefixsums))
