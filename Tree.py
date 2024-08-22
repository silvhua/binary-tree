import sys
sys.path.append(r"./utils")
from Custom_Logger import *
from copy import copy 
from random import randint, choice
from time import time

class Tree:
  def __init__(self, value, parent=None, messages=None, logger=None, logging_level='INFO'):
    self.logger = Custom_Logger(level=logging_level) if logger == None else logger
    self.left = None
    self.right = None
    self.value = value
    self.parent=parent
    self.logging_level=logging_level
    self.generation_dict = {value: 0}
    self.directions_dict = {}
    self.value_present = {}
    message = f'Creating child in {f"node {parent}" if parent else "root"} with value {value}.'

    if messages:
      messages.append(message)
      self.messages = messages
    else:
      self.messages = [message]

  def insert(self, value, show_log=False):
    """
    "Part 1 a) Insert a node to the binary tree"

    This assumes that the tree is a binary search tree, where :
    - each node's left child has a lower value
    - each node's right child has a higher value
    """
    if self.value == None:
      self.value = value
      self.logger.info(f'Inserted value {value} to node.')
    elif self.value > value:
      if self.left:
        self.left = self.left.insert(value)
      else:
        message = f'\nInserting {value} to left side.'
        self.messages.append(message)
        self.left = Tree(value, parent=self.value, messages=self.messages, logging_level=self.logging_level)
    elif self.value < value:
      if self.right:
        self.right = self.right.insert(value)
      else:
        message = f'\nInserting {value} to right side.'
        self.messages.append(message)
        self.right = Tree(value, parent=self.value, messages=self.messages, logging_level=self.logging_level)
    elif self.value == value:
      self.logger.warning(f'Value {value} already exists in tree.')
    if show_log:
      self.logger.info(' '.join(self.messages))
    return self
  
  def search(self, value, root=None, parent=None, generation=0, show_log=False):
    """
    Search for a node with the given value.

    This assumes that the tree is a binary search tree, where :
    - each node's left child has a lower value
    - each node's right child has a higher value
    """
    if root == None:
      root = copy(self)
      self.directions_dict[value] = []
    message = f'\n\tSearching for {value} in node {root.value}.'
    self.messages.append(message)
    if root.value == value:
      message = f'Value {value} found at generation {generation} in {f"parent {parent}" if parent else "root"}.'
      self.messages.append(message)
      self.generation_dict[value] = generation
      if show_log:
        self.logger.info(' '.join(self.messages))
      return root
    elif (root.value > value) & (root.left != None):
      generation += 1
      message = f'\nSearching left.'
      self.messages.append(message)
      self.directions_dict[value].append('left')
      result = self.search(value, root=root.left, parent=root.value, generation=generation, show_log=show_log)
      return result
    elif (root.value < value) & (root.right != None):
      generation += 1
      message = f'\nSearching right.'
      self.messages.append(message)
      self.directions_dict[value].append('right')
      result = self.search(value, root=root.right, parent=root.value, generation=generation, show_log=show_log)
      return result
    # if none of the above `if`/`elif` expressions are met, node has no children
    message = f'\nValue {value} does not exist in tree.'
    self.messages.append(message)
    if show_log:
      self.logger.info(' '.join(self.messages))
    return False
  
  def swap(self, value1, value2, show_log=False):
    """
    Part 1 b)	Swap two nodes on the binary tree
    """
    subtree1 = self.search(value1, show_log=False)
    subtree2 = self.search(value2, show_log=False)
    self.replace(value1, value2, show_log=False)
    self.replace(value2, value1, show_log=show_log)

  def replace(self, original_value, new_value, show_log=False):
    path = self.directions_dict[original_value]
    
    for index, attr in enumerate(path):
      if index == 0:
        node = self
      node = getattr(node, attr)
      if index == len(path) - 1:
        self.messages.append(f'\nValue {node.value} at index {index}.')
        node.value = new_value
        message = f'Changed node from value {original_value} to {new_value}.'
        self.messages.append(message)
    if show_log:
      self.logger.info(' '.join(self.messages))
    
  def contains_value(self, value, strategy='depth_first', max_nodes=100, show_log=False):
    if strategy == 'random':
      self.random_search(value, max_nodes, show_log)
    else:
      self.search_unsorted(value, strategy, show_log=show_log)
    if self.value_present.get(value):
      found = True
    else:
      message = f'\nValue {value} does not exist in tree.'
      self.messages.append(message)
      found = False
      self.messages.append(message)
    if show_log:
      self.logger.info(' '.join(self.messages))
    return found

  def search_unsorted(self, value, strategy, root=None, generation=0, show_log=False):
    """
    Given a tree whose elements are not ordered, search for a node with a given value.
    """
    if root == None:
      root = copy(self)
      self.directions_dict[value] = []
    if self.value_present.get(value) == True:
      return root
    if strategy in ['depth_first', 'dfs']:
      message = f'\n\tSearching for {value} in node {root.value}.'
      self.messages.append(message)
      if root.value == value:
        self.report_value_found(value, root, generation, show_log)
        return root
      if root.left:
        generation += 1
        message = f'\nSearching left.'
        self.messages.append(message)
        self.directions_dict[value].append('left')
        result = self.search_unsorted(value, root=root.left, strategy=strategy, generation=generation, show_log=show_log)
      if root.right:
        message = f'\nSearching right.'
        self.messages.append(message)
        self.directions_dict[value].append('right')
        result = self.search_unsorted(value, root=root.right, strategy=strategy, generation=generation, show_log=show_log)
    elif strategy in ['breadth_first', 'bfs']:
      if root == None:
        return
      elements = []
      elements.append(root)
      while (len(elements) > 0):
        if elements[0].value == value:
          self.report_value_found(value, elements[0], generation, show_log)
          return
        else:
          node = elements.pop(0)
          message = f'\n\tSearching for {value} in node {node.value}.'
          self.messages.append(message)
          if (node.left != None) | (node.right != None):
            generation += 1

          if node.left:
            message = f'\nSearching left.'
            self.messages.append(message)
            self.directions_dict[value].append('left')
            elements.append(node.left)
          if node.right:
            message = f'\nSearching right.'
            self.messages.append(message)
            self.directions_dict[value].append('right')
            elements.append(node.right)

  def random_search(self, value, max_nodes=100, show_log=False):
    """
    Traverse tree randomly until a node with the given value is found.

    Arguments:
      - value (int): Value to search for.
      - max_nodes (int): Max number of nodes to traverse to search for the value.
          If None, the search will continue indefinitely until the given value is found.
      - show_log (bool): Whether or not to show log statements to the console.
    """
    n_generations_to_traverse = randint(1, max_nodes) if max_nodes else 0
    message = f'Traversing {n_generations_to_traverse if max_nodes else "infinite"} generations to search for {value}.'
    self.messages.append(message)
    visited_nodes_values = []
    generation = 0
    current_generation = 0
    current_node = self
    while (max_nodes == None) | (current_generation < n_generations_to_traverse):
      generation += 1
      random_direction = choice(['right', 'left'])
      current_node = getattr(current_node, random_direction)
      if current_node:
        if current_node.value == value:
          self.report_value_found(value, current_node, generation, show_log)
          self.value_present[value] = True
          break
        else:
          visited_nodes_values.append(current_node.value)
          current_generation += 1
      else: # start back at root
        current_node = self
        generation = 0
    message = f'\n{len(visited_nodes_values)} nodes visited:\n' + ' '.join([str(value) for value in visited_nodes_values])
    self.messages.append(message)


  def report_value_found(self,value, node, generation=None, show_log=False):
    message = f'Value {value} found at generation {generation} in parent {node.value}.'
    self.value_present[value] = True
    self.messages.append(message)
    if show_log:
      self.logger.info(' '.join(self.messages))

