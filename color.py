import tkinter 
import random 

# list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black', 
		'Yellow','Orange','White','Purple','Brown','Cyan'] 
score = 0


timeleft = 30

 
def startGame(event): 
	
	if timeleft == 30: 
		
		 
		countdown() 
		
	 
	nextColour() 

 
def nextColour(): 

	
	global score 
	global timeleft 

	
	if timeleft > 0: 

		# make the text entry box active. 
		e.focus_set() 

		# if the colour typed is equal 
		# to the colour of the text 
		if e.get().lower() == colours[1].lower(): 
			
			score += 1

		 
		e.delete(0, tkinter.END) 
		
		random.shuffle(colours) 
		
		
		label.config(fg = str(colours[1]), text = str(colours[0])) 
		
		
		scoreLabel.config(text = "Score: " + str(score)) 



def countdown(): 

	global timeleft 

	
	if timeleft > 0: 

		 
		timeleft -= 1
		
		# update the time left label 
		timeLabel.config(text = "Time left: "
							+ str(timeleft)) 
								
		 
		timeLabel.after(1000, countdown) 




 
root = tkinter.Tk() 


root.title("COLORGAME") 

 
root.geometry("375x200") 

 
instructions = tkinter.Label(root, text = "Type in the colour"
						"of the words, and not the word text!", 
									font = ('Jokerman', 20)) 
instructions.pack() 

 
scoreLabel = tkinter.Label(root, text = "Press enter to start", 
									font = ('JOkerman', 12)) 
scoreLabel.pack() 

 
timeLabel = tkinter.Label(root, text = "Time left: " +
			str(timeleft), font = ('Helvetica', 12)) 
				
timeLabel.pack() 

label = tkinter.Label(root, font = ('Helvetica', 70)) 
label.pack() 

# add a text entry box for 
# typing in colours 
e = tkinter.Entry(root) 

# run the 'startGame' function 
# when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack() 

# set focus on the entry box 
e.focus_set() 

# start the GUI 
root.mainloop() 
