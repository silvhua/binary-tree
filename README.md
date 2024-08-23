# Binary Tree Problem Set
## Problem #1

>A binary tree is a data structure where each node in the tree has two, one, or no, children nodes.
>Implement a binary tree data structure with the following functions:
>
>a)	Insert a node to the binary tree
>
>b)	Swap two nodes on the binary tree
>
>c)	An algorithm to Sort the binary tree (https://en.wikipedia.org/wiki/Tree_sort)
>
>d)	Remove a node from the binary tree without breaking the remaining tree structure


Run the following in the terminal for a demo of all the tasks in Problem #1.

```
python Tree.py
```
Note: You can update the parameters in the script to reduce script execution time.

The code is found in `Tree.py`.




## Problem #2
>Using your tree from Problem #1, 
>
>a. Implement a brute force search algorithm
>
>b. implement a depth-first search algorithm
>
>c. implement a breadth first search algorithm
>
>d. insert a large number of nodes into your tree (10,000; 100,000; 1,000,000), measure the performance of each of your search algorithms (time to complete), comment on the Big O complexity of each (Best case, average case, worst case)

**Note**: I assumed that "brute force search" meant traversing the tree randomly. I also implemented a binary search tree algorithm.

Run the following in the terminal for a demo of all the tasks in Problem #2.

```
python CompareAlgorithms.py
```

Note that you may need to install the `pandas` package to run the script. This can be done with one the the following Python package managers:
* `pip install pandas` if `pip` is installed
* `conda install pandas` if Anaconda is installed

The code is found in `CompareAlgorithms.py` as well as in `Tree.py`.

## Big O complexity

Algorithm | Worst Case | Best Case | Average Case
--- | ---- | --- | ---
random search | infinity; <br>probability-wise, $$O(\log_2(N+1) \times \frac{N + 1}{2})$$ | `O(1)` | $$O(\log_2(N+1) \times \frac{N + 1}{4})$$ 
binary tree search | `O(log N)` | `O(1)` | `O((log N) / 2)`
depth-first search | `O(N)` | `O(1)` | `O(N/2)`
breadth-first search | `O(N)` | `O(1)` | `O(N/2)`

### Best case

For all algorithms, the best case is when the target value is in the root node.

### Worst case

For depth-first search and breadth-first search, the worst case is when  the target value is 
found in the last visited node. In this case, time complexity is `O(N)`.

For random search, the algorithm is such that once a leaf node is reached, the search returns to the root node. Each node may be visited multiple times. There is a small chance that the node is never found. The probability that the node is found:
* Decreases as the tree size increases.
* Increases with the number of steps made (1 step is a traversal between parent-child nodes pair).
* Increases for every node that has 2 children. In the edge case where each child only has one node, worst-case time complexity is `O(N)`.

In a balanced tree, based on probability, the target value should be found by the time the number of steps made is equal to the product of:
* tree height (number of steps until a leaf node is reached): $$\log_2(N+1)$$
* number of nodes at the highest level (possible routes between the root and a leaf node): $$\frac{N + 1}{2}$$

For binary tree search, the number of nodes visited is halved as it traverses the tree, which is why it has the lowest time complexity.

### Average case
For depth-first search and breadth-first search, we can assume that the tree is balanced and that on average, the target value is in the middle of the node tranversal sequence; thus, time complexity is half of the worst case scenario except for in random search.

## Experimental methods

Below are the results of an experiment to compare the 4 above search algorithms. Each trial used a randomly generated binary search tree. The target value was randomly picked from the set of tree elements.

Experiment parameters:
* Tree size: 10,000
* 30 trials

## Results

### All algorithms

The binary search tree algorithm consistently performed the best out of all algorithms. Below are the mean search times:




<details>
<summary>Code</summary>

