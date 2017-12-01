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
	trapped = False;
	snake_size =- 1;
	if (snake[snake_size] == '0 0'):
		if ('0 1' in snake and '1 1' in snake and '1 0' in snake):
			trapped = True;
	elif (snake[snake_size] == '0 '+str(snake_size)):
		if ('0 '+str(snake_size-1) in snake and '1 '+str(snake_size-1) in snake and '1 '+str(snake_size) in snake):
			trapped = True;
	elif (snake[snake_size] == str(snake_size)+' 0'):
		if (str(snake_size-1)+' 0'in snake and str(snake_size-1)+' 1' in snake and str(snake_size)+' 1' in snake):
			trapped = True;
	elif (snake[snake_size] == str(snake_size)+' '+str(snake_size)):
		if (str(snake_size-1)+' '+str(snake_size-1) in snake and str(snake_size-1)+' '+str(snake_size) in snake and str(snake_size)+' '+str(snake_size-1) in snake):
			trapped = True;
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

snake_len = 7;
fname = "dataTest/10x10.csv";
population_size = 5;
population = [[0 for x in range(2)] for y in range(population_size)];

gridSize = file_len(fname);
gridSize -= 1;
grid = readGrid(fname);
for i in range (0, 500):
	snake, value = createSnake(grid, gridSize, snake_len);
	print(snake);
	print(value);



