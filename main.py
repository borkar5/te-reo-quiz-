#te reo quiz- 10 questions 

import os
import time
score = 0
#these lines of code will start the quiz 
def quiz_stort():
  global score
  print("have you played the te reo maori quiz before? ")
  quiz_start = input().lower()
  print(quiz_start)
  if quiz_start == "yes" or quiz_start =="y":
    question_start()
  
  elif quiz_start == "no" or quiz_start == "n":
    os.system('clear')
    show_instructions()
  
  else:
    os.system('clear')
    print("please answer yes or no. ")
    time.sleep(2)
    os.system('clear')
    quiz_stort()
    
    

#this is the instructions function 
def show_instructions():
  print("instructions ")
  
  time.sleep(2)
  
  print("are you ready to play yet?")
  play_now = input().lower()

  if play_now == "yes" or play_now == "y":
    os.system('clear')
    question_start()

  elif play_now == "no" or play_now == "n":
    os.system('clear')
    print("here are the instrutions again.")
    show_instructions()
    


  else:
    os.system('clear')
    show_instructions()
    
  
    
  


#this function decorates the intro statement 
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""
    
#these lines will be the questions 



def question_start():
  global score
  print("Question 1:")
  print("what is the maori word for car?")
  print("A: kapua")
  print("B: Waea")
  print("C: motoka")
  print("D: koromatua")
  question_1 = input().lower()
  if question_1 == "c" or question_1 == "motoka":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question2_start()
  
  elif question_1 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question2_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question2_start()


def question2_start():
  global score
  print("Question 2:")
  print("question?")
  print("A: ")
  print("B: ")
  print("C: ")
  print("D: ")
  question_2 = input().lower()
  if question_2 == "c" or question_2 == "c":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question3_start()
  
  elif question_2 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question3_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question3_start()



def question3_start():
  global score
  print("Question 3:")
  print("question?")
  print("A: ")
  print("B: ")
  print("C: ")
  print("D: ")
  question_3 = input().lower()
  if question_3 == "c" or question_3 == "c":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question4_start()
  
  elif question_3 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question4_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question4_start()



def question4_start():
  global score
  print("Question 4:")
  print("question?")
  print("A: ")
  print("B: ")
  print("C: ")
  print("D: ")
  question_4 = input().lower()
  if question_4 == "c" or question_4 == "c":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question5_start()
  
  elif question_4 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question5_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question5_start()


def question5_start():
  global score
  print("Question 5:")
  print("question?")
  print("A: ")
  print("B: ")
  print("C: ")
  print("D: ")
  question_5 = input().lower()
  if question_5 == "c" or question_5 == "c":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question6_start()
  
  elif question_5 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question6_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question6_start()


def question6_start():
  global score
  print("Question 6:")
  print("question? ")
  print("A: ")
  print("B: ")
  print("C: ")
  print("D: ")
  question_6 = input().lower()
  if question_6 == "c" or question_6 == "c":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question7_start()
  
  elif question_6 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question7_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question7_start()




def question7_start():
  global score
  print("Question 7:")
  print("question?")
  print("A: ")
  print("B: ")
  print("C: ")
  print("D: ")
  question_7 = input().lower()
  if question_7 == "c" or question_7 == "c":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    #question_start()
  
  elif question_7 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    #question_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    #question_start()
    

  
#these lines of code will greet the user and ask them weather they would like to play
statement_generator("welcome to the te reo maori quiz", "#")

quiz_stort()
