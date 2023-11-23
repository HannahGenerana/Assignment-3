from colorama import Fore, Back, Style, init #for text color 
init(convert=True) 
from pyfiglet import Figlet
f = Figlet(font='slant')
from tkinter import messagebox
from tkinter import*

def calculate_total_amount(quantity_apple, quantity_orange):
    apple_price = 20
    orange_price = 26
    total_amount = (apple_price * quantity_apple) + (orange_price * quantity_orange)
    return total_amount

def purchased():
    quantity_apple = int(input (Fore.LIGHTCYAN_EX+('How many apples would you like to purchase?')))
    quantity_orange = int(input (Fore.LIGHTCYAN_EX+('How many oranges would you like to purchase?')))

    total_purchase = calculate_total_amount(quantity_apple, quantity_orange)
    print (Fore.GREEN+f"\033[1mThe total amount you need to pay is {total_purchase} pesos\033[0m")

messagebox.askyesno(title='Fruity Fruits Shop', message='Would you like to place an order?')

print(Fore.LIGHTBLUE_EX+ f.renderText('Welcome to Fruity Fruits Shop where all fruits are freshly harvest!'))
print(Fore.LIGHTBLUE_EX+('Welcome! What would you like to order?')+Fore.RESET)
given_order = input ("Please enter your order:")

print(Fore.RED+("\033[1mWe are so sorry to inform you that the only fruits we have left are Apples and Oranges. Would you still like to place your order?\033[0m"))
continue_order = input ("yes/no:")
if continue_order == "yes":
    print(Fore.WHITE+("Thank you for understanding!"))
if continue_order == "no":
    print(Fore.BLACK+("Sorry for the incoveniece, we will restock in no time soon!"))

print(Fore.MAGENTA+("Here is our pricelist for our fruits"))
print(Fore.LIGHTRED_EX+("1 pc of apple = 20 pesos"))
print(Fore.LIGHTYELLOW_EX+("1 pc of orange = 25 pesos"))

purchased()

receipt_purchase = input ("Is that all your order? (yes/no)")
if receipt_purchase == "yes":
    messagebox.askquestion(title='Fruity Fruits Shop', message='Are you sure about your order?',)
    messagebox.askyesnocancel(title='Fruity Fruits Shop', message='Kindly click yes to place your order.',)
    messagebox.showinfo(title='Fruity Fruits Shop', message='Thank you for ordering!')

if receipt_purchase == "no":
    restart_purchase = input ("I'm sorry, you need to start over the order")
