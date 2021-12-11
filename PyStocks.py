# A Simple Stock exchange alike application built in Python.

import random
import sys
import os

# Main logic of the program written in Object Oriented Way
class Stocks:

    def _buyStock(self, n, sp, m):
        self.x = m
        self.x = self.x-(n*sp)
        print('Your Current Money: ', self.x)

    def _sellStock(self, n, sp, m):
        self.y = m
        self.y = self.y+(n*sp)
        print('Your Current Money: ', self.y)

    def _exit(self):
        ch = input('[*] Do you want to exit? [y/n] ')
        os.system('cls')
        if ch == 'y':
            sys.exit()


# Initializing our main class
St = Stocks()
stocks = 0
stock_price = 0
money = 1000

# Decorations
print('==============================================')
print('                 PYSTOCKS                     ')
print('----------------------------------------------')
print('                                 BY  DEBONMOY ')
print('==============================================')

usr = input('Hey there please tell us your name: ')
print('Your money: ', money)
usr_stocks = 0

print (f'Hello {usr} what would you like to do? ')

# Main infinite loop
while True:

    stocks = random.randint(0,50)
    stock_price = random.randint(0,100)

    print('\nNo. of stocks available in market: ', stocks)
    print('Current stock price: ', stock_price)
    print('No. of stocks owned: ', usr_stocks)
    print('Current Balance: ', money)
    print('1. Buy Stock(s)')
    print('2. Sell Stock(s)')
    print('3. Exit')
    ch = int(input('[*] Your choice: '))

#   Buy Stocks Option
    if ch==1:
        n = int(input('[*] Enter no. of stocks to buy: '))
        usr_stocks = usr_stocks+n
        St._buyStock(n,stock_price,money)
        money = St.x
        St._exit()

#   Sell Stocks Option
    if ch==2:
        n = int(input('[*] Enter the number of stocks to sell: '))
        usr_stocks = usr_stocks-n
        St._sellStock(n,stock_price,money)
        money = St.y
        St._exit()

#   Exit Option
    if ch==3:
        St._exit()
