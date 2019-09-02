import pyttsx3,sys,time
from termcolor import colored,cprint
from pygame import mixer
engine=pyttsx3.init()
voices = engine.getProperty('voices')
'''if (voice.id=='hindi') in voices:
	engine.say('The quick brown fox jumped over the lazy dog.')
	engine.runAndWait() 
'''
def correct():
	engine.say('Correct Answer')
	engine.runAndWait()
	print(colored("Correct Answer",'green'))
	time.sleep(2)
def incorrect():
	engine.say('Incorect Answer')
	engine.runAndWait()
	print(colored("Wrong answer",'red'))
	print('Thanks for playing')
	time.sleep(2)

def clock():
	mixer.init()
	mixer.music.load('/home/Downloads/Tick Tock Sound Effect.mp3')
	mixer.music.play()

mixer.init()
mixer.music.load('/home/Downloads/Kaun Banega Crorepati.mp3')
mixer.music.play()
time.sleep(15)
count=0	
print("\t\t WELCOME TO KBC QUIZ\t\t")
time.sleep(1)
print('''There will be total 10 questions to answer''')
time.sleep(1)
print('SO HERE COMES THE FIRST QUESTION')
time.sleep(1)
print(colored('QUESTION 1','blue'))
print("Who was the first prime minister of india")
print("a.Jawahrlal Nehru")
print("b.Narendra Modi")
print("c.Dr. Rajendra Prasad")
print("d.Motilal Nehru")
clock()
opt=input("Enter Choice ")
if (opt=='a' or opt=='A'):
	correct()
	count+=1
elif (opt=='b' or opt=='B' or opt=='C' or opt=='c' or opt=='D' or opt=='d'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
print(colored('QUESTION 2','blue'))
print('Which of these personalities was appointed as the youngest ever UN Messenger of Peace in April 2017')
print('a.Malia Obama')
print('b.Priyanka Chopra')
print('c.Aylan Kurdi')
print('d.Malala Yousafzai')
clock()
opt=input("Enter Choice ")
if (opt=='d' or opt=='D'):
	correct()
	count+=1
elif (opt=='b' or opt=='B' or opt=='C' or opt=='c' or opt=='A' or opt=='a'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
print(colored('QUESTION 3','blue'))
print("According to the Guinness World Records, variety of which of these birds has the fastest wing beat")
print("a.Sparrow")
print("b.Hummingbird")
print("c.Myna")
print("d.Kingfisher")
clock()
opt=input("Enter Choice ")
if (opt=='b' or opt=='B'):
	correct()
	count+=1
elif (opt=='a' or opt=='A' or opt=='C' or opt=='c' or opt=='D' or opt=='d'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
print(colored('QUESTION 4','blue'))
print("Who became the first woman to head India's External Affairs Ministry")
print("a.Indira Gandhi")
print("b.Sushma Swaraj")
print("c.Meira Kumar")
print("d.Rajkumari Amrit Kaur")
clock()
opt=input("Enter Choice ")
if (opt=='a' or opt=='A'):
	correct()
	count+=1
elif (opt=='b' or opt=='B' or opt=='C' or opt=='c' or opt=='D' or opt=='d'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
print(colored('QUESTION 5','blue'))
print("Which of these group of bones is also called 'merudand'")
print("a.Backbone")
print("b.Skull")
print("c.Pelvis")
print("d.Ribs")
clock()
opt=input("Enter Choice ")
if (opt=='a' or opt=='A'):
	correct()
	count+=1
elif (opt=='b' or opt=='B' or opt=='C' or opt=='c' or opt=='D' or opt=='d'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
print(colored('QUESTION 6','blue'))
print("In which field did Jeffrey Hall, Michael Rosbash and Michael Young won the 2017 Nobel Prize")
print("a.Physiology or Medicine")
print("b.Physics")
print("c.Chemistry")
print("d.Literature")
clock()
opt=input("Enter Choice ")
if (opt=='a' or opt=='A'):
	correct()
	count+=1
elif (opt=='b' or opt=='B' or opt=='C' or opt=='c' or opt=='D' or opt=='d'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
print(colored('QUESTION 7','blue'))
print("Which ruler's conservation efforts in the early 20th century saved the Asiatic lion from the brink of extinction in India")
print("a.Maharaja of Baroda")
print("b.Nawab of Junagadh")
print("c.Maharaja of Nawanagar")
print("d.Nawab of Rampur")
clock()
opt=input("Enter Choice ")
if (opt=='b' or opt=='B'):
	correct()
	count+=1
elif (opt=='a' or opt=='A' or opt=='C' or opt=='c' or opt=='D' or opt=='d'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
print(colored('QUESTION 8','blue'))
print("Which country gets its name because it is believed that Christopher Columbus first sighted it on a Sunday")
print("a.Ecuador")
print("b.Chile")
print("c.Dominica")
print("d.Fiji")
clock()
opt=input("Enter Choice ")
if (opt=='c' or opt=='C'):
	correct()
	count+=1
elif (opt=='b' or opt=='B' or opt=='a' or opt=='A' or opt=='D' or opt=='d'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
print(colored('QUESTION 9','blue'))
print("According to Mahabharata, what was the name of the conch blown by Sahadeva in the battlefield of kurukshetra")
print("a.Anatvijaya")
print("b.Manipushpak")
print("c.Sugosh")
print("d.Paundra")
clock()
opt=input("Enter Choice ")
if (opt=='b' or opt=='B'):
	correct()
	count+=1
elif (opt=='a' or opt=='A' or opt=='C' or opt=='c' or opt=='D' or opt=='d'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
print(colored('QUESTION 10','blue'))
print("Which colonial power ended its involvement in india by selling the rights of the Nicobar Islands to the British on October 16,1868")
print("a.Belgium")
print("b.Italy")
print("c.Denmark")
print("d.France")
clock()
opt=input("Enter Choice ")
if (opt=='c' or opt=='C'):
	correct()
	count+=1
elif (opt=='b' or opt=='B' or opt=='A' or opt=='a' or opt=='D' or opt=='d'):
	incorrect()
	print('You answered', count, 'questions correctly' )
	sys.exit()	
else:
	print("Invalid Choice")
	print("Thanks for playing")
	sys.exit()
