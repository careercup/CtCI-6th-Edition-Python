# Python Solutions to *Cracking the Coding Interview, 6th Edition*

These are **Python** solutions for the book [Cracking the Coding Interview, 6th Edition](https://www.careercup.com/book) by *Gayle Laakmann McDowell*.

## How to use?

To run the programs, just use the `python chapter_X/filename.py` command.

To run the tests: `pip install pytest` and `pytest`

## Contributions

Contributions welcome! Please submit separate pull requests for each solution you work on.

In general solutions should fall into one of the following three categories:
 - *algorithm demonstration*.  This is the primary type of problem and solution that the text is concerned with. As
 such, solutions should not use standard library functions in cases that would make it unnecessary to implement the
 algorithm.  The goal of these solutions should be to have an easy to understand solution that demonstrates
 understanding of the algorithm.
 - *python demonstration*.  We also accept solutions that solve the problem in a more practical way, using whatever
 standard library functions are available.  Please do not use any third party dependencies.  These solutions should
 also be easy to understand and good examples of pythonic ways of doing things.
 - *speed demonstration*.  These alternative solutions may be accepted if the fastest way to do something is not very
 readable or intuitive and thus it doesn't fit into the first two categories.

If you want to do everything really well, here are some guidelines. Solutions should:
 - work with Python 3.6 or greater
 - not depend on third-party libraries (like `numpy`)
 - follow [python style conventions](https://www.python.org/dev/peps/pep-0008/)
   - camel_case for everything except classes
   - descriptive, longer variable names
 - be formatted using the [`black`](https://black.readthedocs.io/en/stable/) code formatter
 - include tests to prove they work. [pytest](https://docs.pytest.org/en/stable/) is supported
 - have a clean commit history ideally following the
 [angular commit message convention](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#type)
 and including the problem being worked on in parenthesis. For example `feature(C01_P04): added solution`.  The C01_P04
 referring to Chapter 1, Problem 4.  Look at our [commit history](https://github.com/careercup/CtCI-6th-Edition-Python/commits/master) for more examples:

We'll still work with your contributions even if they don't follow these guidelines so don't let that stop you.