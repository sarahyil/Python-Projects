'''
Sarah Yildirim
9/25/20
OMH
Sources: None
Description: This game was inspired by the TV show Friends. I thought that I would create my own twist
and make the game based on Phoebe. Ultimately, the user is going through the day by planning for the birthday
and then there's a package at the door. The package is from Phoebe's parents and it turns out that Phoebe's sister
invited them. The user has to then decide on how to move forward without making Phoebe upset. At the end of the
game, the user finds out if Phoebe had a good or a bad birthday.

For this game, I had to restart after I submitted by draft because I liked this idea more. This code was hard
at first because I had many little errors. Once I continued writing the code, I got the hang of it and was able
to write it without errors. This game (not counting the first one I made before) probably took around 4-6 to code.
Overall, I am very happy with the outcome and I think that it's a very fun choose your own adventure. Also, the game
is "unbreakable" in the sense that it always asks the user to try again if they input something that isn't correct.
'''

# import
import time
# functions

def greet():
	'''
	this function is getting the user's name
	'''
	global user_name
	print("Welcome to the Friends inspried game!")
	time.sleep(1)
	user_name = input("Please enter what you would like to be called during the game: ")
	print("Nice to meet you, "+user_name+"! Now time to go to Central Perk...")
	cafe()


def cafe():
	'''
	This funtion is the intro where they are at central perk. It is Phoebe's birthday and the user has to decide whether
	to wish her a Happy Birthday or not.
	'''
	time.sleep(1)
	print("Today we enter Central Perk, a fun cafe the group likes to hang out at after their busy days. You remember that today is Phoebe's birthday! You totally forgot because you had a busy day at work. You enter the cafe.")
	print("\n"+user_name+", do you wish her a Happy Birthday or don't mention it because you didn't get her anything? Enter a yes if you want to mention it and a no if you don't mention it.")
	decision_one = input()
	if decision_one == 'yes':
		yes_bday()
	elif decision_one == 'no':
		no_bday()
	else:
		print("Only yes or no. Try again.")
		cafe()

def yes_bday():
	'''
	This function is where the user decided on wishing Phoebe a 
	Happy Birthday. Afterwards, Phoebe leaves and the user decided if
	they want to go to the surprise party.
	'''
	print("Great! You wish Phoebe a happy birthday and she thanks you by singing Smelly Cat!")
	time.sleep(2)
	print("\nAfter you and Phoebe chat a little bit, the rest of the friends walk in. Phoebe says that she has to go home because she's tired. Ross and Rachel mention a surprise party for tonight. Do you want to go?")
	yes_birthday = input()
	if yes_birthday == 'yes':
		surprise()
	elif yes_birthday == 'no':
		home()
	else:
		print("Try again!")
		yes_bday()


def no_bday():
	'''
	This function is where the user doesn't wish Phoebe a Happy Birthday but ends
	up wishing her a happy birthday because of Gunther. Then Phoebe leaves and the user decides
	if they want to go to the surprise party.
	'''
	print("You don't mention anything for a few minutes. Then, Gunther brings over your drink and wishes Phoebe a Happy Birthday. You instantly feel bad and wish her a Happy Birthday. She just says thank you and doesn't sing for you like she usually does. You wonder if everything is ok but brush it off once your friends arrive.")
	time.sleep(3)
	print("\nYour friends came and after chatting for a bit, Phoebe leaves and goes home.")
	time.sleep(3)
	print("\nRoss and Rachel mention a surprise party they are throwing Phoebe for tonight. Do you want to go? ")
	no_birthday = input()
	if no_birthday == 'yes':
		surprise()
	elif no_birthday == 'no':
		home()
	else:
		print("Try again!")
		no_bday()

