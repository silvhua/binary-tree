import sys
sys.path.append(r"./utils")
sys.path.append(r"../") # required to run script in jupyter terminal
from Tree import *
from Custom_Logger import *
from copy import copy 
from random import randint, choice
from time import time
import numpy as np
import pandas as pd

class CompareAlgorithms:
  """
  d)	insert a large number of nodes into your tree (10,000; 100,000; 1,000,000), measure the performance of each of your 
  search algorithms (time to complete), comment on the Big O complexity of each (Best case, average case, worst case)
  """

  def __init__(self, tree_size, logging_level='INFO', show_log=False):
    self.logging_level = logging_level
    self.strategies = ['random', 'binary', 'breadth_first', 'depth_first']
    self.results_dict = {
      'random': [],
      'binary': [],
      'breadth_first': [], 
      'depth_first': [],
      'fastest': []
    }
    self.tree_size = tree_size
    self.show_log = show_log

  def get_list_of_unique_numbers(self):
    max_value = self.tree_size * 5
    possible_values = [value for value in range(max_value)]
    elements = []
    for index in range(self.tree_size):
      random_element = choice(possible_values)
      elements.append(random_element)
      possible_values.remove(random_element)
    return elements

  def time_search(self, target, strategy, max_nodes=None):
    logger = Custom_Logger(f'{strategy}_logger', level=self.logging_level)
    self.tree.value_present[target] = False
    start_time = time()
    # print(f'Starting search for {strategy} strategy (timestamp: {start_time})')
    search_result = self.tree.contains_value(
      target, strategy, max_nodes=max_nodes, show_log=False
    )
    elapsed_time = time() - start_time
    if search_result:
      message = f'\nElapsed time for search: {elapsed_time}.'
    else:
      message = f'\nFailed to find {target} using "{strategy}" algorithm.'
      print(message)
      # If target value is not found, make elapsed time larger so it always ranks last compared with other algorithms
      elapsed_time = np.nan 
    if self.show_log:
      logger.info(message)
    return elapsed_time 

  def compare_search_algorithms(self, max_nodes=100000):
    """
    Compare the 3 algorithms by searching for the same element in the same tree.
    """
    self.logger = Custom_Logger(f'compare_search_algorithms_logger', level=self.logging_level)
    messages = []
    tree_elements = self.get_list_of_unique_numbers()
    self.tree = Tree(tree_elements[0], logging_level='INFO')
    for element in tree_elements[1:]:
      self.tree.insert(element)
    target = choice(tree_elements)
    message = f'Tree of size: {self.tree_size}. \nValues range: {min(tree_elements)} - {max(tree_elements)}. Elements: {tree_elements}.\nTarget value: {target}.'
    messages.append(message)
    elapsed_times = []
    for strategy in self.strategies:
      elapsed_time = self.time_search(target, strategy, max_nodes=max_nodes)
      elapsed_times.append((strategy, elapsed_time))
      self.results_dict[strategy].append(elapsed_time)
    sorted_times = sorted(elapsed_times, key=lambda x: x[1] if not np.isnan(x[1]) else float('inf'))
    fastest = sorted_times[0][0]
    self.results_dict['fastest'].append(fastest)
    if self.show_log:
      self.logger.info('\n'.join(messages))
  
  def run_experiment(self, n_trials, max_nodes=100000):
    """
    Compare the 3 search algorithm over multiple trials (n_trials) to take the mean search time.
    To determine which algorithms are significantly different from each other with greater confidence, 
    you would also perform statistical tests (e.g. one-way ANOVA followed by posthoc testing)
    on the resulting data 
    """
    message = f'Running {n_trials} trials using trees with {self.tree_size} elements each.'
    for trial in range(n_trials):
      self.compare_search_algorithms(max_nodes=max_nodes)
    results_df = pd.DataFrame(self.results_dict)
    results_df.index.name = 'trial'
    print('\nResults sorted by average elapsed time:')
    print(results_df[['random', 'binary', 'breadth_first', 'depth_first']].mean().sort_values())
    print('\nCount of fastest algorithm:')
    print(results_df['fastest'].value_counts())
    return results_df
    

if __name__ == '__main__':

  ##################################################
  # UPDATE THIS IF NEEDED TO REDUCE RUN TIME: 
  # #Number of trials to perform
  n_trials = 30

  # Maximum number of nodes to traverse for brute force (random) search algorithm 
  max_nodes = 1000000

  ##################################################

  # Number of tree nodes
  tree_size = 10000

  logging_level='INFO'

  comparator = CompareAlgorithms(
    tree_size=tree_size,
    logging_level=logging_level
    )
  results = comparator.run_experiment(n_trials, max_nodes=max_nodes)
  print('\nAll data:\n', results)