def non_repeating(list1):
	#the function gives a list of elements of list1 appearing only once
	f_list = []
	for i in list1:
		if i not in f_list:
			f_list.append(i)
	return(f_list)
def prime_implicants(list1,actual_function,numVar):
	#list1 contains all the combining 1,2,3 's outputs	
	prime_implicants = [] ; l1 = [] ; l2 = [] ; l3 = []
	for i in list1 :
		x = i.count("-")
		if x == 1:
			l1.append(i)
		if x == 2:
			l2.append(i)
		if x == 3:
			l3.append(i)		
	prime_implicants.extend(l3)
	if len(l3) == 0 and len(l2) != 0:
		prime_implicants.extend(l2)
	if len(l3) == 0 and len(l2) == 0 and len(l1) != 0:
		prime_implicants.extend(l1)
	if len(l3) == 0 and len(l2) == 0 and len(l1) == 0:
		prime_implicants.extend(actual_function)

	a = [] ; b = [] ; c = []
	for i in l1:
		x = i.replace("-","0")
		y = i.replace("-","1")
		c.append(x); c.append(y)
	for i in actual_function:
		if i not in c:
			prime_implicants.append(i)
	for i in l2:
		x = i.find("-")
		y = i.rfind("-")
		x1 = i.replace("-","0",1)
		y1 = i.replace("-","1",1)
		if y != numVar-1:
			x2 = i[:y] + "0" + i[y+1:]
			y2 = i[:y] + "1" + i[y+1:]
		else:
			x2 = i[:y] + "0"
			y2 = i[:y] + "1"
		a.append(x1) ; a.append(x2) ; a.append(y1) ; a.append(y2)
	for i in l1:
		if i not in a:
			prime_implicants.append(i)		
	if numVar == 4 and len(l3) != 0:
		for i in l3:
			x = i.find("-")
			z = i.rfind("-")
			y = i.find("-",x+1,z)
			x1 = i[0:x] + "0" + i[x+1:] ; x2 = i[0:x] + "1" + i[x+1:]
			y1 = i[0:y] + "0" + i[y+1:]	; y2 = i[0:y] + "1" + i[y+1:]
			if z != numVar-1:
				z1 = i[0:z] + "0" + i[z+1:] ; z2 = i[0:z] + "1" + i[z+1:]
			else:
				z1 = i[0:z] + "0" ; z2 = i[0:z] + "1"
			b.append(x1);b.append(x2);b.append(y1);b.append(y2);b.append(z1);b.append(z2)	
		for i in l2:
			if i not in b:
				prime_implicants.append(i)
		
	prime_implicants = non_repeating(prime_implicants)
	return(prime_implicants)