def surprise():
	'''
	This function is where they are now back to their place.
	The user decides if they want to help put up decorations or
	wrap the presents.
	'''
	print("Ross and Rachel invite all of you back to their place. The party is supposed to begin in two hours.")
	time.sleep(1)
	print("\nDo you want to help by putting up the decorations, or do you want to wrap presents?")
	helping = input()
	if helping == 'decorations':
		decor()
	elif helping == 'presents':
		presents()
	else:
		print("Try again!")
		surprise()

def home():
	'''
	This function is where the user then feels bad for not going to the party and changes their mind.
	'''
	print("Now that you are home, you feel bad for saying you don't want to go to the surprise party. You call Ross and tell him you've changed your mind and that you'll be there in half an hour. He says you can help with wrapping the presents and getting ready!")
	presents()

def presents():
	'''
	This function is where the user is wrapping presents. Then, someone is at
	the door and the user decides if they want to open the door or not.
	'''
	print("You being wrapping presents with Joey. But, he is going very slow and the ducks are distracting him. You ignore this and keep wrapping the presents on your own. The whole crew is listening to music as you all get ready for the big party. Suddenly, there's a knock at the door. Phoebe isn't supposed to be there for another hour!! Do you guys open the door?")
	knocking = input()
	if knocking == 'yes':
		open_door()
	elif knocking == 'no':
		ignore_door()
	else:
		print("Try again!")
		presents()

def decor():
	'''
	This function is where the user is putting up decorations with Rachel.
	Then, someone is at the door and the user decided to open it or not.
	'''
	print("You decide to put up decorations. Rachel helps you with this and you guys chat about your days while listening to music. Suddenly, there's a knock at the door. Phoebe isn't supposed to be there for another hour!! Do you guys open the door?")
	knock = input()
	if knock == 'yes':
		open_door()
	elif knock == 'no':
		ignore_door()
	else:
		print("Try again!")
		decor()

def open_door():
	'''
	This function is where they open the door and they see that the package is from Phoebe's
	parents. The user decides to open the package or not.
	'''
	print("Ross finally opens the door once everyone is hiding. There's a package. The package is from Phoebe's parents. That's strange... they don't know this address considering Phoebe doesn't live there. Do you guys want to open the package?")
	package = input()
	if package == 'yes':
		open_package()
	elif package == 'no':
		ignore_package()
	else:
		print("Try again!")
		open_door()

def ignore_door():
	'''
	This function is where they don't open the door. But, after some time
	Ross finally opens the door. The user decides to open the package or not.
	'''
	print("You guys don't open the door. The knocking continues for a few minutes and then they leave. After 15 minutes, Ross carefully opens the door. There's a package. The package is from Phoebe's parents. That's strange... they don't know this address considering Phoebe doesn't live there. Do you guys want to open the package?")
	package_phoebe = input()
	if package_phoebe == 'yes':
		open_package()
	elif package_phoebe == 'no':
		ignore_package()
	else:
		print("Try again!")
		ignore_door()

def open_packagae():
	'''
	This function is where the user decided to open the package. Then the
	user decides if they want to tell Phoebe's sister if the parents should or should not come.
	'''
	print("You open the package! You find a letter from her parents. Turns out, Phoebe's sister invited Phoebe's parents over for the surprise party without telling anyone. You guys know that Phoebe hasn't talking to her parents in years.")
	time.sleep(2)
	print("Do you tell Phoebe's sister that the parents can't come?")
	tell_sister = input()
	if tell_sister == 'yes':
		sister()
	elif tell_sister == 'no':
		no_sister()
	else:
		print("Try again!")
		open_package()

def ignore_package():
	'''
	This function is where they ignore the package but then Joey goes and opens it. They then
	have to decide if they should tell Phoebe's sister if the parents should or should not come.
	'''

	print("You guys ignore the package at first. Then, Joey goes and secretly opens it because he loves presents. He sees that the package is from Phoebe's parents but still opens it. It's a letter saying that they will be coming to the surprise party.")
	time.sleep(2)
	print("\nTurns out, Phoebe's sister told them.")
	time.sleep(2)
	print("\nDo you guys tell Phoebe's sister that the parents can't come?")
	sister_tell = input()
	if sister_tell == 'yes':
		sister()
	elif sister_tell == 'no':
		no_sister()
	else:
		print("Try again!")
		ignore_package()

