## Python Solutions to Cracking the Coding Interview 6th Edition

To run the programs, just use the `python filename.py` command.

The test cases are included in the solution files.

Alternatively to verify solutions using custom input/output, you can use the tester module provided.

### Tester

#### Usage

```bash
$ python tester Chapter8/4_PowerSet/recursive.py

Correct answer!

Input:
[1, 2, 3]

Your output:
[(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]
```



In the example above, the tester will scan the module directory for files `input` and `output`. 
These can also be supplied from the command-line:

```bash
python tester Chapter8/4_PowerSet/iterative.py \
> -i Chapter8/4_PowerSet/input \
> -o Chapter8/4_PowerSet/output
```

#### Input/Output syntax

It supports almost any built-in python data structure expression such as numbers, tuples, lists, dicts:

* 1
* [2, 3]
* (4, 5)
* 6.7

If your function accepts multiple parameters:

```python
def my_algorithm(array, start, end):
```

The input file supports adding them to separate lines:

```
[1, 2, 3, 4, 5, 6, 7, 8]
0
7
```