def essential_prime_implicants(list1,actual_function,numVar):
	EPI = [] ; l0 = [] ; l1 = [] ; l2 = [] ; l3 = []
	for i in list1:
		x = i.count("-")
		if x == 0:
			l0.append(i)
		if x == 1:
			l1.append(i)
		if x == 2:
			l2.append(i)
		if x == 3:
			l3.append(i)
	EPI.extend(l3)
	for i in l0:
		if i in actual_function:
			EPI.extend(l0) 
	A = [] ; a = [] ; b = []
	for i in l1:
		s1 = []
		x1 = i.replace("-","0")
		x2 = i.replace("-","1")
		if x1 in actual_function:
			s1.append(x1) 
		if x2 in actual_function:
			s1.append(x2)
		a.append(s1)
	for i in range (0,len(l1)):
		y1 = a[i] ; y2 = l1[i]
		y = y2,y1
		A.append(y) 
	for i in l2:
		s2 = []
		w = i.find("-")
		q = i.rfind("-")
		if q != numVar-1 and q-w == 1:
			x1 = i[0:w] + "00" + i[q+1:] ; x2 = i[0:w] + "01" + i[q+1:]			
			x3 = i[0:w] + "10" + i[q+1:] ; x4 = i[0:w] + "11" + i[q+1:]			
		if q == numVar-1 and q-w == 1:
			x1 = i[0:w] + "00" ; x2 = i[0:w] + "01"	
			x3 = i[0:w] + "10" ; x4 = i[0:w] + "11"
		if q != numVar-1 and q-w != 1:
			x1 = i[0:w] + "0" +i[w+1:q] + "0" + i[q+1:]
			x2 = i[0:w] + "0" +i[w+1:q] + "1" + i[q+1:]
			x3 = i[0:w] + "1" +i[w+1:q] + "0" + i[q+1:]
			x4 = i[0:w] + "1" +i[w+1:q] + "1" + i[q+1:]
		if q == numVar-1 and q-w != 1:
			x1 = i[0:w] + "0" + i[w+1:q] + "0"
			x2 = i[0:w] + "0" + i[w+1:q] + "1"
			x3 = i[0:w] + "1" + i[w+1:q] + "0"
			x4 = i[0:w] + "1" + i[w+1:q] + "1"
		if x1 in actual_function:
			s2.append(x1)
		if x2 in actual_function:
			s2.append(x2)
		if x3 in actual_function:
			s2.append(x3)
		if x4 in actual_function:
			s2.append(x4)
	
		b.append(s2)
	for i in range (0,len(l2)):
		y1 = b[i] ; y2 = l2[i]
		y = y2,y1
		A.append(y)
	list2 = []
	for i in A :
		x = i[1]
		for j in range (0,len(x)):
			y = x[j]
			list2.append(y)
	list3 = []
	for i in list2:
		if i in actual_function:
			list3.append(i)

	D = {}
	for i in list3:
		x = list3.count(i)
		D[i] = x
	H = []
	for i in A:
		x = i[1]
		I = []
		for j in x:
			y = D[j]
			I.append(y)
		i = list(i)
		i.append(I)
		H.append(i)
	list4 = []
	list5 = []
	for i in H:
		x = i[2]
		if 1 in x:
			EPI.append(i[0])
		else:
			list4.append(i)
	l = []
	for i in EPI:
		if len(i) == 3:
			x = i[1]
			l.extend(x)
	for i in list4:
		x = i[1]
		for j in range (0,len(x)):
			y = x[j]
			if y not in l:
				list5.append(i)
	#list5 has the minimised terms which are semi-essential	
	
	if len(list5) != 0:
		list6 = []	
		list5 = non_repeating(list5)
		for i in list5:
			x = i[1]			
			for j in x:
				r1 = []
				for k in list5:
					y = k[1]
					if k != i:						
						for m in y:
							if m == j:
								list6.append(i[0])
		list6 = non_repeating(list6)
		if len(list6) == 2:
			r1 = [] ; r1.append(list6[0])
			r2 = [] ; r2.append(list6[1])
			r1.extend(EPI) ; r2.extend(EPI)
			return(r1,r2)
		if len(list6) == 4:
			r1 = [] ; r1.append(list6[0]) ; r1.append(list6[2])	;r1.extend(EPI)						
			r2 = [] ; r2.append(list6[0]) ; r2.append(list6[3])	;r2.extend(EPI)	
			r3 = [] ; r3.append(list6[1]) ; r3.append(list6[2])	;r3.extend(EPI)	
			r4 = [] ; r4.append(list6[1]) ; r4.append(list6[3])	;r4.extend(EPI)	
			return(r1,r2,r3,r4) 

	EPI = non_repeating(EPI)
	return(EPI)
def combining1(list1,list2,numVar):
	#the function creates pairs of the binary inputs available depending on the no. of matching occurences, based on mccluskey method
	l = []
	if len(list1) != 0 and len(list2) != 0:
		for i in list1:
			for j in list2:
				count = 0
				for k in range (0,numVar):
					if i[k] == j[k]:
						count += 1
				if count == numVar-1 :
					for k in range (0,numVar):
						if i[k] != j[k]:
							if k < numVar-1:
								m = i[0:k] + "-" + i[k+1:]
							else:
								m = i[0:k] + "-"
							l.append(m)
	return(l)
