def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("invalid input! enter a number")


#calculator
def calculator():
    x=get_int("enter your number:")
    y=get_int("enter your number:")

    print("1.Add")
    print("2.Sub")
    print("3.Mul")
    print("4.Div")

    choice=get_int("Enter your choice:")

    if choice==1:
        print("x+y=",x+y)
    elif choice==2:
        print("x-y=",x-y)
    elif choice==3:
        print("x*y=",x*y)
    elif choice==4:
        print("x/y=",x/y)

    print("solution")        

   
   
    #2 guess.py        
import random
target = random.randint(1,100)
def guess():

    while True:
        userchoice=(input("Guess the target or Quit: "))
        if(userchoice=="Quit"):
            break
        userchoice=int(userchoice)
        if(userchoice==target):
            print("Won")
        elif(userchoice<target):
            print("number is too small guess bigger")
        elif(userchoice>target):        
            print("number is too big guess smaller")

            print("____game over____")



#3 stone_paper_scissors
import random
def stone_paper_scissors():
    choices = ["STONE","PAPER","SCISSOR"]

    user=input("choice STONE,PAPER,OR SCISSOR :")
    computer=random.choice(choices)

    if user not in choices:
        print("invalid choice")
    elif user == computer:
        print("match draw")
    elif (user=="STONE"and computer=="SCISSOR")or\
        (user=="PAPER"and computer=="STONE")or\
            (user=="SCISSOR"and computer=="PAPER"):
            print("YOU WON")

    else:
        print("YOU LOSE")                            


# 4 digital_clock

import tkinter as tk
import time

def digital_clock():
    root = tk.Tk()
    root.title("Digital Clock")

    label = tk.Label(root, font=("time and roman",130),background="red")
    label.pack(padx=20,pady=20)


    def update_clock():
        current_time = time.strftime("%H:%M:%S")
        label.config(text=current_time)
        root.after(1000,update_clock)

    update_clock()
    root.mainloop()        


#5 Expense_tracker

def Expense_tracker():
    expenses=[]
    while True:
        print("\n----Expense Tracker----")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Exit")

        choice=input("Enter your choice : ")

        if choice =="1":
            name=input("Enter expense name : ")
            amount=float(input("Enter amount : $"))

            expenses.append({"name":name, "amount":amount})
            print("Expense added successfully!")

        elif choice == "2":
            for expense in expenses :
                print(expense["name"],"-$",expense["amount"])
        elif choice=="3":
            total = sum(e["amount"] for e in expenses)
            print("total expenses : $",total)
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("invalid choice!")    

