import numpy as np


test_list=np.array([[0,1,0,0],
					[0,0,1,0],
					[1,0,0,0],
					[0,0,1,0]])




class graph:
	"""" search an adjacency list in a breadth first pattern"""
	def __init__(self, adjacency_list):
		self.adj_1 = adjacency_list
	def to_nodes(self, node):
		to_list = [y for y, x in enumerate(self.adj_1[node]) if x == 1]
		return to_list
	def from_nodes(self, node):
		from_list = [y for y, x in enumerate(self.adj_1[:,node]) if x == 1]
		return from_list
	def set_search(self, nodeA):
		self.visited_nodes = [nodeA]
		seeds = [node for node in self.to_nodes(nodeA)]
		self.paths = [[nodeA, x] for x in seeds]
		self.visited_nodes.extend(seeds)
	def find_path(self,nodeA,nodeB):
		self.set_search(nodeA)
		while len(self.paths) != 0:
			subject_path = self.paths.pop()
			new_nodes = self.to_nodes(subject_path[-1])
			if len(new_nodes) == 0:
				continue
			else:
				for node in new_nodes:
					new_path = subject_path
					new_path.append(node)
					if node == nodeB:
						return new_path
					elif node in self.visited_nodes:
						continue
					else:
						self.visited_nodes.append(node)
						self.paths.append(new_path)
		else:
			return False



test_run=graph(test_list)
test_run.find_path(3,1)


class bigraph(graph):
	""" search in a bidirectional manner """
	def set_bi_search(self, nodeA, nodeB):
		""" make the two starting path objects """
		self.visited_nodesA = [nodeA]
		self.visited_nodesB = [nodeB]

		A_seeds = [node for node in self.to_nodes(nodeA)]
		A_paths = [[nodeA, x] for x in A_seeds]
		B_seeds = [node for node in self.from_nodes(nodeB)]
		B_paths = [[nodeB, x] for x in B_seeds]
		self.visited_nodesA.extend(A_seeds)
		self.visited_nodesB.extend(B_seeds)
		self.paths = [A_paths, B_paths]
	
	def extend_paths(self, current_paths, direction):
		new_paths = []
		while len(current_paths) != 0:
			subject_path = current_paths.pop()
			if direction == 'to':
				new_nodes = self.to_nodes(subject_path[-1])
			elif direction == 'from':
				new_nodes = self.from_nodes(subject_path[-1])
			else:
				print('specify direction')
			if len(new_nodes) == 0:
				continue
			else:
				for node in new_nodes:
					new_path = subject_path
					new_path.append(node)
					if direction == 'to':
						if node in self.visited_nodesA:
							continue
						else:
							self.visited_nodesA.append(node)
							new_paths.append(new_path)
					elif direction == 'from':
						if node in self.visited_nodesB:
							continue
						else:
							self.visited_nodesB.append(node)
							new_paths.append(new_path)
		return new_paths

	def compare_paths(self, pathsA, pathsB):
		for x in pathsA:
			for y in pathsB:
				if x[-1] == y[-1]:
					best_path = x
					best_path.extend([z for z in reversed(y[:-1])])
					return best_path
				else:
					continue
		return False

	def next_level(self):
		""" extend the paths """
		A_next_levels = self.extend_paths(self.paths[0], 'to')
		intersection = self.compare_paths(A_next_levels,self.paths[1] )
		if intersection != False:
			return intersection
		B_next_levels = self.extend_paths(self.paths[1], 'from')
		""" alter the paths object """
		intersection2 = self.compare_paths(A_next_levels,B_next_levels)
		if intersection2 != False:
			return intersection2
		self.paths = [A_next_levels, B_next_levels]

	def find_path(self, nodeA, nodeB):
		""" find the best path through a double breadth search """
		self.set_bi_search(nodeA, nodeB)
		while (len(self.paths[0]) != 0) and (len(self.paths[1]) != 0):
			extend_compare = self.next_level()		
			""" extend the paths one level in both directions"""
			""" compatre the paths for intersection """
			if extend_compare != False:
				return extend_compare
		else:
			return False



test_run=bigraph(test_list)
test_run.find_path(3,1)