def combining2(list1,list2,numVar):
	#the function creates quads of the minimised pairs from combining1 function depending on the no. of matching occurences, based on mccluskey method

	l = []
	if len(list1) != 0 and len(list2) != 0 :
		for i in list1:
			for j in list2:
				for k in range (0,numVar):
					if i[k] == "-" and j[k] == "-":
						count = 0
						for m in range (0,numVar):
							if i[m] == j[m]:
								count += 1
						if count == numVar-1:
							for n in range (0,numVar):
								if i[n] != j[n]:
									if n < numVar-1:
										o = i[0:n] + "-" + i[n+1:]
									else:
										o = i[0:n] + "-"
									l.append(o)
	return(l)
def combining3(list1,list2,numVar):
	#the function creates octs of the quads obtained from combining2 function depending on the no. of matching occurences, based on mccluskey method
	l = []
	if len(list1) != 0 and len(list2) != 0 :
		for i in list1:
			for j in list2:
				count1 = 0
				for k in range (0,numVar):
					if i[k] == "-" and j[k] == "-":
						count1 += 1
				if count1 == 2:
					count2 = 0
					for m in range (0,numVar):
						if i[m] == j[m]:
							count2 += 1
					if count2 == numVar-1:
						for n in range  (0,numVar):
							if i[n] != j[n]:
								if n < numVar-1:
									o = i[0:n] + "-" + i[n+1:]
								else:
									o = i[0:n] + "-"
								l.append(o)
	return(l)
def integertobinary(intlist,numVar):
	#the function converts the input integers to binary
	flist = []
	for i in intlist:
		z = format(int(i),"b")		
		if numVar == 4:
			if len(z) == 1:
				z = "000" + str(z)
			elif len(z) == 2:
				z = "00" + str(z)
			elif len(z) == 3:
				z = "0" + str(z)
			elif len(z) == 4:
				z = str(z)
		elif numVar == 3:
			if len(z) == 1:
				z = "00" + str(z)
			elif len(z) == 2:
				z = "0" + str(z)
			elif len(z) == 3:
				z = str(z)
		elif numVar == 2:
			if len(z) == 1:
				z = "0" + str(z)
			elif len(z) == 2:
				z = str(z)
		elif numVar == 1:
			z = str(z)
		
		flist.append(z)
	return(flist)
def expression(l,numVar):
	#the function substitues variables to  the minimised binary inputs 
	# for a 1 input functon the output variable is w
	# for a 2 input function the output variables are w,x
	# for a 3 variable input the output variables are w,x,y
	# for a 4 input function the output variables are w,x,y,z
	exp = ""
	for i in range (0,len(l)):
		f = l[i]
		for j in range (0,numVar):
			if j == 0:
				if f[j] == '0':
					exp = exp + "w'"
				elif f[j] == '1':
					exp = exp + "w"
			if j == 1:
				if f[j] == '0':
					exp = exp + "x'"
				elif f[j] == '1':
					exp = exp + "x"
			if j == 2:
				if f[j] == '0':
					exp = exp + "y'"
				elif f[j] == '1':
					exp = exp + "y"
			if j == 3:
				if f[j] == '0':
					exp = exp + "z'"
				elif f[j] == '1':
					exp = exp + "z"
			
		exp = exp + "+"
	stringOut = exp[:-1]
	return stringOut
