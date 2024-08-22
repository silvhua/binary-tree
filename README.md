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
python ../Tree.py
```


The code is found in `Tree.py`



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

Run the following in the terminal for a demo of all the tasks in Problem #2.

```
python CompareAlgorithms.py
```

Note that you may need to install the `pandas` package to run the script. This can be done with one the the following:
* `pip install pandas` if `pip` is installed
* `conda install pandas` if Anaconda is installed

The code is found in `CompareAlgorithms.py` as well as in `Tree.py`.

To determine which algorithms are significantly different from each other with greater confidence, 
you would also perform statistical tests (e.g. one-way ANOVA followed by posthoc testing)
on the resulting data
