def minion_game(s):
    vowel_chr='IOEAU'
    vowel=0
    consonants=0
    for i,_chr in enumerate(s,0):
        if _chr in vowel_chr:
            vowel+=len(s)-i
        else:
            consonants+=len(s)-i
    if vowel>consonants:
        print('Kevin '+str(vowel))
    elif vowel<consonants:
        print('Stuart '+str(consonants))
    else:
        print('Draw')