def minFunc(numVar, stringIn):
	# the function will give the minimised expression for a 1,2,3,4 variable function using the concept of kmaps.
	a = stringIn.find("d")
	x = (stringIn[1:a-1]).split(",")
	y = x
	actual_function = integertobinary(y,numVar)
	if stringIn[a+1] != "-":
		w = (stringIn[a+2:len(stringIn)-1]).split(",")		
		x.extend(w)	
	function = integertobinary(x,numVar)	
	l0 = []; l1 = []; l2 = []; l3 = []; l4 = []			
	#li : list of binary no's having i no. of 1
	count = 0											
	for i in function:
		for j in range (0,numVar):
			if i[j] == "1":
				count += 1
		if count == 0 :
			l0.append(i)
		if count == 1:
			l1.append(i)
		if count == 2:
			l2.append(i)
		if count == 3:
			l3.append(i)
		if count == 4:
			l4.append(i)
		count = 0	
	if numVar == 4:
		i = non_repeating(combining1(l0,l1,numVar))
		j = non_repeating(combining1(l1,l2,numVar))
		k = non_repeating(combining1(l2,l3,numVar))
		l = non_repeating(combining1(l3,l4,numVar))
		i1 = non_repeating(combining2(i,j,numVar))
		j1 = non_repeating(combining2(j,k,numVar))
		k1 = non_repeating(combining2(k,l,numVar))
		i2 = non_repeating(combining3(i1,j1,numVar))
		j2 = non_repeating(combining3(j1,k1,numVar))
		if len(i2) == 4 and len(j2) == 4:
			minlist = ["----"]
			fminlist = minlist
		else:
			list1 = i+j+k+l+i1+j1+k1+i2+j2
			minlist = prime_implicants(list1,actual_function,numVar)		#list of prime implicants of function
			fminlist = essential_prime_implicants(minlist,actual_function,numVar)	#list of essential prime implicants of the function
	if numVar == 3:
		i = non_repeating(combining1(l0,l1,numVar))
		j = non_repeating(combining1(l1,l2,numVar))
		k = non_repeating(combining1(l2,l3,numVar))
		i1 = non_repeating(combining2(i,j,numVar))
		j1 = non_repeating(combining2(j,k,numVar))
		i2 = non_repeating(combining3(i1,j1,numVar))
		if len(i2) != 0:
			minlist = ["---"]
			fminlist = minlist
		else:
			list1 = i+j+k+i1+j1
			minlist = prime_implicants(list1,actual_function,numVar)		#list of prime implicants of function
		fminlist = essential_prime_implicants(minlist,actual_function,numVar)		#list of essential prime implicants of the function
	if numVar == 2:
		i = non_repeating(combining1(l0,l1,numVar))
		j = non_repeating(combining1(l1,l2,numVar))
		i1 = non_repeating(combining2(i,j,numVar))
		if len(i1) != 0:
			minlist = ["--"]
			fminlist = minlist
		else:
			list1 = i +j
			minlist = prime_implicants(list1,actual_function,numVar) 			#list of prime implicants of function
			fminlist = essential_prime_implicants(minlist,actual_function,numVar)		#list of essential prime implicants of the function
	if numVar == 1:
		if len(function) == 2:
			minlist = ["-"]
		else:
			minlist = function 
		fminlist = minlist
	if fminlist[0] == "-"*numVar :		
		exp = "1"
		stringOut = exp
		return(stringOut)	
	if type(fminlist) == tuple:
		f1 = fminlist[0]
		f2 = fminlist[1]
		s1 = expression(f1,numVar) 
		s2 = expression(f2,numVar)
		b = s1.split("+")
		c = b.sort()
		s1 = "" 
		for i in b:
			s1 = s1 + i
			s1 = s1 + "+"
		s1 = s1[:-1]
		b = s2.split("+")
		c = b.sort()
		s2 = ""
		for i in b:
			s2 = s2 + i
			s2 = s2 + "+"
		s2 = s2[:-1]
		stringOut = s1 + " (or) "+ s2
		if len(fminlist) == 4:
			f3 = fminlist[2] ; s3 = expression(f3,numVar)
			f4 = fminlist[3] ; s4 = expression(f4,numVar)
			b = s3.split("+") 
			c = b.sort()
			s3 = ""
			for i in b:
				s3 = s3 + i
				s3 = s3 + "+"
			s3 = s3[:-1]
			b = s4.split("+") 
			c = b.sort()
			s4 = ""
			for i in b:
				s4 = s4 + i
				s4 = s4 + "+"
			s4 = s4[:-1]
			stringOut = s1 + " (or) "+ s2 + " (or) " + s3 + " (or) " + s4 
	else:
		s1 = expression(fminlist,numVar)
		a = s1.replace(" ","")
		b = a.split("+")
		c = b.sort()
		s1 = "" 
		for i in b:
			s1 = s1 + i
			s1 = s1 + "+"
		stringOut = s1[:-1]		
	return(stringOut)
