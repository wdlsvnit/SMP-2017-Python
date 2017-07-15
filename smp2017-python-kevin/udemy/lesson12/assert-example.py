traffic = { 'ns': 'green', 'ew': 'red' }

def Lights(traffic):
	for key in traffic.keys():
		if traffic[key] == 'green':
			traffic[key] = 'yellow'
		elif traffic[key] == 'yellow':
			traffic[key] = 'red'
		elif traffic[key] == 'red':
			traffic[key] = 'green'
	assert 'red' in traffic.values(), 'neither light is red!' + str(traffic)

Lights(traffic)           
