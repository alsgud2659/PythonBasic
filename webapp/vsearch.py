def search4vowels(phrase:str) -> str:
    '''Return any vowels found in a supplied phrase.'''
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str,letters:str) -> set:
    return set(letters).intersection(set(phrase))