```Python
import sys
sys.path.append(r"../")
from CompareAlgorithms import *

if __name__ == '__main__':

  ##################################################
  # UPDATE THIS IF NEEDED TO REDUCE RUN TIME: 
  # #Number of trials to perform
  n_trials = 30

  # Maximum number of nodes to traverse for brute force (random) search algorithm 
  max_nodes = 100000000

  ##################################################

  # Number of tree nodes
  tree_size = 10000

  logging_level='INFO'

  comparator = CompareAlgorithms(
    tree_size=tree_size,
    logging_level=logging_level
    )
  results = comparator.run_experiment(n_trials, max_nodes=max_nodes)

print()
results[['random', 'binary', 'breadth_first', 'depth_first']].mean().sort_values()
```
</details>
    
    




    binary           0.000133
    depth_first      0.009137
    breadth_first    0.013585
    random           2.568950
    dtype: float64




Below are the raw data with time shown in seconds. 

Note: `NaN` indicates that the target value was not found within the step limit.


<details>
<summary>Code</summary>

```Python
results.index.name = None
results
```
</details>



<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>random</th>
      <th>binary</th>
      <th>breadth_first</th>
      <th>depth_first</th>
      <th>fastest</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.159719</td>
      <td>0.000000</td>
      <td>0.018732</td>
      <td>0.011414</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.802768</td>
      <td>0.000000</td>
      <td>0.036582</td>
      <td>0.016001</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.350202</td>
      <td>0.000000</td>
      <td>0.007276</td>
      <td>0.014031</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.520093</td>
      <td>0.000000</td>
      <td>0.003284</td>
      <td>0.010039</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.617885</td>
      <td>0.000000</td>
      <td>0.025705</td>
      <td>0.009261</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.271080</td>
      <td>0.000000</td>
      <td>0.007992</td>
      <td>0.018224</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.043975</td>
      <td>0.000000</td>
      <td>0.003999</td>
      <td>0.014968</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>7</th>
      <td>4.221317</td>
      <td>0.000000</td>
      <td>0.021878</td>
      <td>0.003766</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>8</th>
      <td>10.339950</td>
      <td>0.000000</td>
      <td>0.027486</td>
      <td>0.014628</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.030252</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.019180</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>0.000000</td>
      <td>0.023269</td>
      <td>0.016482</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>11</th>
      <td>10.359279</td>
      <td>0.000999</td>
      <td>0.015994</td>
      <td>0.007000</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.009047</td>
      <td>0.000000</td>
      <td>0.005243</td>
      <td>0.006081</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.022374</td>
      <td>0.000000</td>
      <td>0.001670</td>
      <td>0.009537</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.847556</td>
      <td>0.000000</td>
      <td>0.010731</td>
      <td>0.001565</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.330954</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.013078</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.503806</td>
      <td>0.000000</td>
      <td>0.010399</td>
      <td>0.007013</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.012894</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.006108</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.241606</td>
      <td>0.000000</td>
      <td>0.009974</td>
      <td>0.000921</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.013314</td>
      <td>0.000000</td>
      <td>0.004017</td>
      <td>0.007158</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.986308</td>
      <td>0.000000</td>
      <td>0.004518</td>
      <td>0.011318</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.025534</td>
      <td>0.000000</td>
      <td>0.005633</td>
      <td>0.011049</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.061022</td>
      <td>0.000000</td>
      <td>0.008070</td>
      <td>0.002116</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NaN</td>
      <td>0.003000</td>
      <td>0.041651</td>
      <td>0.005321</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.010779</td>
      <td>0.000000</td>
      <td>0.011036</td>
      <td>0.002024</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>25</th>
      <td>9.858027</td>
      <td>0.000000</td>
      <td>0.008585</td>
      <td>0.011089</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0.098731</td>
      <td>0.000000</td>
      <td>0.009045</td>
      <td>0.000954</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>27</th>
      <td>3.706781</td>
      <td>0.000000</td>
      <td>0.020887</td>
      <td>0.009054</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>28</th>
      <td>15.450262</td>
      <td>0.000000</td>
      <td>0.049627</td>
      <td>0.004097</td>
      <td>binary</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2.035090</td>
      <td>0.000000</td>
      <td>0.014256</td>
      <td>0.010628</td>
      <td>binary</td>
    </tr>
  </tbody>
</table>
</div>



### Algorithms other than binary tree search

