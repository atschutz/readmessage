import enchant
import random

from nltk.corpus import wordnet as wn
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!! Remember to call nltk.download() and install WordNet package !!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# List of prepositions to be randomly selected. 
prepositions = ['aboard', 'about', 'above', 'absent', 'across', 'cross', 'after', 'against', 'along','alongside', 'amid', 'among', 'around', 'as', 'astride',
                'at', 'atop', 'ontop', 'bar', 'before', 'behind', 'below', 'beneath', 'beside', 'besides', 'between', 'beyond', 'but', 'by', 'circa', 'come',
                'despite', 'down', 'during', 'except', 'for', 'from', 'in', 'inside', 'into', 'less', 'like', 'minus', 'near', 'notwithstanding', 'of', 'off',
                'on', 'onto', 'opposite', 'out', 'outside', 'over', 'past', 'per', 'plus', 'post', 'pre ', 'pro', 'sans', 'save', 'short', 'since', 'through',
                'throughout', 'to', 'toward', 'towards', 'under', 'underneath', 'unlike', 'until', 'up', 'upon', 'upside', 'versus', 'via', 'with', 'within',
                'without', 'worth']

def getRandomWordByPos(partOfSpeech):
    # If we're not returning a preposition....
    if not partOfSpeech == 'prep':
        # Use partOfSpeech parameter to decide which part of speech our random word will be
        if partOfSpeech == 'noun':
            word = random.choice(list(wn.all_synsets(wn.NOUN)))
        elif partOfSpeech == 'verb':
            word = random.choice(list(wn.all_synsets(wn.VERB)))
        elif partOfSpeech == 'adj':
            word = random.choice(list(wn.all_synsets(wn.ADJ)))
        elif partOfSpeech == 'adv':
            word = random.choice(list(wn.all_synsets(wn.ADV)))       
        else:    

            print('Invalid part of speech.')
            return None    

        # Split actual word from synset.
        splitWord = word.name()
        finalWord = splitWord.partition('.')[0]

        # If WordNet returns a "word" with a space in it for some reason (noted with an underscore), 
        # run the function again until we get a "word" without an underscore.
        if '_' in finalWord:
            return getRandomWordByPos(partOfSpeech)
        else:
            # Otherwise, if we have a verb, convert it to a present participle.
            if partOfSpeech == 'verb':
                finalWord = addPresentParticipleSuffixToVerb(verb=finalWord)
                
                # If the present participle function returns None, it means we hit a non-convertable word
                # and neet to run it again. this is explained more within the function. 
                if finalWord == None:
                    return getRandomWordByPos(partOfSpeech='verb')

            return finalWord
    # If we are returning a preposition, return a random one from our prepositions list. 
    else:
        return random.choice(prepositions)        

def addPresentParticipleSuffixToVerb(verb):
    # Append an "ing" ending to a verb. Uses some basic rules of english to decide how this is done. 
    # Appending routine taken from https://gist.github.com/arjun921/5f38259ea056fdc35617cb7449fb234e
    li = []

    for x in verb:
        li.append(x)

    if li[len(li)-1] == 'e' and li[len(li)-2] != 'i':
        del li[len(li)-1]
        li.append("ing")
    elif li[len(li)-1] == 'e' and li[len(li)-2] == 'i':
        del li[len(li)-1]
        del li[len(li)-1]
        li.append("ying")
        """To Check"""
    elif li[len(li)-2] in 'aeiou' and li[len(li)-1] not in 'aeiou':
        temp = li[len(li)-1]
        del li[len(li)-1]
        li.append(temp)
        li.append(temp)
        li.append("ing")
    elif li[len(li)-1] in 'aeiouy':
        li.append("ing")
    else:
        li.append("ing")
    
    ppVerb = "".join(li)

    # In some cases, the verb returned isn't a proper english word. This is usually because of an irregular case
    # where there is a double consonant before the "ing" when there shouldn't be. Here, we check to see if the 
    # word is within the english dictionary, and if not, we remove the extra consonant. If the new verb is still
    # not in the english dictionary, we return None. Better to leave out a few irregular verbs than return a 
    # misspelled word!
    d = enchant.Dict("en_US")

    if d.check(ppVerb):
        return ppVerb
    else:
        ppVerb = removeAt(len(ppVerb)-4, ppVerb)
        
        if d.check(ppVerb):
            return ppVerb
        else:
            return None   

def removeAt(index, string):
    # Return a given string with the letter at given index removed.
    return string[:index] + string[index+1:] 