def sister():
	'''
	This is the function where the user decides that the parents shouldn't come. They soon find out that
	the parents have to come because they are already in town.
	'''
	print("You tell her that the parents can't come because Phoebe wouldn't want them there. She says they're already in NYC at a hotel nearby and they are insisting on coming. You have no choice but to not tell Phoebe. It will be a surprise for her")
	almost_time()

def no_sister():
	'''
	This is the function where the user decides to not say anything. They soon find out that
	the parents have to come anyways because they are already in town.
	'''
	print("You don't say anything to Phoebe's sister. Turns out the parents are already in NYC anyways, so it wouldn't have mattered. You're worried about how Phoebe will react but are hoping she doesn't mind. It will be a surprise for her.")
	almost_time()

def almost_time():
	'''
	This is when the parents come and they surprise Phoebe. She is shocked and runs out.
	The user decides whether to run after Phoebe or not.
	'''
	time.sleep(4)
	print("\n\nPhoebe's parents arrive. You had met them many years back... when Phoebe still talked to them. Phoebe will be arriving any minute now. Everyone hides.")
	time.sleep(4)
	print("\n\nPhoebe walks in! You all jump out and scare her and wish her a happy birthday! She sees her parents and stands there in shock. Suddenly, she runs out. Do you go chase after her?")
	chase = input()
	if chase == 'yes':
		chase_after()
	elif chase == 'no':
		dont_chase()
	else:
		print("Try again!")
		almost_time()

def chase_after():
	'''
	This is the function where they chase after Phoebe.
	'''
	print("You chase after Phoebe and try talking to her. She says she's shocked that they would actually come. She had missed them a lot and tells you to go get them.")
	time.sleep(1)
	print("You come back with her parents and they talk. Turns out, Phoebe really had missed her parents, and she was so happy they were there for her birthday.")
	ending_one()

def dont_chase():
	'''
	This is the function where they don't chase after Phoebe.
	'''

	print("You don't chase Phoebe. You guys wait for half an hour until you start getting worried. You guys call her and search for her but don't hear anything. Turns out, she didn't want her parents there. She's upset and says her day is ruined.")
	time.sleep(4)
	print("\n\nYou feel terrible and don't know what to do. You tell her parents to leave and that you will talk to Phoebe. They leave. You talk to Phoebe about it and she eventually forgives you all. Her day has been ruined, but she still is thankful to have all of you as her friends.")
	ending_two()

def ending_one():
	'''
	This is the ending where they chase after Phoebe.
	'''
	time.sleep(2)
	print("\nGreat job today! Phoebe is happy and she has reconnected with her parents! She hopes to talk to them more often and she says that she had an amazing birthday.")

def ending_two():
	'''
	This is the ending where they don't chase after Phoebe
	'''
	time.sleep(2)
	print("\nPhoebe doesn't want to see her parents ever again. She is upset and says that it was a terrible birthday. You are sad that you made your friend upset. She still is thankful for you all and you hope that she isn't lying. You now know not to allow anyone to invite Phoebe's parents to her birthday party ever again!")


greet()


'''
Comments/Feedback:

Grace Liu: I think you should add some time between certain sentences because it will then make the lines easier to read.
	Resolved by adding time between lines in most of the functions.

Tyler: There are some spelling mistakes within your code. Try and fix those and also make your sentences more descriptive.
	Resolved by fixing all grammar mistakes and also by adding more descriptions to my sentences.

Zoe: Add a description to your functions so that it is clear what each one is doing.
	Resolved by including clear descriptions to each of the functions.

Ms. Healey: Include decriptions to the functions so that they can be easily understood by the person looking at the code.
	Resolved by including clear descriptions to each of the functions.

'''



		 



	