When the results from the binary tree search algorithm are ignored, we see that:
* The random search algorithm performed the worst and was never the best performing algorithm.
* Depth-first search and breadth-first search performed similarly. Depth-first search performed the best over half of the time (17 out of 30).


<details>
<summary>Code</summary>

```Python
def find_fastest(row):
  # print(f'row: {row.name}, {row.index}')
  sorted = row.sort_values()
  return sorted.index[0]

results_without_binary = results.loc[:, ['random', 'breadth_first', 'depth_first']]
results_without_binary['fastest'] = results_without_binary.apply(lambda x: find_fastest(x), axis=1)
results_without_binary.index.name = None
results_without_binary
```
</details>



<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>random</th>
      <th>breadth_first</th>
      <th>depth_first</th>
      <th>fastest</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.159719</td>
      <td>0.018732</td>
      <td>0.011414</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.802768</td>
      <td>0.036582</td>
      <td>0.016001</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.350202</td>
      <td>0.007276</td>
      <td>0.014031</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.520093</td>
      <td>0.003284</td>
      <td>0.010039</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3.617885</td>
      <td>0.025705</td>
      <td>0.009261</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.271080</td>
      <td>0.007992</td>
      <td>0.018224</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.043975</td>
      <td>0.003999</td>
      <td>0.014968</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>7</th>
      <td>4.221317</td>
      <td>0.021878</td>
      <td>0.003766</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>8</th>
      <td>10.339950</td>
      <td>0.027486</td>
      <td>0.014628</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.030252</td>
      <td>0.000000</td>
      <td>0.019180</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>10</th>
      <td>NaN</td>
      <td>0.023269</td>
      <td>0.016482</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>11</th>
      <td>10.359279</td>
      <td>0.015994</td>
      <td>0.007000</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.009047</td>
      <td>0.005243</td>
      <td>0.006081</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.022374</td>
      <td>0.001670</td>
      <td>0.009537</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.847556</td>
      <td>0.010731</td>
      <td>0.001565</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.330954</td>
      <td>0.000000</td>
      <td>0.013078</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.503806</td>
      <td>0.010399</td>
      <td>0.007013</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.012894</td>
      <td>0.000000</td>
      <td>0.006108</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.241606</td>
      <td>0.009974</td>
      <td>0.000921</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.013314</td>
      <td>0.004017</td>
      <td>0.007158</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.986308</td>
      <td>0.004518</td>
      <td>0.011318</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.025534</td>
      <td>0.005633</td>
      <td>0.011049</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.061022</td>
      <td>0.008070</td>
      <td>0.002116</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>23</th>
      <td>NaN</td>
      <td>0.041651</td>
      <td>0.005321</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.010779</td>
      <td>0.011036</td>
      <td>0.002024</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>25</th>
      <td>9.858027</td>
      <td>0.008585</td>
      <td>0.011089</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0.098731</td>
      <td>0.009045</td>
      <td>0.000954</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>27</th>
      <td>3.706781</td>
      <td>0.020887</td>
      <td>0.009054</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>28</th>
      <td>15.450262</td>
      <td>0.049627</td>
      <td>0.004097</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2.035090</td>
      <td>0.014256</td>
      <td>0.010628</td>
      <td>depth_first</td>
    </tr>
  </tbody>
</table>
</div>




Count of fastest algorithm across all trials:


<details>
<summary>Code</summary>

```Python
summary_without_binary = pd.DataFrame(results_without_binary['fastest'].value_counts())
summary_without_binary.index.name = None
summary_without_binary
```
</details>



<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>depth_first</th>
      <td>17</td>
    </tr>
    <tr>
      <th>breadth_first</th>
      <td>13</td>
    </tr>
  </tbody>
</table>
</div>



## Discussion and conclusion

If searching binary trees that are not sorted (i.e. not binary search trees), the binary search tree algorithm would not work. The binary search tree algorithm should be implemented if the binary tree meets the criteria for a binary search tree.

Depth-first search and breadth-first search perform about equally well when information about node location is unknown. To determine if these algorithms are significantly different eachother, one could perform statistical tests (e.g. one-way ANOVA followed by posthoc testing) on data collected across all trials. 

If node location is known, search algorithm selection can be made accordingly.
