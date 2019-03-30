# Skcript-PS

### Problem Statement:

https://www.reddit.com/r/dailyprogrammer/comments/aq6gfy/20190213_challenge_375_intermediate_a_card/

### Algorithm to Solve:

This problem can b divided into two types based on the number of 1s in the string. If there are even number of 1s, then there exists no solution and if there are odd number of 1s, then there exists a solution to which I will be proposing an algorithm.

#### Proof for the case of even 1s:

This can be done using induction on the length of the string.

**Base Case:** Length of string is 1. For a string length of 1, 0 is the only string with even number of 1s. Clearly it has no solution. Hence base case is true.

**Induction Hypothesis:** Let all strings upto length n with even number of 1s have no solution. Take a string with length n+1 and even number of 1s. If there are no 1s in the string it clearly has no solution. So let it have atleast one 1. Take any 1 in the string and remove it. This creates 2 subproblems, to the left and right, each of length  strictly less than n+1. Now let x be the number of 1s to the left in the original string and y be the number of 1s to the right in the original string. Now if the element to the left of the 1 we removed be a zero, then the number of 1s in the left subproblem is x+1. If the element to the left is 1, then the number of 1s in the left subproblem is x-1. Similarly the number of 1s in the right subproblem is y+1 or y-1. Now in the original string x+y+1 is even, hence x+y is odd. This implies either x or y have to be odd, since the parity of x+1, x-1, y+1 or y-1 is opposite to that of x or y, there is atleast one subproblem which has even number of 1s. Hence atleast one subproblem will not have a solution. So the string itself will not have a solution. If the 1 we remove be a corner point, then there exists only one subproblem. Let the number of 1s in the original string excluding the 1 we remove be x. So, x+1 is even, this implies x is odd.
So the number of 1s in the subproblem is either x+1 or x-1, both of which is even. So again the subproblem has no solution. Hence the Induction Hypothesis is Proved.

#### Algorithm for strings with odd number of 1s:

The algorithm I propose is as follows: Pick the first 1 from the left in the string and remove it. So this creates two subproblems. The element to the left of 1, is a 0 due to our choice. So now it becomes a 1 and our left subproblem is a sequence of 0s followed by a 1. This is solved by removing the 1 recursively as every time you remove the 1, it creates one more before it. Now continue this algorithm for the right subproblem.

#### Proof for the above algorithm:

We shall prove this as well by induction on the length of the string. 

**Base Case:** Length of string is 1. For a string length of 1, 1 is the only string with odd number of 1s. Clearly the algorithm solves it.

**Induction Hypothesis:** Let all strings of length upto n be solvable using this algorithm. Take a string of length n+1 with odd number of 1s. Pick the first 1 according to the algorithm and remove it. Now the left portion is solvable as I have explained above. Let x be the number of 1s in the right portion originally. After removing the 1, it either becones x+1 or x-1. We know the number of 1s in the string originally was x+1 which is odd. Hence the number of 1s in the right subproblem is also odd, whose solution exists as it is a string of smaller length and has odd number of 1s. Thus the Induction Hypothesis is proved.

#### Time Complexity

The running time for this algorithm is O(n). It takes O(n) to check the parity of number of 1s in the string. The algorithm part also runs in O(n) time. This is because every I start a subproblem, reach the first 1 and come back to the start of problem. Hence each character is visited twice.
