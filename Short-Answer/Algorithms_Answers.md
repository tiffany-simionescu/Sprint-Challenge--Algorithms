#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) - Even though there are some constants (O(1)), this algorithm runs linear as n will increase gradually over time due to the while loop.


b) O(n log n) - The outer loop runs linear (O(n)), because it increases n times, while the inner loop runs logarithmically (O(log n)), because you are doubling the value of j during each iteration. This combination will give you a Linearithmic (O(n log n)) runtime. 


c) O(n) - Even though there's recursion, it's a singular recursion that will only increase n (bunnies) times (linear).

## Exercise II

eggs won't break < floor_of_breakage => eggs will break

A binary search will help determine the breaking height / floor for the eggs.

By dividing the search in half, we can minimize breakage. If the egg breaks at mid point, we know that the breaking point is either the mid point or lower and can eliminate higher possibilities. If the egg doesn't break at midpoint, we know that the breaking point is higher than midpoint and can element the lesser half.

Because we're eliminating the possibilies by half each time, this would be a logarithmic runtime (O(log n))
