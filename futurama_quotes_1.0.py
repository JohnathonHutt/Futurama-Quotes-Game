#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:24:18 2019

@author: jhutt5383
"""

import random

quotes = [
        ["Good news everyone!", "Hubert J. Farnsworth", 1],
        ["Bite my shiny metal a$$!", "Bender B. Rodriguez", 1],
        ["Let's go microwave. I'm in a hurry here.", "Philip J. Fry", 2],
        ["I don't know what happened, but we've taken on a lot of clocks.", "Turanga Leela", 2],
        ["By the way, I took the liberty of fertilizing your caviar.", "Dr. John Zoidberg", 2],
        ["Now it's time to go home and relax the traditional jamaican way. A glass of warm milk and a good nights sleep", "Hermes Conrad", 1],
        ["Sweet gorrilla of Manilla!", "Hermes Conrad", 1],
        ["Look, everyone wants to be like Germany, but do we really have the pure strength of will?", "Amy Wong", 2],
        ["When I'm in command, every mission is a suicide mission", "Zapp Brannigan", 2],
        ["This company is going to shoot straight to the top and stay there - like Cyndi Lauper", "That Guy", 3],
        ["A complete sandwich? Ha! You got fleeced! I would have settled for a hard roll with ketchup inside.", "Dr. John Zoidberg", 2],
        ["Well, then good news! It's a suppository.", "Hubert J. Farnsworth", 2],
        ["Posers! I was hating Zoidberg before it was cool.", "Bender B. Rodriguez", 2],
        ["There are two kinds of people: sheep and sharks. Anyone who is a sheep is fired. Who is a sheep?", "That Guy", 3],
        ["What smells like blue?", "Philip J. Fry", 2],
        ["I’m so embarrassed. I wish everybody else was dead.", "Bender B. Rodriguez", 2],
        ["There. Now no one can say I don’t own John Larroquette’s spine.", "Bender B. Rodriguez", 2],
        ["If, For Any Reason You're Not Satisfied, I Hate You.", "Sales Clerk", 2],
        ["Now, Now, There Will Be Plenty Of Time To Discuss Your Objections When And If You Return.", "Hubert J. Farnsworth", 2],
        ["I did do the nasty in th pasty", "Philip J. Fry", 2],
        ["Windmills do not work that way!", "Morbo", 3],
        ["Ah the scent of a rose, curious how an aromatic chain of hydrocarbons can evoke our deepest emotions", "Philip J. Fry", 3],
        ["Oh, the hypochondriac's back! So what is it this time?", "Dr. John Zoidberg", 2],
        ["Ow! It's hot. The butter in my pocket is melting!", "Philip J. Fry", 2],
        ["Well, my lead pipe hurts a little.", "Philip J. Fry", 2],
        ["Quick! We can escape through that nasal capillary into the sinus.", "Dr. John Zoidberg", 2],
        ["That's such a beautiful thought, Fry. And what's more amazing, you expressed it without spewing crumbs at me.", "Turanga Leela", 2],
        ["But I don't like being a delivery boy.", "Philip J. Fry", 2],
        ["Shinier than yours, meatbag!", "Bender B. Rodriguez", 1],
        ["You kidding? I was a star! I could bend a girder to any angle: 30 degrees, 32 degrees, you name it!    ....31.", "Bender B. Rodriguez", 1],
        ["I'm never going to get used to the 31st century. Caffinated bacon? Baconated grapefruit? Admiral Crunch?", "Philip J. Fry", 1],
        ["Ah, Hermes! Crew, meet Hermes Conrad. He manages my delivery business, pays the bills, notifies next of kin, what have you.", "Hubert J. Farnsworth", 1],
        ["Now open your mouth and let's have a look at that brain.", "Dr. John Zoidberg", 2],
        ["Yeah, like you don't have crap in your neck!", "Bender B. Rodriguez", 2],
        ["Ah, to be young again. And also a robot.", "Hubert J. Farnsworth", 1],
        ["Ooh Big Pink! It's the only gum with the breath freshening power of ham!", "Philip J. Fry", 3],
        ["And it pinkens your teeth while you chew", "Bender B. Rodriguez", 3],
        ["Hey Fry, I'm steering with my a$$", "Bender B. Rodriguez", 1],
        ["That's the best thing I ever saw!", "Philip J. Fry", 3],
        ["I guess a robot would have to be crazy to wanna be a folk singer...", "Bender B. Rodriguez", 1],
        ["Sheesh! 40,000 channels and only 150 have anything good on.", "Philip J. Fry", 3],
        ["I don't know. Something I couldn't quite put my finger on. Possibly his vile lizard tongue.", "Turanga Leela", 2],
        ["Yeah. If you rule out every guy with a lizard tongue or a low I.Q. or an explosive violent temper, of course you're gonna be lonely.", "Philip J. Fry", 2],
        ["You just have to give guys a chance. Sometimes you meet a guy and think he's a pig, but then later you realise he actually has a really good body.", "Amy Wong", 2],
        ["We have detected a vessel attempting to break the security cordon around Vergon 6. I'm anticipating an all-out tactical dogfight, followed by a light dinner ... ravioli, ham, sundae bar.", "Zapp Brannigan", 1],
        ["In the game of chess, you can never let your adversary see your pieces.", "Zapp Brannigan", 2],
        ["You see, Killbots have a preset kill limit. Knowing their weakness, I sent wave after wave of my own men at them, until they reached their limit and shutdown.", "Zapp Brannigan", 2],
        ["I doubt I've seen more than three or four captains sexier than you, and only one who was deadlier.", "Zapp Brannigan", 2],
        ["I’ll take it. We’ll meet you tonight for part of dinner and the first half of a movie.", "Zapp Brannigan", 2],
        ["You win again, gravity!", "Zapp Brannigan", 2],
        ["Ah, yes. Comets, the icebergs of the sky.", "Zapp Brannigan", 2],
        ["I’m swelling with patriotic mucus!", "Dr. John Zoidberg", 2],
        ["Two oil changes for the price of one! Now if I could afford the one, and the car.", "Dr. John Zoidberg", 2],
        ["Friends! Help! A guinea pig tricked me!", "Dr. John Zoidberg", 2],
        ["Whoop! Whoop! Whoop!", "Dr. John Zoidberg", 1],
        ["Switzerland is small and neutral! We are more like Germany, ambitious and misunderstood!", "That Guy", 3],
        ["Yep, I remember. They came in last at the Olympics, then retired to promote alcoholic beverages.", "Philip J. Fry", 2],
        ]

#Make active quotes quotes copy - so that questions that have been asked can be removed

#Main characters have been added twice to give an effective weighted appearance - look into a better way in the future why not?

names = [
        "Hubert J. Farnsworth",
        "Bender B. Rodriguez",
        "Philip J. Fry",
        "Turanga Leela",
        "Dr. John Zoidberg",
        "Hermes Conrad",
        "Amy Wong",
        "Zapp Brannigan",
        "Hubert J. Farnsworth",
        "Bender B. Rodriguez",
        "Philip J. Fry",
        "Turanga Leela",
        "Dr. John Zoidberg",
        "Hermes Conrad",
        "Amy Wong",
        "Zapp Brannigan",
        "That Guy",
        "Sales Clerk",
        "Morbo"
        ]

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


def playGame():
    """Requires imported files and relevent functions defined above"""

    #Intro
    print('')
    print("Welcome to the world of tomorrow!")
    print('')
    print("It's time to test your knowledge of who said what with respect to Futurama quotes")
    print('')
    print("Do your best to beat the high score - you can miss up to three questions")
    
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
    
        
playGame()