def is_vowel(vowelstring):
    '''
    This function takes in a string and lowercases it
    Return true if input is a vowel
    And return False if input is consonant
    '''
    #lowercase the input string
    vowelstring = vowelstring.lower()
    
    #if the input is a vowel
    if vowelstring == ('a' or 'e' or 'i' or 'o' or 'u'):
        return True
    else:
        return False