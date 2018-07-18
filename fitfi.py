class Tree(object):
    def __init__(self):
        self.parent = None
        self.children = list()
        self.data = None

    def done(self):
        return self.data.get('done', False)

    def children_done(self):
        for child in self.children:
            if not child.done():
                return False
        return True

    def __str__(self):
        return str(self.data) + " : " + str(self.children) + ""

    def __repr__(self):
        return self.__str__()

    def add_child(self, node):
        self.children.append(node)

tasks = [{'id': 'schroten', 'depends': ['weighed-stuff'], 'requires': ['malt-mill', 'bucket'], 'duration': 10},
        {'id': 'weighed-stuff', 'depends': ['weighed-pils', 'weighed-munich'], 'requires': ['weigher', 'scoop']},
        {'id': 'weighed-munich', 'depends': [], 'requires': ['munich'], 'duration': 1},
        {'id': 'weighed-pils', 'depends': [], 'requires': ['pils'], 'duration': 2}]

def find_def(lijstje, key):
    for t in lijstje:
        if t['id'] == key:
            return t
    return None

def find_leafs(root, root_cost):
    cost = root_cost + root.data.get('duration', 0)

    leafs = []
    if root.done():
        return leafs

    for child in root.children:
        leafs += find_leafs(child, cost)

    if not leafs:
        leafs += (root.data, cost)

    return leafs

for task in tasks:
    if task.get('node', None) == None:
      task['node'] = Tree()
      task['node'].data = task
    for dep in task['depends']:
      depTask = find_def(tasks, dep)
      depTask['node'] = Tree()
      depTask['node'].data = depTask
      depTask['node'].parent = task['node']
      task['node'].add_child(depTask['node'])

root = tasks[0]['node']

leafs = find_leafs(root, 0)

print leafs
