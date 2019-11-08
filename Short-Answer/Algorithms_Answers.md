#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because there's one loop being execute n times and it scales linearly.

b) O(n^2) because there's a nested loop and each time the algorithm runs, which means the steps performed is n*n.

c) O(n) because the function is being called recursively until it hits it's base case and it looks like it scales linearly.

## Exercise II

First, we notice that the floors are in order from lowest to highest. Knowing the data is already sorted we can do a search, and in this case binary search makes the most sense.

So we'd start off by splitting the number of floors and finding the middle floor in the building. If an egg breaks from there, all the floors above it are eliminated and a new floor is selected from the middle of the floors below you.

This process keeps going until you find a floor that doesn't break the egg. If on a specific floor the egg doesn't break, then you selected a new floor from the middle of the floors above you and continue to check.

Once there are only two floors left, the floor that does break the egg is what we're looking for. The floor under it should not be breaking the egg. Because this is a binary search, it has time complexity of O(log n).