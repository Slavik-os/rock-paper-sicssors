#!/usr/bin/env python3


from tkinter import * 
import random

moves  = ['Rock','Paper','Scissors']

class program :
	def __init__(self,master) :
		self.master = master
		master.geometry('600x550')
		
		# Buttons 
		
		self.rock = Button(master,text="Rock",command=lambda:self.choseMove(moves[0])).pack()	
		self.paper = Button(master,text="Paper",command=lambda:self.choseMove(moves[1])).pack()	
		self.scissor = Button(master,text="Scissors",command=lambda:self.choseMove(moves[2])).pack()	
		# Text

		self.text = Text(master,width=50, height=20)
		self.text.pack()

	# logic 
		
	def cp_choice(self) :
		return random.choice(moves)
	def choseMove(self,move) :
		winner = False 	
		cp  = self.cp_choice()
		self.text.delete('1.0',END)
		res =  'Your Choice : \t'+move+'\n'+'Computer Choice : \t'+cp
		self.text.insert(END,res)
		
		if move == moves[0] and cp == moves[1] :    # Rock vs paper
			winner = False 
			print('Machine!')
			
		elif move == moves[0] and cp == moves[2] :    # Rock vs Scissors
			winner = True
			print('Human !')


		elif move == moves[1] and cp == moves[2] :    # Rock vs Scissors
			winner = False
			print('Machine !')


		elif move == moves[1] and cp == moves[0] :    # Rock vs Scissors
			winner = True
			print('Human !')
		
		elif move == moves[2] and cp == moves[0] :    # Rock vs Scissors
			winner = False
			print('Machine !')


		elif move == moves[2] and cp == moves[1] :
			winner = True
			print('Humane!')


		elif move  == cp  :
			self.text.delete('1.0',END)
			self.text.insert(END,res+'\n Draw !')
			winner = None 
		else :
			print('Something went wrong! try Again !?')
		
		if winner == True :
			self.text.delete('1.0',END)
			self.text.insert(END,res+'\n'+'Winner : Human!')

		elif winner == False :
			self.text.delete('1.0',END)
			self.text.insert(END,res+'\n'+'Winner : Machine!')
			

	# Check of winner
	

	
root = Tk()
gui = program(root)
root.mainloop()
