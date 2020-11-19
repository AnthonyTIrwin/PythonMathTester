import random
import csv
import datetime

# Function that starts the math assesment.   
def teststart():
  
  scoreright = 0
  counter = 0
  
  while counter < questsize:

    testvaraone = rannumone()
    testvaratwo = rannumtwo()
    
    print("What's " + str(testvaratwo) + " plus " + str(testvaraone))
  
    answer = int(input("Answer: "))
  
    if answer == testvaraone + testvaratwo:
      print("Good Job!")
      scoreright += 1
      counter += 1
    
    else:
      print("Wrong!")
      counter += 1
  else:
     print('You got ' + str(scoreright) + ' out of ' + str(questsize) + ' questions!')
     saveit(scoreright)

# Random Number Generator Functions

def rannumone():
  return int(random.randint(1,1000))

def rannumtwo():
  return int(random.randint(1, 1000))



# Saving the score and the name to .csv

def saveit(scoreright):
  wannasave = input(str("Would you like to save your score to a .csv? Y/N?")).lower()
  
  if wannasave == "y":
   print("okay")
   with open('scorecard.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
    quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    timewrite = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    
    spamwriter.writerow([namez] + [" had a score of "] + [scoreright] + [timewrite])
  
  else:
    print('Fine, dont save it')

  

    # Start Menu where user is asked to put in their name and ask whether or not they want to take the math challenge.  






namez = input(" Please enter your name:")

print("Welcome " + namez + " would you like to test your computational skills?")

wannaplay = input("Y/N? ").lower()

if wannaplay == "y":
  questsize = int(input("How many questions do you want to answer?"))
  print(namez + "Lets Begin.")
  teststart()
else:
  print("Please feel free to start when you're ready")
