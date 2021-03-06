# vanhackathon-7snake-game
Vanhackaton 27/11/2017, delivery at 28/11/2017
This problem is a typical search problem much like tic-tac-toe or chess. You must search through a (large) space for possible solutions

Ascent Software Challenge
http://www.ascentsoftware.eu/
Playing with 7-Snakes

This problem is a typical search problem much like tic-tac-toe or chess. You must search through a (large) space for possible solutions. The cleverness (in our view) is in the way you enumerate the search space.
Let’s start with some definitions:
Consider the Grid A below. A 7-Snake is a sequence of cells c1, c2, …,c7 in a grid such that each cell is adjacent to the one before it. 
More formally, for 1 ≤ i < 7, ci+1 is adjacent to ci. 
Two cells a and b are adjacent if b is to the top, bottom, left, or right of a. 
Given an arbitrary ordering of the cells in a 7-Snake, each cell ci, can only be adjacent to ci-1 or ci+1.  Note that this exclude cycles.
In Grid A below, the yellow and blue 7-Snakes are valid but the green one is not. This is because cell 7 is not to the top, bottom, left, or right of cell 6. ‘Diagonal’ adjacency is not allowed.

![GridA][grid_a]

# Problem Definition:
The problem is very simple to describe. Given a grid of integers such as Grid B below, find a pair (two) of 7-Snakes A and B that has the property that the sum of the integers in 7-Snake A is exactly the same as the sum of integers in 7-Snake B

![GridB][grid_b]

# Notes:
The two 7-Snakes must be distinct. They cannot share cells.
In general there may be more than one pair of 7-Snakes with the required property. Your program need only find one pair.
If no such pair exists the program should output ‘FAIL’. Otherwise it should output the first pair it finds that has the above property.
The solution depends on your ability to enumerate the set of all pairs of distinct 7-Snakes in the given grid.
In general, the input grid can be any (square) size. Grid B above is just an example of a 10 X 10 grid. The grid should be stored in CSV format on disk and loaded by your solution. This will allow us to test your solution on various test examples. The integers in each cell must range from 1 to 256. 

Solution:
![Solution][solution]

[solution]: /solution.png "Solucao"
[grid_a]: /grida.png "Solucao"
[grid_b]: /gridb.png "Solucao"

# My solution:
This problem was solved using the concept of population of the genetic algorithm.

This program works using the following steps:

	1. Fill the population with random snakes to the max allowed population size.
	2. Verify if in this population have 2 snakes that have same value and not share the same space.
		- In positive case go to step 4.
		- In negative case go to step 3.
	3. Kill a given amount of the population and go to step 1.
	4. finish the program and show the 2 snakes

This logic need an enhancement to be a real AG.

The final logic has to be something like:

	1. Fill the population with random snakes to the max allowed population size.
	2. Verify if in this population have 2 snakes that have same value and not share the same space.
		- In positive case go to step 5.
		- In negative case go to step 3.
	3. Kill a given amount of the population.
	4. Merge and/or mutate the rest of snakes to create new snakes to fill the spaces and go to step 2.
	5. finish the program and show the 2 snakes

And also will need tests to find the best population size and best percent of population killing.
