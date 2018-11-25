class Project:
  def __init__(self, name):
    self.name = name
    self.children = []
    self.nb_dependency = 0

class Graph:
  def __init__(self):
    self.projects = []

  def add_project(self, name):
    new = Project(name)
    self.projects.append(new)
    return new

  def add_dependency(self, a, b):
    b.nb_dependency +=1
    a.children.append(b)


def build_order(graph):
  n = len(graph.projects)
  order = n * [None]
  offset = addnondependent(order,graph.projects,0)
  tobeprocessed = 0
  while tobeprocessed < n :
    current = order[tobeprocessed]
    if not current:
      raise Excecption("the project cannot be built")
    for child in current.children:
      child.nb_dependency -= 1
    offset = addnondependent(order, current.children, offset)
    tobeprocessed += 1
  return order

def addnondependent(order, projects, offset):
  for p in projects:
    if p.nb_dependency == 0:
      order[offset] = p
      offset += 1
  return offset   


graph = Graph()

a = graph.add_project("a")
b = graph.add_project("b")
c = graph.add_project("c")
d = graph.add_project("d")
e = graph.add_project("e")
f = graph.add_project("f")
g = graph.add_project("g")

graph.add_dependency(f,a)
graph.add_dependency(f,b)
graph.add_dependency(f,c)


graph.add_dependency(b,e)
graph.add_dependency(b,a)

graph.add_dependency(c,a)

graph.add_dependency(a,e)

graph.add_dependency(d,g)

order = build_order(graph)
print([p.name for p in order])
