import random
import csv
import datetime
import plotly.express as px

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
     saveit(scoreright, questsize)
# Random Number Generator Functions
def rannumone():
  return int(random.randint(1,1000))
def rannumtwo(): 
  return int(random.randint(1, 1000))
# Saving the score and the name to .csv
def saveit(scoreright, questsize):
  wannasave = input(str("Would you like to save your score to a .csv? Y/N?")).lower()
  if wannasave == "y":
   print("okay")
   with open('scorecard.csv', 'a', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    timewrite = '{:%Y-%m-%d}'.format(datetime.datetime.now())
    spamwriter.writerow([namez] + [scoreright] + [questsize] + [timewrite])
    scoreboard()
  else:
    print('Fine, dont save it')   
    scoreboard()
def scoreboard():
  wannsee = input('Would you like to see the scoreboard? Y/N ').lower()
  if wannsee == 'y':
    with open('scorecard.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        if line_count == 0:
          print(f'{", ".join(row)}')
          line_count += 1
        else:
          print(f'\t{row[0]}    {row[1]}/{row[2]}      {row[3]}')
        line_count += 1
    print(f'A Total of  {line_count} scores.')
  else:
    print('Okay.')

def plot():
  df = px.data.gapminder().query("country=='Canada'")
  fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
  fig.show()





# Start Menu where user is asked to put in their name and ask whether or not they want to take the math challenge.  
namez = input(" Please enter your name:")
scoreboard()
print("Would you like to test your computational skills??")
wannaplay = input("Y/N? ").lower()
if wannaplay == "y":
  questsize = int(input("How many questions do you want to answer?"))
  print(namez + " lets Begin.")
  teststart()
else:
  print("Please feel free to start when you're ready")







    
