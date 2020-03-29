# NAME : LARIKA SEHGAL
# ROLL. NO: 2018243
# SECTION : B
# GROUP : 4
import math
import matplotlib.pyplot
def matrix_multiplication(A,B):
	#A and B are our matrices which are to be multioplied
	#A is the transformation matrix and B is the input matrix consisting of the verices of the polygon
	if type(B[0])==list:
		M=[] # the matrix contained from multiplication
		for i in A:
			l = []
			for j in range(len(B[0])):
				count = 0
				for k in range(len(A[0])):
					a=B[k][j]
					b=i[k]
					count+=a*b
				l.append(count)
			M.append(l)		
		return(M)
	else:
		print("hi")
		M=[]
		for i in A:
			count = 0
			for j in range(len(A[0])):
				b = i[j]
				a = B[j]
				count += a*b
			M.append(count)
		return(M)
def scaling(s,command,M,h,k,r1,r2):
	sx = int(command[1])
	sy = int(command[2])
	scaling_matrix = [[sx,0,0],[0,sy,0],[0,0,1]]	
	if s == "polygon":
		output=matrix_multiplication(scaling_matrix,M)
		print(output[0],output[1])	#the new xcord and ycord list
		M = output
		return(M,h,k,r1,r2)
	if s == "disc":
		if h ==0 and k==0:
			output=matrix_multiplication(scaling_matrix,M)
			d1 = sx*r1 ; d2 = sy*r2
			print(h,k,d1,d2)
			M = output
			return(M,h,k,d1,d2)
		else:
			return(M)
def rotation(s,command,M,h,k,r1,r2):
	x = float(command[1])
	sinx = math.sin(math.radians(x))
	cosx = math.sin(math.radians(90) - math.radians(x)) 
	rotate_matrix = [[cosx,-sinx,0],[sinx,cosx,0],[0,0,1]]	
	if s == "polygon":
		output = matrix_multiplication(rotate_matrix,M)
		print(output[0],output[1])	#the new xcord and ycord list
		M = output
		return(M,h,k)
	if s == "disc":
		output = matrix_multiplication(rotate_matrix,M)
		m = [h,k,1]
		print(m)
		x = matrix_multiplication(rotate_matrix,m)
		h1 = x[0] ; k1 = x[1]
		print(h1,k1,r,r)
		M = output
		return(M,h1,k1)
def translate(s,command,M,h,k,r1,r2):
	#finding translate_matrix
	tx = int(command[1])
	ty = int(command[2])
	translate_matrix = [[1,0,tx],[0,1,ty],[0,0,1]] 
	output = matrix_multiplication(translate_matrix,M)		
	if s == "polygon":
		print(output[0],output[1])	#the new xcord and ycord list
		M = output
		return(M,h,k)
	if s == "disc":
		h1 = h+tx ; k1 = k+ty
		print(h1,k1,r,r)
		M = output
		return(M,h1,k1)
def LT(s,xcord,ycord,h,k,r):
	M = []	# the 3x n matrix containing ccoordinates, ycoordinates matrix
	M.append(xcord) ; M.append(ycord)
	l = []
	a = len(xcord)
	for i in range(len(xcord)):
		l.append(1)
	M.append(l)
	command = "hi"	
	r1 = r ; r2 = r 		#by default the radii r1,r2 are equal to r i.e circle/disc
	while command != "quit":	#till the user stops		
		if command[0] == "S":	#The command for scalling
			command=command.split(" ")
			if h == 0 and k == 0:
				Z = scaling(s,command,M,h,k,r1,r2)
				d1 = Z[3] ; r1 = d1
				d2 = Z[4] ; r2 = d2
				M = Z[0]
				h1 = Z[1] ; h = h1
				k1 = Z[2] ; k = k1
		if command[0] == "R":	# The command for rotating
			command = command.split(" ")
			Z = rotation(s,command,M,h,k,r1,r2)
			h1 = Z[1]
			k1 = Z[2]
			M = Z[0]
			h = h1  ; k = k1 
		if command[0] == "T":	# The command for translate
			command = command.split(" ")
			Z = translate(s,command,M,h,k,r1,r2)
			h1 = Z[1]			
			k1 = Z[2]			
			M = Z[0]			
			h = h1 ; k = k1
		x = M[0] + [M[0][0]] ; y = M[1] +[M[1][0]]
		matplotlib.pyplot.ion()
		matplotlib.pyplot.plot(x,y)		
		matplotlib.pyplot.show()
		command = input()
		matplotlib.pyplot.clf()		
s = input()
if s == "polygon":
	x = input().split(" ")
	y = input().split(" ")
	xcord = [] ; ycord = []
	for i in x:
		a = int(i)
		xcord.append(a)
	for i in y:
		a = int(i)
		ycord.append(a)
	h = 0 ; k = 0 ; r = 0
if s == "disc":
	i = input().split(" ")
	h = int(i[0]) ; k = int(i[1]) ; r = int(i[2])	# here (h,k) is the center and r is the radius	
	xcord = [] ; ycord = []
	for i in range (0,1500):
		theta = (math.pi/750)*i
		sintheta = math.sin(theta)
		costheta = math.sin(math.radians(90)-theta) 
		x = h + r*costheta ; y = k + r*sintheta 		
		xcord.append(x)
		ycord.append(y)
print(LT(s,xcord,ycord,h,k,r))
