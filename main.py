#te reo quiz- 10 questions 



#these lines of code will start the quiz 
def quiz_stort():
  print("have you played the te reo maori quiz before? ")
  quiz_start = input().lower()
  print(quiz_start)
  if quiz_start == "yes" or quiz_start =="y":
    question_start()
  
  elif quiz_start == "no" or quiz_start == "n":
    show_instructions()
  
  else:   
    print("please enter yes or no! ")
    

#this is the instructions function 
def show_instructions():
  print("instructions ")


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
  score = 0
  print("Question 1:")
  print("what is the maori word for car?")
  print("A: kapua")
  print("B: Waea")
  print("C: Waka")
  print("D: koromatua")
  question_1 = input().lower
  if question_1 == "a" or question_1 == "waka":
    print("correct") 
    score += 1
    print("your score is {}".format(score))
  else: 
    print("incorrect")
    score += 0
    print("your score is {}".format(score))

#these lines of code will greet the user and ask them weather they would like to play
statement_generator("welcome to the te reo maori quiz", "#")

quiz_stort()
