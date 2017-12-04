def readGrid(fname):
	file  = open(fname, "r");
	lines = file.readlines();
	fileLen = file_len(fname);
	grid = [];
	for i in range (0, fileLen):
		grid.append(lines[i].replace('\n', '').split(';'));
	return grid

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def generateRandomIndex(gridSize):
	from random import randint
	x, y = randint(0, gridSize), randint(0, gridSize);
	index = str(x)+' '+str(y);
	return index;

def nextPosition(x, y, gridSize):
	from random import randint
	x1, y1 = randint(-1, 1), randint(-1, 1);
	newX = x1 + x;
	if (newX < 0):
		newX = 0;
	elif (newX > gridSize):
		newX = gridSize; 
	newY = y1 + y;
	if (newY < 0):
		newY = 0;
	elif (newY > gridSize):
		newY = gridSize; 
	pos = str(newX)+' '+str(newY);
	return pos

def isNextStepViable(gridSize, snake, nextStep):
	isViable = True;
	x, y = nextStep.split(' ');
	x = int(x);
	y = int(y);
	if (x < 0 or x > gridSize or y < 0 or y > gridSize or nextStep in snake):
		isViable = False;
	return isViable

def isTrapped(gridSize, snake, snake_size):
	snake_size -= 1;
	trapped = True;
	x, y = snake[snake_size].split(' ');
	x = int(x);
	y = int(y);
	for i in range(-1, 1):
		for j in range(-1, 1):
			x1 = x + i if (x + i <= gridSize and x + i >= 0) else x;
			y1 = y + j if (y + j <= gridSize and y + j >= 0) else y;
			trapped = trapped and (str(x1)+' '+str(y1) in snake);
	return trapped;

def createSnake(grid, gridSize, snake_len):
	#getting the first position of the snake
	x, y = generateRandomIndex(gridSize).split(' ');
	snake = [];
	snake.append(x+' '+y); # first position of the snake
	x = int(x);
	y = int(y);
	value = int(grid[x][y]);
	snake_size = 1;
	while (snake_size < snake_len): #getting all other positions
		nextStep = nextPosition(x, y, gridSize);
		if (isNextStepViable(gridSize, snake, nextStep)):
			snake.append(nextStep);
			x, y = nextStep.split(' ');
			x = int(x);
			y = int(y);
			value += int(grid[x][y]);
			snake_size += 1;
		elif (isTrapped(gridSize, snake, snake_size)):
			return [0], 0;
	return snake, value

def isSnakeDifferent(snake1, snake2, snake_len):
	different = True;
	for j in range(0, snake_len-1):
		if (snake1[j] in snake2):
			different = False;
	return different

def solutionFounded(population, population_size, snake_len):
	valueList = list(map(lambda l: l[0], population));
	for y in range(0, population_size-1):
		solutionList = [i for i, j in enumerate(valueList) if j == population[y][0]];
		if (len(solutionList) > 1): # verify if have 2 or more snakes in population that have same value
			for j in range(0, len(solutionList)-1):
				if (isSnakeDifferent(population[solutionList[j]][1], population[solutionList[j+1]][1], snake_len)): #compare snake to see if they are not in same place
					return True, [solutionList[j], solutionList[j+1]]
	return False, [];

def findBiggerAndSmaller(valueList):
	bigger = smaller = valueList[0]; # save the value to search
	biggerI = smallerI = 0; #save the index
	for j in range(0, len(valueList)):
		if (bigger < valueList[j]):
			bigger = valueList[j];
			biggerI = j;
		if (smaller > valueList[j]):
			smaller = valueList[j];
			smallerI = j;
	return biggerI, smallerI;

def killPop(population, sizeOfKilling):
	while (sizeOfKilling > 0):
		valueList = list(map(lambda l: l[0], population));
		bigger, smaller = findBiggerAndSmaller(valueList);
		if (bigger > smaller and sizeOfKilling > 1):
			population.pop(bigger);
			population.pop(smaller);
			sizeOfKilling -= 2;
		elif(smaller > bigger and sizeOfKilling > 1):
			population.pop(smaller);
			population.pop(bigger);
			sizeOfKilling -= 2;
		else:
			population.pop(bigger);
			sizeOfKilling -= 1;
	return population


snake_len = 7;
fname = "dataTest/10x10.csv";
population_size = 10;
percentOfKilling = 20;
popToKill = int(population_size * (percentOfKilling/100));


gridSize = file_len(fname);
gridSize -= 1;
grid = readGrid(fname);
solutionList =[];
solutionFound = False;
population = [];
i = 0;
iteration = 0;

while (solutionFound == False):
	if (i > 0):
		population = killPop(population, popToKill);
		i -= popToKill;
	while (i < population_size):  #creating a population
		snake, value = createSnake(grid, gridSize, snake_len);
		if (value == 0):
			i -= 1;
		else:
			population.append([value, snake]);
		i += 1;
	solutionFound, solutionList = solutionFounded(population, population_size, snake_len); #verify if the solution was founded
	iteration += 1;

print(population[solutionList[0]][0]); #print value of the solution
for i in range(0, len(solutionList)): #print snake of the solution
	print(population[solutionList[i]][1]);
print ('problem solved in ' + str(iteration) + ' iteration(s)');
