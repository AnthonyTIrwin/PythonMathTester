import random

# function that creates random numbers from 1 to 1000 and asks user math problem.

def teststart():
  testvara = int(random.randint(1, 1000))
  testvaratwo = int(random.randint(1, 1000))
  print("What's " + str(testvaratwo) + " plus " + str(testvara))
  answer = input("Answer: ")
  if answer == testvara + testvaratwo:
    print("Good Job!")
  else:
      print("How shameful, try again!!")
  return

# Start Menu where user is asked to put in their name and ask whether or not they want to take the math challenge.  
namez = input(" Please enter your name:")
print("Welcome " + namez + " would you like to test your computational skills?")
wannaplay = input("Y/N?")
if wannaplay == "Y":
  print(namez + "Lets Begin.")
  teststart()
else:
  print("Please feel free to start when you're ready")






    
