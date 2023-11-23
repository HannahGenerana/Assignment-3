from colorama import Fore, Back, Style, init #for text color 
init(convert=True) 
from tkinter import messagebox
from tkinter import*
import tkinter as tk
from tkinter import simpledialog
import time

def total_purchase():
    # the amount of money the user have
    user_inp_money 

    # price of apple
    apple_price = 20

    # calculate the maximum number of apples you can buy
    time.sleep(0.5)
    quantity_apple = int(input(Fore.LIGHTYELLOW_EX+ Style.BRIGHT+"How many apples would you like to purchase, our dear customer?"))
    amount_apple = apple_price * quantity_apple
    max_apple_purchase = user_inp_money // apple_price

    # calculate the purchase apple
    apple_purchase = amount_apple

    # calculate the remaining money after purchasing apples
    balance_money = user_inp_money - (apple_price * quantity_apple)

    # show the purchased apples and remaining money
    time.sleep(0.5)
    print(Fore.LIGHTBLUE_EX+ Style.BRIGHT+f"You have a amount of {user_inp_money:.2f} pesos and you can buy a maximum of {int(max_apple_purchase)} apples!")
    time.sleep(0.5)
    print(Fore.LIGHTGREEN_EX+f"You only purchased a {quantity_apple} pieces of apples. This is total to {apple_purchase:.2f} pesos.")
    time.sleep(0.5)
    print(Fore.LIGHTRED_EX+f"You'll now have {balance_money:.2f} pesos remaining to your money")

def verify_purchased():
    purchase = input (Fore.LIGHTYELLOW_EX+ Style.BRIGHT+"Is this all you want to purchase? (yes/no)")
    if purchase == "yes":
      messagebox.askyesno(title='Fruity Fruits Shop', message='We are now placing your order. Please click yes if you want to continue the process.')
      messagebox.showinfo(title='Fruity Fruits Shop', message='We already process your order. Thank you for ordering!')

    if purchase == "no":
        time.sleep(0.5)
        print (Fore.LIGHTMAGENTA_EX+"We will process your concern right away!")

        process_customer_request()

def placing_order():
    continue_order = input("Are you sure you would like to place your order? (yes/no)")
    if continue_order == "yes":
        messagebox.showwarning(title='Fruity Fruits Shop', message= "We will now place your order.")
        messagebox.showinfo(title='Fruity Fruits Shop', message=' Thank you so much for purchasing to our shop! We hope to see you again soon!')

    if continue_order == "no":
        messagebox.showinfo(title='Fruity Fruits Shop', message='We are sorry if we failed to manage your order.')

def calculate_added_quantity():
    user_inp_money

    apple_price = 20
    
    # calculate added quantity of apples
    time.sleep(0.5)
    new_quantity = int(input (Fore.LIGHTRED_EX+"How many apples you would like to purchase?"))
    new_apple_quantity = new_quantity

    # calculate the final amount purchase
    final_amount = apple_price * new_apple_quantity

    # calculate the remaining money 
    total_balance = (user_inp_money) - (final_amount)
    
    # show the total purchased apples and remaining money
    time.sleep(0.5)
    print(Fore.CYAN+Style.BRIGHT+f"You purchased a {new_apple_quantity} pieces of apples. This is total to {final_amount:.2f} pesos.")
    time.sleep(0.5)
    print(Fore.LIGHTBLUE_EX+f"You'll now have {total_balance:.2f} pesos remaining to your money")

def process_customer_request():
    print (Fore.MAGENTA+"What seems to be the problem?")
    time.sleep(0.5)
    customer_request = input (Fore.LIGHTBLUE_EX+"a. I would like to change the quantity of the apples    b. I would like to cancel my order")
    if customer_request == "a":
        calculate_added_quantity()
        placing_order()
        time.sleep(0.15)
    
    if customer_request == "b":
        print(Fore.WHITE+"I'm sorry to know that you are cancelling your order.")

messagebox.showinfo(title='Fruity Fruits Shop', message='Welcome to Fruity Fruits Shop where all fruits are freshly harvest!')
messagebox.showinfo(title='Fruity Fruits Shop', message='We only accept E-Payment this time')

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
user_inp = simpledialog.askstring (title="Fruity Fruits Shop", prompt="What is your name?")
user_inp_money = (int(simpledialog.askstring (title="Fruity Fruits Shop", prompt="Please Enter the money you have:")))

# check it out
print(Fore.LIGHTCYAN_EX+ Style.BRIGHT+"Hello!", user_inp, "Welcome to Fruity Fruits Shop!")
time.sleep(0.5)
print(Fore.BLUE+"You have an amount of", user_inp_money, "pesos.")

print(Fore.RED+ Style.BRIGHT+ "It is almost Christmas! We are so sorry to inform you that the only fruit we have left is "+ Fore.RESET+ "Apples.")
time.sleep(0.5)
order = input (Fore.GREEN+"Would you like to continue purchasing? (yes/no)")
if order == "yes":
    print(Fore.MAGENTA+"We highly appreciate your understanding!")
    total_purchase ()

if order == "no":
    print(Fore.LIGHTWHITE_EX+"We are sorry for the incovenience. Thank you for trying to order!")

verify_purchased ()
