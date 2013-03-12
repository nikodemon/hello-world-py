#!/usr/bin/env python
#-*- coding: utf-8 -*-
import string


def isWordGuessed(secretWord, lettersGuessed):
    """docstring for isWordGuessed"""
    isLetterTrue = []
    for letter in range(len(secretWord)):
        isLetterTrue.append(False)
        for letterg in range(len(lettersGuessed)):
            if secretWord[letter] == lettersGuessed[letterg]:
                isLetterTrue[letter] = True
        if not(isLetterTrue[letter]):
            return False
            break
    if letter == len(secretWord) - 1 and isLetterTrue[letter]:
        return True


def getWordGuessed(secretWord, lettersGuessed):
    """docstring for getWordGuessed"""
    wordGuessed = []
    for letter in range(len(secretWord)):
        wordGuessed.append('_')
        for letterg in range(len(lettersGuessed)):
            if secretWord[letter] == lettersGuessed[letterg]:
                wordGuessed[letter] = secretWord[letter]
    if letter == len(secretWord) - 1 and wordGuessed[letter]:
        return ''.join(wordGuessed)


def getAvalibleLetters(lettersGuessed):
    """docstring for getAvalibleLetters"""
    avalibleLetters = string.ascii_lowercase
    letters = ''
    for letterToCheck in avalibleLetters:
        letters += letterToCheck
        for letter in lettersGuessed:
            if letter == letterToCheck:
                letters = letters[0:-1]
                break
    return letters


def hangman(secretWord):
    """docstring for hangman"""
    shots = 8
    checkLetter = True
    shotLetters = []
    checkWord = word = getWordGuessed(secretWord, shotLetters)
    while shots >= 1:
        print "you have %i shots left." % shots
        shots -= 1
        shotedLetter = ''
        print "avalible letters %s." % getAvalibleLetters(shotLetters)
        while True:
            shotedLetter = raw_input("Please shot a Letter: ")
            if len(shotedLetter) == 1:
                shotedLetter = shotedLetter.lower()
                for checkLetter in shotLetters:
                    if checkLetter == shotedLetter:
                        print "Ops! You`ve already shoted that letter! %s" % word
                        checkLetter = False
                        break
                if checkLetter:
                    break
            print "Please select next shot."
        shotLetters.append(shotedLetter)
        word = getWordGuessed(secretWord, shotLetters)
        if word == checkWord:
            print "Ops! That letter is not in my word! %s" % word
        else:
            print "Good shot! %s" % word
            checkWord = word
            shots += 1
            if isWordGuessed(secretWord, shotLetters):
                print "Congratulations, you won!"
                break
    if not(isWordGuessed(secretWord, shotLetters)):
        print "sorry, you out of shots. The word was else."

if __name__ == '__main__':
    print "Welcome in hangman!"
    hangman('psiadupa')

