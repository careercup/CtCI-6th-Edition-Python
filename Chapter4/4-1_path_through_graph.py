import numpy as np


test_list=np.array([[0,1,0,0],
					[0,0,1,0],
					[1,0,0,0],
					[0,0,1,0]])




class graph:
	def __init__(self, adjacency_list):
		self.adj_1 = adjacency_list
	def to_nodes(self, node):
		to_list = [y for y, x in enumerate(self.adj_1[node]) if x == 1]
		return to_list
	def from_nodes(self, node):
		from_list = [y for y, x in enumerate(self.adj_1[:,node]) if x == 1]
		return from_list
	def find_path(self,nodeA,nodeB):
		self.visited_nodes = [nodeA]
		seeds = [node for node in self.to_nodes(nodeA)]
		self.paths = [[x] for x in seeds]
		self.visited_nodes.extend(seeds)
		self.dead_ends = []
		while True:
			if len(self.paths) == 0:
				break
			subject_path = self.paths.pop()
			print(subject_path)
			print(self.paths)
			new_nodes = self.to_nodes(subject_path[-1])
			if len(new_nodes) == 0:
				self.dead_ends.append(subject_path)
				continue
			else:
				for node in new_nodes:
					new_path = subject_path
					new_path.append(node)
					print(new_path)
					if node == nodeB:
						return new_path
					elif node in self.visited_nodes:
						self.dead_ends.append(new_path)
					else:
						self.visited_nodes.append(node)
						self.paths.append(new_path)
		else:
			return False



test_run=graph(test_list)
test_run.find_path(3,1)

