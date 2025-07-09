Tutorial for BIF-retreat 2025

Welcome to the brief tutorial on test-driven development (TDD)!

TDD has become the de facto standard for writing clean code. It combines several proven software-development practices in one set of actionable steps. 
In this tutorial, you will implement a set of string-matching algorithms, starting from simple to complex ones.
Start of with brute-force exact matching, as described in the _test.py file. You can start with the classes defined in matcher.py

You will finish by implementing  the pigeonhole principle, a pattern matching approach combining exact with approximate matching approaches.

In approximate string matching (e.g., allowing up to k mismatches), the pigeonhole principle offers a simple but powerful insight:

If a pattern is divided into k + 1 parts, and the text contains the pattern with at most k errors, then at least one part must match exactly.

This idea helps reduce the search space: we can first look for exact matches of the parts (which is faster), and only then verify the surrounding regions for possible approximate matches.

For more information on the pigeonhole principle, please see this lecture by Ben Langmead, from John Hopkins University:
https://www.youtube.com/watch?v=duatMINEGgE

Here for an implementation in code by the same author: 
https://www.youtube.com/watch?v=9M8aNFgwNG0&t=13s

Please finish the pigeonhole principle for 1 mismatch, and try to implement it, with TDD, for 2 mismatches!

This tutorial will use pytest, a simple but powerful testing framework based on the traditional unittest library, now shipped automatically with python:

https://docs.pytest.org/en/stable/index.html

To start, simply install pytest via 

>> pip3 install pytest

to run the tests, go to the directory containing them, and run:

>> pytest (optional: filename)

This will check all the files ending with _test.py, and look for methods starting or ending as well with "test_","_test",

You can also expand on the classes used in unittest. See the attaced code as an example
