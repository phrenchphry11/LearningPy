# Creat a hangman game for dictionary.com's word of the day

import requests
var = requests.get('http://dictionary.reference.com/wordoftheday/archive/2014/06/20.html')
html = var.text.encode('utf-8')
from bs4 import BeautifulSoup
soup = BeautifulSoup(html)

word = soup.h2.string
definition = soup.select(".defn")

length = len(word)
print '_ ' * length

known = {}
letNum = 0
while letNum < length:
    known[letNum] = word[letNum]
    letNum += 1 

unknown = {}
unNum = 0
while unNum < length:
    unknown[unNum] = '_'
    unNum += 1  


def letterFind(fullWord,let,forward):
    if fullWord.count(let) > 0:
        position = fullWord.find(let)
        unknown[position + forward] = known[position + forward]
        forward += (position + 1)
        letterFind(fullWord[position+1:],let,forward)

def writer():
    wordLength = 0
    allLetters = ''
    while wordLength < length:
        allLetters += unknown[wordLength]
        wordLength +=1  
    return allLetters

def defPrinter():
    for div in definition:
        cut = str(div).find('</')
        cut2 = str(div).find('<em>')
        if (div).find('em') >= 0:
            return str(div)[18:cut2]
        else:   
            return str(div)[18:cut] 


wrongLetters = ''
wrong = 0
while '_' in unknown.values():
    guess = raw_input('Guess a letter:')
    position = word.find(guess)
    if guess == '':
        print "You didn't guess"
    elif len(guess) > 1:
        print "Only one letter ya jerk!"
    elif writer().count(guess) >=1:
            print "You already guessed " + guess        
    elif position >=0:
        letterFind(word,guess,0)
        print writer()
    else:
        if wrong >= 5:
            print 'Sorry the word was: ' + word
            print 'It means:'
            print defPrinter()
            break
        elif wrongLetters.count(guess) >=1:
            print "You already guessed " + guess 
            print "Your wrong letters are:" + wrongLetters
        else:   
            wrong += 1
            wrongLetters += (guess + " ") 
            print "Sorry " + guess + " isn't in the word"
            print "You have guessed " + str(wrong) + " letters wrong out of 6 allowed"
            print "Your wrong letters are:" + wrongLetters

#only show if won
if writer().count('_') == 0:
    if len(defPrinter()) > 0:
        print "You win, it means:"
        print defPrinter()
    else:
        print "You Win!"    