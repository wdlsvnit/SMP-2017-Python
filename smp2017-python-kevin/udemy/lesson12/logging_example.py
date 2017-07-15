import logging

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

def fact(n):
	logging.debug('Start of factorial:%s'%n)
	total = 1
	for i in range(1,n+1):
		total*=i
		logging.info('i is %s, total is %s' %(i,total))
	
	logging.debug('Return value:%s'%total)
	return total

print(fact(4))

logging.debug('EOpgm')
