import random
import csv
import datetime
import requests

# Added feature of local temperature API.
def whatisweather(): 
  API_key = "f360ccaab20b5b1f7087127ed1a6d955"
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  zip_code = input("Enter your Zip code: ")
  Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code
  weather_data = requests.get(Final_url).json()
  localinf = weather_data['main']['temp']
  ink = (localinf - 273.15) * 1.8 + 32
  print('The temperature in ' + weather_data['name'] + " is " + str(round(ink)) + 'F')

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
    again()
  else:
    print('Fine, dont save it')  
    again() 

# Function that reads .csv vile and displays the Name, Score and Date
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

# Asks for another try at it.
def again():
  anothertry = input('Do you want to try again? Y/N ').lower()
  if anothertry == "y":
    teststart()
  else:
    print('Goodbye!')

# Start Menu where user is asked to put in their name and ask whether or not they want to take the math challenge.  
whatisweather()
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