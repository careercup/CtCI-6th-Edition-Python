
class parking_space():
	def __init__(self, space):
		self.location = space
		self.status = 'empty'
	def enter(self, car):
		self.status = car
	def leave(self):
		self.status = 'empty'

class car():
	def __init__(self, license):
		self.name = license
	def find_spot(self, parking_lot):
		""" look through the parking lot, park in first avaliable spot """
		for num in parking_lot.keys():
			if parking_lot[num].status == 'empty':
				self.park(parking_lot[num])
				return '%s parked in %s' % (self.name, parking_lot[num].location)
			else:
				continue
			return 'lot is full, wait then try again!'
	def park(self, parking_spot):
		""" put the car in the spot, create object connections """
		parking_spot.enter(self)
		self.location = parking_spot
		
	def depart(self):
		""" undo the connections produced by park """
		self.location.status = 'empty'
		self.location = 0






if __name__ == '__main__':

parking_spaces = {}

list_of_lanes = ['A','B','C','D','E','F','G','H']

""" track the number of total spots, zero indexed """
p_counter = 0
#build the dict of spots
for i in list_of_lanes:
	for j in range(1,9):
		parking_spaces[p_counter]= parking_space((i,j))
		p_counter += 1

