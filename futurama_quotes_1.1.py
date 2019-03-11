#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:58:37 2019

@author: jhutt5383
"""

#Futurama quote game


#import random, high_score file and file with quotes and names
import random
from high_score import*
from quotes_and_names import*



def newQuoteIndex():
    """Output: generates new global variable quote index based on length of quotes_copy list"""
    
    global quote_index
    quote_index = random.randint(0, (len(quotes_copy)-1))

def printQuote(quote_index):
    """pass in index integer between 0 and len(quotes)
       return: None
       prints: quote"""
       
    print('')
    print("Which character said:")
    print('')
    print(quotes_copy[quote_index][0])
    
    
    
def returnNameChoiceList(quote_index):
    """input: quote_index - int marking index of chosen quote
       return: A list of name choices, with answer at index 0"""
    #list of name choices with correct answer added manually
    name_choices = [quotes_copy[quote_index][1]]
    #populate the rest of the list
    while len(name_choices) < 5:
        name_index = random.randint(0, (len(names)-1))
        new_name = names[name_index]
        if new_name not in name_choices:
            name_choices.append(new_name)
            
    return name_choices



def printMultChoiceReturnKey(quote_index, name_choices):
    """Input: int - quote_index, list - name_choices
    Returns: dictionary with key:value equals letter_answer : name_answer
    Prints: Name choices next to their letter choices
    """
    #multiple choice letters
    letters = ['A', 'B', 'C', 'D', 'E']
    #generates dictionary to link multiple choice letter with name answers
    answer_key = {}
    #make a copy of name_choices to delete names as they are randomly selected
    name_choices_copy = name_choices.copy()
    #loop through name_choices_copy - randomly select names and link them to multiple choice letter in the dictionary - delete letter and name from respective lists
    while name_choices_copy != []:
        
        #select random index and it's corresponding name
        
        rand_index = random.randint(0, (len(name_choices_copy)-1))
        name = name_choices_copy[rand_index]
        
        #add + link name if it is not already in the answer_key dictionary
        
        if name not in answer_key.values():
            answer_key[letters[0]] = name
            del(letters[0])
            del(name_choices_copy[rand_index])
            
    #print out graphical display for user
    
    print('')
    print("A) " + answer_key["A"])
    print('')
    print("B) " + answer_key["B"])
    print('')
    print("C) " + answer_key["C"])
    print('')
    print("D) " + answer_key["D"])
    print('')
    print("E) " + answer_key["E"])
    print('')
    
    #returns the letter:name answer key dictionary
    return answer_key

    
    
def getUserAnswer(quote_index, answer_key, score_errors):
    """Input: quote_index - int >= 0; answer_key - dictionary
    OUtput: Other stuff"""
    answer_name = quotes_copy[quote_index][1]
    #Get user guess
    guess = input("Enter the letter of the correct answer: ")
    
    valid_answers = ['a', 'b', 'c', 'd', 'e', 'A', 'B', 'C', 'D', 'E']
    #check guess validitity
    while guess not in valid_answers:
        guess = input("Yeah, try again, preferably a letter this time: ")
    #add a try statement or something so there's not issues with KeyError
    #possibly split into two methods
    if answer_key[guess.upper()] == answer_name:
        #acknowledge win and update score
        print('')
        print('Hooray! You just earned ' + str(quotes_copy[quote_index][2]) + ' points!')
        score_errors[0] += quotes_copy[quote_index][2]
        
    else:
        #acknoledge missed question and update errors
        print('')
        print('Ooh, so close!')
        score_errors[1] += 1
        
    #remove used quote
    del(quotes_copy[quote_index])
    
    return score_errors
    

def displayScore(score_errors):
    """Input: list of length 2
    Output: None
    prints: score and number of errors (out of 3 possible)"""
    
    print('')
    print("Your current score is " + str(score_errors[0]))
    print("You have made " + str(score_errors[1]) + " out of 3 possible incorrect guesses")


def updateHighScore(score):
    """Input: Current score
    Output: None
    Writes: Updates high_score file with new high score and player initials"""
    
    initials = input('Congratulations, you just earned a new high score! Enter your initials: ')
    file_handle = open('high_score.py', 'w')
    file_handle.write('high_score = ' + str(score) + '\n')
    file_handle.write('high_score_initials = ' + '"' + initials + '"')
    file_handle.close()
    

def playGame():
    """Requires imported files and relevent functions defined above"""

    #Intro
    print('')
    print("Welcome to the world of tomorrow!")
    print('')
    print("It's time to test your knowledge of who said what with respect to Futurama quotes")
    print('')
    print("Do your best to beat the high score - " + str(high_score) + " by " + high_score_initials + " - you can miss up to three questions")
    
    #set score to 0 index [0], set errors to 0 index [1]
    score_errors = [0, 0]
    
    #At top of game loop - pass in as parameter
    
    #creates copy of quotes - each quote dele ted after use
    global quotes_copy
    quotes_copy = quotes.copy()
    
    #Game loop
    
    while score_errors[1] < 3:
       
        #display score
        displayScore(score_errors)
        
        #possible add a 'n' for the next question or q to quit
        
        keep_playing = input("Type 'n' for the next question or 'q' to quit: ")
        while keep_playing.lower() not in ['n', 'q']:
           keep_playing = input("Seriously though, type 'n' for the next question or 'q' to quit: ")
        if keep_playing.lower() == 'q':
            #when break is used final score is not updated score_errors
            break
    
        #generate quote index - random number - if index
        if len(quotes_copy) != 0:
            newQuoteIndex()
        else:
            print('')
            print('You made it through all of the quotes! Huzzahs are in order! Huzzah!')
            break
        #display the quote
        printQuote(quote_index)
        #display the answer choices - make answer key
        answer_key = printMultChoiceReturnKey(quote_index, returnNameChoiceList(quote_index))
        #take input to get answer - update score
        score_errors = getUserAnswer(quote_index, answer_key, score_errors)
        
        #works if all caps entered - lowercase works fine except for last wrong answer
        
    print('')    
    print('GAME OVER: FINAL SCORE = ' + str(score_errors[0]) + ' POINTS')
    
    if score_errors[0] > high_score:
        #update high score
        updateHighScore(score_errors[0])
        

