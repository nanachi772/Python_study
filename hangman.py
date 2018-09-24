# This game is hangman
import random

def hangman():
	questions = ['cat', 'gollira', 'dog', 'bird', 'rabbit']
	i = random.randint(0, 4)
	wrong = 0
	stages = ['',
	'__________	 ',
	'|	|			',
	'|	|			',
	'|	0			',
	'|      /|\	',
	'|      / \	',
	'|				',
	]
	
	rletters = list(questions[i])
	board = ['_'] * len(questions[i])
	win = False
	print ('welcome to hangman!')
	
	while wrong < len(stages) - 1:
		print ('\n')
		msg = 'guess any single character in word '
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong += 1
		print (' ' .join(board))
		e = wrong + 1
		print ('\n' .join(stages[0:e]))
		if '_' not in board:
			print ('you are win!')
			print (' ' .join(board))
			win = True
			break
		
	if not win:
		print ('\n' .join(stages[0:wrong + 1]))
		print ('you are lose, answer is {}.' .format(questions[i]))

hangman()