import collections

names = {
		"john":10,\
		"jon":3,\
		"davis":2,\
		"kari":3,\
		"johny":11,\
		"carlton":8 ,\
		"carleton":2,\
		"jonathan":9,\
		"carrie":5

}

pairs = [["jonathan","john"],["jon","johny"],["johny","john"],["kari","carrie"],["carleton","carlton"]]

parent = {}
for name in names.keys():
	parent[name] = name

#find operation
def find(x):
	if parent[x]!=x:
		parent[x]=find(parent[x])
	return parent[x]
#union operation
def union(x1,x2):
	r1 = find(x1)
	r2 = find(x2)
	if r1!=r2:
		parent[r1]=r2
res = collections.defaultdict(int)
for pair in pairs:
	union(pair[0],pair[1])

for key in parent.keys():
	#find root of cluster
	root = find(key)
	res[root]+=names[key]
print(res)
