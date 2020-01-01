import random
import random_word_by_pos as randPOS

def createNounGroup():
	# Random number to decide group structure.
	roll = random.randint(1,10)

	# Return noun 80% of the time.	
	if roll <= 8:
		return randPOS.getRandomWordByPos(partOfSpeech='noun')
	# Return adj noun 10% of the time.
	elif 8 < roll <= 9:
		return randPOS.getRandomWordByPos(partOfSpeech='adj') + ' ' + randPOS.getRandomWordByPos(partOfSpeech='noun')
	# Return noun noun 10% of the time.
	else:
		return randPOS.getRandomWordByPos(partOfSpeech='noun') + ' ' + randPOS.getRandomWordByPos(partOfSpeech='noun')

def createVerbGroup():
	# Random number to decide group structure.
	roll = random.randint(1,10)

	# Return verb 80% of the time.
	if roll <= 8:
		return randPOS.getRandomWordByPos(partOfSpeech='verb')
	# Return adv verb 10% of the time.
	elif 8 < roll <= 9:
		return randPOS.getRandomWordByPos(partOfSpeech='adv') + ' ' + randPOS.getRandomWordByPos(partOfSpeech='verb')
	# Return adj verb 10% of the time.
	else:
		return randPOS.getRandomWordByPos(partOfSpeech='adj') + ' ' + randPOS.getRandomWordByPos(partOfSpeech='verb')	  	

def createPrepGroup():
	# Random number to decide group structure.
	roll = random.randint(1,10)

	# Return verbGroup prep nounGroup 80% of the time.
	if roll <= 8:
		return createVerbGroup() + ' ' + randPOS.getRandomWordByPos(partOfSpeech='prep') + ' ' + createNounGroup()
	# Return verbGroup prep 10% of the time.
	elif 8 < roll <= 9:
		return createVerbGroup() + ' ' + randPOS.getRandomWordByPos(partOfSpeech='prep')
	# Return verbGroup prep verbGroup 10% of the time.
	else:
		return createVerbGroup() + ' ' + randPOS.getRandomWordByPos(partOfSpeech='prep') + ' ' + createVerbGroup()		

def createPhraseGroup():
	# Random number to decide group structure.
	roll = random.randint(1,10)

	# Return nounGroup 40% of the time.
	if roll <= 4:
		return createNounGroup()
	# Return verbGroup 40% of the time.	
	elif 4 < roll <= 8:
		return createVerbGroup()
	# Return prepGroup 20% of the time.	
	else:
		return createPrepGroup()		  	