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

## Experiment results

Experiment parameters:
* Tree size: 10,000
* 50 trials

### Summary


<details>
<summary>Code</summary>

```Python
summary = pd.DataFrame(results['fastest'].value_counts())
summary.index.name = None
summary
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
      <td>36</td>
    </tr>
    <tr>
      <th>breadth_first</th>
      <td>13</td>
    </tr>
    <tr>
      <th>random</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>


### Raw data

Time is shown in seconds


<details>
<summary>Code</summary>

```Python
results
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
    <tr>
      <th>trial</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>132.818496</td>
      <td>0.045720</td>
      <td>0.012662</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.016872</td>
      <td>0.002001</td>
      <td>0.006592</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.199031</td>
      <td>0.009146</td>
      <td>0.005009</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.095326</td>
      <td>0.009473</td>
      <td>0.007019</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14.676934</td>
      <td>0.007137</td>
      <td>0.000000</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.670573</td>
      <td>0.011362</td>
      <td>0.008693</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.111632</td>
      <td>0.007967</td>
      <td>0.004228</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.632179</td>
      <td>0.008631</td>
      <td>0.008754</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.682468</td>
      <td>0.011561</td>
      <td>0.010052</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.008077</td>
      <td>0.001682</td>
      <td>0.014272</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.301640</td>
      <td>0.005000</td>
      <td>0.001510</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.712716</td>
      <td>0.010731</td>
      <td>0.011450</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>12</th>
      <td>208.580028</td>
      <td>0.080353</td>
      <td>0.004998</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.148526</td>
      <td>0.003008</td>
      <td>0.005420</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2.001810</td>
      <td>0.015203</td>
      <td>0.001998</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>15</th>
      <td>16.364257</td>
      <td>0.009711</td>
      <td>0.005025</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.075880</td>
      <td>0.004000</td>
      <td>0.002946</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.013624</td>
      <td>0.002998</td>
      <td>0.003329</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1.052521</td>
      <td>0.010382</td>
      <td>0.002000</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.283590</td>
      <td>0.009389</td>
      <td>0.007522</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.088684</td>
      <td>0.002994</td>
      <td>0.002008</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>21</th>
      <td>7.951844</td>
      <td>0.010002</td>
      <td>0.001001</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.541047</td>
      <td>0.013502</td>
      <td>0.006452</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.029864</td>
      <td>0.002998</td>
      <td>0.011707</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.046217</td>
      <td>0.006987</td>
      <td>0.004058</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>25</th>
      <td>5.326335</td>
      <td>0.012105</td>
      <td>0.006093</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0.408940</td>
      <td>0.009268</td>
      <td>0.007550</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>27</th>
      <td>17.198798</td>
      <td>0.009989</td>
      <td>0.005008</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>28</th>
      <td>12.152348</td>
      <td>0.044939</td>
      <td>0.008737</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>29</th>
      <td>28.591341</td>
      <td>0.054369</td>
      <td>0.008000</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>30</th>
      <td>1.455813</td>
      <td>0.013281</td>
      <td>0.011152</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>31</th>
      <td>0.045278</td>
      <td>0.000868</td>
      <td>0.000000</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>32</th>
      <td>0.026372</td>
      <td>0.008519</td>
      <td>0.000519</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>33</th>
      <td>0.930354</td>
      <td>0.012005</td>
      <td>0.008398</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2.244429</td>
      <td>0.031994</td>
      <td>0.011005</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>35</th>
      <td>0.059901</td>
      <td>0.008066</td>
      <td>0.002047</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>36</th>
      <td>22.743219</td>
      <td>0.039224</td>
      <td>0.012195</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>37</th>
      <td>0.964319</td>
      <td>0.011958</td>
      <td>0.000999</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>38</th>
      <td>0.069916</td>
      <td>0.010198</td>
      <td>0.010662</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>39</th>
      <td>0.101052</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>40</th>
      <td>5.629613</td>
      <td>0.007211</td>
      <td>0.019990</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>41</th>
      <td>8.017100</td>
      <td>0.008277</td>
      <td>0.002138</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>42</th>
      <td>0.003186</td>
      <td>0.000550</td>
      <td>0.000000</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>43</th>
      <td>2.990086</td>
      <td>0.009069</td>
      <td>0.000000</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>44</th>
      <td>0.000551</td>
      <td>0.000000</td>
      <td>0.000913</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>45</th>
      <td>0.000000</td>
      <td>0.008536</td>
      <td>0.000000</td>
      <td>random</td>
    </tr>
    <tr>
      <th>46</th>
      <td>0.270985</td>
      <td>0.009236</td>
      <td>0.000967</td>
      <td>depth_first</td>
    </tr>
    <tr>
      <th>47</th>
      <td>0.071053</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>48</th>
      <td>0.010752</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>breadth_first</td>
    </tr>
    <tr>
      <th>49</th>
      <td>2.270887</td>
      <td>0.008771</td>
      <td>0.001053</td>
      <td>depth_first</td>
    </tr>
  </tbody>
</table>
</div>

