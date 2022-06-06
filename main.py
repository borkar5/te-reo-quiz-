#te reo quiz- 10 questions 

import os
import time
score = 0


#quiz end 
def quiz_end():
  print("that is the end of the quiz")
  print("your score was {}".format(score))

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
  print("this is a ten question te reo maori quiz. ")
  time.sleep(1)
  print("you will be asked questions you must answer with the corospondng letter")
  time.sleep(1)
  print("you will find out your score after each question. ")
  time.sleep(1)
  print("you must get 6 or more questions correct if you want to pass")
  time.sleep(1)
  print("anything under six you will fail")
  
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
  print("what is the maori word for apple?")
  print("A:panana ")
  print("B:aporo ")
  print("C:karaka ")
  print("D:makimaki ")
  question_2 = input().lower()
  if question_2 == "b" or question_2 == "aporo":
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
  print("what is the maori word for dog?")
  print("A:kanohi ")
  print("B:mokoweri")
  print("C:tangata ")
  print("D:kuri ")
  question_3 = input().lower()
  if question_3 == "d" or question_3 == "kuri":
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
  print("what is the maori word for number 1 ?")
  print("A:tahi ")
  print("B:ure ")
  print("C:i roto ia tatou ")
  print("D:watea ")
  question_4 = input().lower()
  if question_4 == "a" or question_4 == "tahi":
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
  print("what is the maori word for hello?")
  print("A:whakapohehe ")
  print("B:kia ora ")
  print("C:āe ")
  print("D:mātauranga ")
  question_5 = input().lower()
  if question_5 == "b" or question_5 == "kia ora":
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
  print("what is the maori word for nose? ")
  print("A:ihu ")
  print("B:upoko ")
  print("C:makka pakka ")
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
    question8_start()
  
  elif question_7 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question8_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question8_start()




def question8_start():
  global score
  print("Question 8:")
  print("question?")
  print("A: ")
  print("B: ")
  print("C: ")
  print("D: ")
  question_8 = input().lower()
  if question_8 == "c" or question_8 == "c":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question9_start()
  
  elif question_8 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question9_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question9_start()

def question9_start():
  global score
  print("Question 9:")
  print("question?")
  print("A: ")
  print("B: ")
  print("C: ")
  print("D: ")
  question_9 = input().lower()
  if question_9 == "c" or question_9 == "c":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question10_start()
  
  elif question_9 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question10_start()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    question10_start()




def question10_start():
  global score
  print("Question 10:")
  print("question?")
  print("A: ")
  print("B: ")
  print("C: ")
  print("D: ")
  question_10 = input().lower()
  if question_10 == "c" or question_10 == "c":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    quiz_end()
  
  elif question_10 == "no":
    print("incorrect")
    score -= 1
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    quiz_end()

  else:
    print("incorrect")
    score -= 0
    print("your score is {}".format(score))
    time.sleep(1)
    os.system('clear')
    quiz_end()
#these lines of code will greet the user and ask them weather they would like to play
statement_generator("welcome to the te reo maori quiz", "#")

quiz_stort()
