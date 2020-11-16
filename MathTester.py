import random

# function that creates random numbers from 1 to 1000 and asks user math problem.

def teststart():

  testvaraone = rannumone()
  testvaratwo = rannumtwo()
  score = 0
  
#  testvaratwo = int(random.randint(1, 1000))
  print("What's " + str(testvaratwo) + " plus " + str(testvaraone))
  
  answer = int(input("Answer: "))
  
  if answer == testvaraone + testvaratwo:
    print("Good Job!")
    score += 1
    print("You have a score of " + str(score))
  else:
      print("How shameful, try again!!")
  
def rannumone():
  return int(random.randint(1,1000))

def rannumtwo():
  return int(random.randint(1, 1000))

# Start Menu where user is asked to put in their name and ask whether or not they want to take the math challenge.  
namez = input(" Please enter your name:")
print("Welcome " + namez + " would you like to test your computational skills?")
wannaplay = input("Y/N?")
if wannaplay == "Y":
  print(namez + "Lets Begin.")
  teststart()
else:
  print("Please feel free to start when you're ready")






    
