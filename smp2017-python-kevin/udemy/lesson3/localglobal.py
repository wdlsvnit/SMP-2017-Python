def fun1():	
	bob=100	
	print(bob)

def fun2():
	print(bob)

def fun3():
	global bob
	bob = 100	
	print(bob)

bob=121

print('Fuction 1')
fun1()
print(bob)

print('Fuction 2')
fun2()
print(bob)

print('Fuction 3')
fun3()
print(bob)

