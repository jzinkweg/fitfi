class Tree(object):
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.data = None

    def __str__(self):
        return str(self.data) + " left: " + str(self.left) + ", right: " + str(self.right)

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
    if root.data:
        cost = root_cost + root.data.get('duration', 0)
    else:
        cost = root_cost

    leafs = []
    if root.left:
        leafs += find_leafs(root.left, cost)

    if root.right:
        leafs += find_leafs(root.right, cost)

    if not root.left and not root.right:
        leafs += (root.data, cost)

    return leafs

for task in tasks:
    if task.get('node', None) == None:
      task['node'] = Tree()
      task['node'].data = task
    for dep in task['depends']:
      depTask = find_def(tasks, dep)
      if depTask.get('node', None) == None:
        depTask['node'] = Tree()
        depTask['node'].data = depTask
      if task['node'].left == None:
         task['node'].left = depTask['node']
         depTask['node'].parent = task['node']
      elif task['node'].right == None:
         task['node'].right = depTask['node']
         depTask['node'].parent = task['node']
      else:
         extraNode = Tree()
         extraNode.parent = task['node']
         extraNode.left = task['node'].right
         task['node'].right.parent = extraNode
         task['node'].right = extraNode
         extraNode.right = depTask['node']
         depTask['node'].parent = extraNode

root = tasks[0]['node']
leafs = find_leafs(root, 0)

print leafs
