# Getting started

make

make run  or ./main "input file"

# The implementation

For hashing functionality I used unordered_map in c++
And the key of this unordered_map would be String type "ValueNum OP ValueNum"

For example, let assume that there are two expressions:
a = x + y;
b = x + y;

whenever, we encounter the new variable, I assigned the value number
So, 1 is assigned to x and 2 y is assigned to y.
And then, 3 is assigned to a.
In addition, as subexpression of a is in the basic block,
We need to map the same Value Number (3) to the subexpression (x + y)

1. Before doing this, we need to care this thing: 
if there is a condition (x = l, z = l), then x + y and z + y has to be understood 
as same subexpression.
To solve this problem, I always change the subexpression like this.
if x is mapped to Value Number (1) and y is mapped to Value Number (2), then
subexpression is changed to '1+2'
and in the example case (x = 1, z = 1), x and z would have the same Value Number,
x + y and z + y would change into same subexpression (1+2).
And, by using this subexpression (1+2), I use hashing and check whether there is
a common subexpression or not.
Therefore, we can solve this problem.

***
so, the example (input: test/test1.txt, output: test/out1.txt)
```
a = x + y;
b = x + y;
```
is changed to
3 = 1 + 2;
4 = 1 + 2;

as there is a common subexpression "1 + 2"
the output would be
```
a = x + y;
b = a;
```
***

***
An example (input: test/test2.txt, output: test/out2.txt)
```
a = x + y;
b = x + y;
a = 5;
c = x + y;
```

is changed to
3 = 1 + 2
4 = 1 + 2;
5 = I5
6 = 1 + 2

For this problem, 
Value Number 3 is no longer used, all information relate to Value Number 3 is removed.
Therefore, the output would be
```
a = x + y;
b = a;
a = 5;
c = b;
```
***

***
The final example (input: test/test3.txt, output: test/out3.txt)
```
a = x + y;
b = x + y;
a = 5;
b = 5;
c = x + y;
```

```
is changed to
a = x + y;
b = a;
a = 5;
b = 5;
c = x + y;
```
***
