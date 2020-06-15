implement_list = ['List', 'Tuple', 'Dictionary']
method_list = ['Encrypt', 'Decrypt']
word = input('Enter a text: ')
key = input('Enter a key: ')

print('Select method: \n 1) Encrypt \n 2) Decrypt ')

step = True
method = ''
while method.capitalize() not in method_list:
    if step:
        method = input('Enter method:')
        step = False
    else:
        method = input('Enter a correct method: ')

print('Select implementation method: \n 1) List \n 2) Tuple \n 3) Dictionary')

implement = ''
step = True
while implement.capitalize() not in implement_list:
    if step:
        implement = input('Enter a implementation method: ')
        step = False
    else:
        implement = input('Enter a correct implementation method: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def EncOrDec(letter, step, method, alphabetList, letterIndex):
    if method.capitalize() == 'Encrypt':
        pos = alphabetList.index(letter.lower()) + letterIndex[step]
        if pos > 25:
            pos %= 26
        return pos
    else:
        pos = alphabetList.index(letter.lower()) - letterIndex[step]
        if pos < 0:
            pos += 26
        return pos


def EncOrDecForDic(letter, step, method, alphabetDictionary, letterIndex):
    indexAndCase = []
    if method.capitalize() == 'Encrypt':
        index = alphabetDictionary[letter.lower()] + letterIndex[step]
        if index > 25:
            index %= 26
        indexAndCase.append(index)
        if letter.isupper():
            indexAndCase.append(1)
        else:
            indexAndCase.append(0)
        return indexAndCase
    else:
        index = alphabetDictionary[letter.lower()] - letterIndex[step]
        if index < 0:
            index += 26
        indexAndCase.append(index)
        if letter.isupper():
            indexAndCase.append(1)
        else:
            indexAndCase.append(0)
        return indexAndCase


def EncryptOrDecrypt(word, key, implement, method):
    global alphabet
    # I use only list
    if implement.capitalize() == 'List':
        answerList = []
        alphabetList = list(alphabet)
        letterIndex = []
        for letter in key:
            letterIndex.append(alphabetList.index(letter.lower()))
        step = 0
        for letter in word:
            if step == len(letterIndex):
                step = 0
            pos = EncOrDec(letter, step, method, alphabetList, letterIndex)
            if letter.isupper():
                answerList.append(alphabetList[pos].upper())
            else:
                answerList.append(alphabetList[pos])
            step += 1
        return answerList

    # I use only tuple
    if implement.capitalize() == 'Tuple':
        answerTuple = ()
        alphabetTuple = tuple(alphabet)
        letterTuple = ()
        for letter in key:
            letterTuple += (alphabetTuple.index(letter.lower()),)
        step = 0
        for letter in word:
            if step == len(letterTuple):
                step = 0
            pos = EncOrDec(letter, step, method, alphabetTuple, letterTuple)
            if letter.isupper():
                al = alphabetTuple[pos].upper()
                answerTuple += (al,)
            else:
                answerTuple += (alphabetTuple[pos],)
            step += 1
        return answerTuple

    # I use only dictionary
    if implement.capitalize() == 'Dictionary':
        alphabetDictionary = {}
        alphabetDictionaryHelper = {}
        answerDictionary = {}
        letterIndex = {}
        for i in range(len(alphabet)):
            alphabetDictionary[alphabet[i]] = i
            alphabetDictionaryHelper[i] = alphabet[i]
        step = 0
        for letter in key:
            letterIndex[step] = alphabetDictionary[letter.lower()]
            step += 1
        step = 0
        index = 0
        for letter in word:
            if step == len(letterIndex):
                step = 0
            answerDictionary[index] = EncOrDecForDic(letter, step, method, alphabetDictionary, letterIndex)
            step += 1
            index += 1
        answerString = ''
        # It will be more beautiful if the answer is a string
        for x, y in answerDictionary.items():
            if y[1] == 1:
                answerString += alphabetDictionaryHelper[y[0]].upper()
            else:
                answerString += alphabetDictionaryHelper[y[0]]
        return answerString


print('\n' + method.capitalize() + 'ed text is:', EncryptOrDecrypt(word, key, implement, method))
print('Implementation method was ' + implement)
