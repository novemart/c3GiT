#from rpsModule import welcome, user_choice, computer_choice, find_winner

from my_modules import rpsModule as myModule

again = ''

while again != 'n':
	myModule.welcome()
	user = myModule.user_choice()
	computer = myModule.computer_choice()
	myModule.find_winner(user, computer)
	again = input("Again? ")








	#need to add the no option to run the code again
	#why is it printing none?
	#how can i change the code to include functions