def inorder(tree, result=None):
  """
  Part 1 c)	An algorithm to Sort the binary tree (https://en.wikipedia.org/wiki/Tree_sort)
  """
  if result == None:
    result = []
  if tree:
    inorder(tree.left, result=result)
    result.append(tree.value)
    inorder(tree.right, result=result)
  
  # Sort the list of elements in case the tree is not a binary search tree where the node value is always greater than the left child and less than the right child
  result = sorted(result)
  return result

def print_node(node):
  message = f"""
Node value: {node.value}. 
Left child value: {node.left.value if node.left else None}. 
Right child value: {node.right.value if node.right else None}.
  """
  print(message)

if __name__ == '__main__':

  # Set up the initial parameters
  logging_level='INFO'
  root_value = 10 
  target = 18
  max_nodes = None

  # a) Insert a node to the binary tree
  tree = Tree(root_value, logging_level=logging_level)
  tree.insert(5)
  tree.insert(15)
  tree.insert(12)
  tree.insert(18)
  print_node(tree)
  search_result = tree.search(target, show_log=True)

  # b)	Swap two nodes on the binary tree
  swap_result = tree.swap(12, 15, show_log=True)

  # c)	An algorithm to Sort the binary tree (https://en.wikipedia.org/wiki/Tree_sort)
  inorder(tree)



  # df_search_result = tree.contains_value(
  #   target, 'depth_first', show_log=True
  #   )
  # bf_search_result = tree.contains_value(
  #   target, 'breadth_first', show_log=True
  #   )
  # random_search_result = tree.contains_value(
  #   target, 'random', max_nodes=max_nodes, show_log=True
  #   )