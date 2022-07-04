# Developed in Python 3.7.1
# Made by Israel Wokoh (Queen Mary, University of London)

class UNiDAYSDiscountChallenge:
    pricingRules = {'A': 8,
                    'B': 12,
                    'C': 4,
                    'D': 7,
                    'E': 5} # Called in CalculateTotalPrice()


    def __init__(s):
        s.basket = [] # Using a list to represent basket - could use string as that's iterable too.

    def AddToBasket(s, item): # _item_ is a string
        if all(elem in 'ABCDE' for elem in item): # Checks that every element of user input is valid
            for elem in item: # If the basket were a string, I'd just do s.basket += item
                s.basket.append(elem)
            # print(f'This is your basket: {"".join(sorted(s.basket))}') # Shows basket in linear form
            print('\nThis is your basket:', end = '')
            s.ShowBasket()

        else: # At least one invalid item
            print(f'{item} contains invalid item(s).')

    def ClearBasket(s): # EXTRA
        s.basket = [] # Reset basket
        print('Basket cleared.')

    def ShowBasket(s): # EXTRA
        print()
        for elem in 'ABCDE':
            if s.basket.count(elem) is not 0: # Prints items in basket
                print(f'{elem} × {s.basket.count(elem)}')

    def CalculateTotalPrice(s): # Calculate and return the overallTotal price
        overallTotal = 0 # Reset basket price

        for elem in 'ABCDE':
            itemCount = s.basket.count(elem)
            itemTotal = 0 # Subtotal allows user to see cost of each item in basket

            # Calculation method for each item
            if elem is 'A': # £8 each
                itemTotal += itemCount * s.pricingRules['A']

            elif elem is 'B': # £12/2 for £20
                itemTotal += (itemCount // 2) * 20\
                           + s.pricingRules['B'] * (itemCount % 2)

            elif elem is 'C': # £4/3 for £10
                itemTotal += (itemCount // 3) * 10\
                             + s.pricingRules['C'] * (itemCount % 3)

            elif elem is 'D': # Buy One, Get One Free
                itemTotal += ((itemCount // 2) + (itemCount % 2))\
                             * s.pricingRules['D']

            else: # 3 for 2
                itemTotal += (itemCount // 3) * (2 * s.pricingRules['E'])\
                           + (itemCount % 3) * s.pricingRules['E']

            # Showing individual item totals
            if itemCount != 0: # Doesn't show items that aren't in basket
                print(f'{elem} × {s.basket.count(elem)} → £{itemTotal}.00')
                overallTotal += itemTotal

        # Determines delivery charge
        if overallTotal >= 50 or overallTotal is 0:
            deliveryCharge = 0 # Free
        else:
            deliveryCharge = 7 # Costs £7
        print(f'Delivery Charge: £{deliveryCharge}.00') # Shows delivery charge
        print(f'Total Price: £{overallTotal + deliveryCharge}.00') # Total price shown in currency format

def Menu():
    user = UNiDAYSDiscountChallenge()

    while True:
        print()
        choice = input('Enter:\n(1) - Add item(s) to your basket\
                           \n(2) - Clear basket\
                           \n(3) - Show basket\
                           \n(4) - Get the total price of basket\
                           \nChoice: ')

        if choice not in ['1','2','3','4']:
            print('Invalid choice.\n')

        else:
            if choice is '1':
                user.AddToBasket(input('\nWhich items would you like to add?\
                \n(Enter A, B, C, D, E or any combination): ').upper().replace(' ', ''))

            elif choice is '2':
                user.ClearBasket()

            elif choice is '3':
                user.ShowBasket()

            else:
                user.CalculateTotalPrice()

if __name__ == '__main__':
    Menu()