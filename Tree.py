import sys
sys.path.append(r"../utils")
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
    n_generations_to_traverse = randint(1, max_nodes) if max_nodes else 0
    message = f'Traversing {n_generations_to_traverse if max_nodes else "infinite"} generations to search for {value}.'
    self.messages.append(message)
    # route = []
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
  Sort the elements of the tree. 
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

def get_list_of_unique_numbers(n_elements):
  max_value = n_elements * 5
  possible_values = [value for value in range(max_value)]
  result = []
  for index in range(n_elements):
    random_element = choice(possible_values)
    result.append(random_element)
    possible_values.remove(random_element)
  return result

def time_search(target, strategy, tree, max_nodes=None, logging_level='INFO', show_log=True):
  logger = Custom_Logger(f'{strategy}_logger', level=logging_level)
  tree.value_present[target] = False
  start_time = time()
  search_result = tree.contains_value(
    target, strategy, max_nodes=max_nodes, show_log=False
  )
  elapsed_time = time() - start_time
  if search_result:
    message = f'\nElapsed time for search: {elapsed_time}.'
  else:
    message = f'\nFailed to find {target} using "{strategy}" algorithm.'
    # If target value is not found, make elapsed time larger so it always ranks last compared with other algorithms
    elapsed_time += 999 
  if show_log:
    logger.info(message)
  return elapsed_time 

def compare_search_algorithms(tree_size):
  logger = Custom_Logger(f'compare_search_algorithms_logger', level='INFO')
  messages = []
  tree_elements = get_list_of_unique_numbers(tree_size)
  tree = Tree(tree_elements[0], logging_level='INFO')
  for element in tree_elements[1:]:
    tree.insert(element)
  target = choice(tree_elements)
  message = f'Tree of size: {tree_size}. \nValues range: {min(tree_elements)} - {max(tree_elements)}. Elements: {tree_elements}.\nTarget value: {target}.'
  messages.append(message)
  strategies = ['random', 'breadth_first', 'depth_first']
  elapsed_times = []
  for strategy in strategies:
    elapsed_time = time_search(target, strategy, tree, max_nodes=None, show_log=False)
    elapsed_times.append((strategy, elapsed_time))
  sorted_times = sorted(elapsed_times, key=lambda x: x[1])
  messages.append('Ranking of search algorithm search performance:')
  for strategy, time in sorted_times:
    message = f'\t{time if time < 999 else "failed search"}: {strategy}'
    messages.append(message)
  logger.info('\n'.join(messages))
  return tree

# logging_level='WARNING'
logging_level='INFO'
# logging_level='DEBUG'

# root_value = 10
# target = 180
# max_nodes = 200

# tree = Tree(root_value, logging_level=logging_level)
# tree.insert(5)
# tree.insert(15)
# tree.insert(12)
# tree.insert(18)

# print_node(tree)
# inorder(tree)
# search_result = tree.search(target, show_log=True)
# swap_result = tree.swap(12, 15, show_log=True)

# df_search_result = tree.contains_value(
#   target, 'depth_first', show_log=True
#   )
# bf_search_result = tree.contains_value(
#   target, 'breadth_first', show_log=True
#   )
# random_search_result = tree.contains_value(
#   target, 'random', max_nodes=max_nodes, show_log=True
#   )
tree = compare_search_algorithms(10000)
