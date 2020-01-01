import random

import ds_choices as ds
import phrases

# List of structures to be used as formatting.
structures = ['{word} ahead', 'be wary of {word}', 'try {word}', 'need {word}', 'imminent {word}...', 'weakness: {word}', '{word}', '{word}?', 
              'no {word} ahead', '{word} required ahead', 'could this be a {word}?', 'if only I had a {word}...', 'visions of {word}...',
              'time for {word}', '{word}!', '{word}...', 'huh. It\'s a {word}...', 'praise the {word}!', 'let there be {word}', 'ahh, {word}...'] 

# List of conjunctions to join two structures.
conjunctions = ['\nand then ', '\ntherefore ', '\nin short ', '\nor ', '\nonly ', '\nby the way ', '\nso to speak ', '\nall the more ', ',\n']

def makeSegment():
    # Return a random phrase group.
    return random.choice(structures).format(word=phrases.createPhraseGroup())  

def makeStructure():    
    # Use a conjunction one 1/3 of the time.
    roll = random.randint(1,3)

    # Use an in-game possible message 1/20 of the time.
    # Since the script will run on average 3 times a day, this should produce a message like this a little less than once a week.
    if random.randint(1,50) == 1:
        if roll == 1:
            return ds.getRandomPhrase() + random.choice(conjunctions) + ds.getRandomPhrase()
        else:
            return ds.getRandomPhrase()
    # Otherwise, create our own message.            
    else:        
        if roll == 1:
            return makeSegment() + random.choice(conjunctions) + makeSegment()
        else:
            return makeSegment()

def makeCapitalizedMessage():
    # Create message without capitalization.
    message = makeStructure()

    # Capitalize the first letter of the message.
    message = message[0].upper() + message[1:]

    # If the message has any line breaks, find where the new line is started and capitalize the first letter of the new line.
    if '\n' in message:
        charIndex = message.index('\n')
        message = message[0:charIndex + 1] + message[charIndex + 1].upper() + message[charIndex + 2:]
    
    print(message)
    return message   
