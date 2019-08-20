#-------------------------------------------------------------------------------
# Project Title: Cryptocurrency converted and calculator
# Student Names: Zachary Merrill
# Assignment: Final Project main file
# Submission Date: 12-6-17
# Python Version: 3.43
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: https://coinmarketcap.com/all/views/all/
#-------------------------------------------------------------------------------
# Note: There are no errors within this code
#-------------------------------------------------------------------------------
# Pseudocode:
# Starts here
#-------------------------------------------------------------------------------
# Source Code:

def convert(pricePerUnit):
    '''
    Input: N/A
    Return: new list (conversions)
    '''
    conversions = [] #new list for conversions
    for i in range (0, len(pricePerUnit)): #for loop to loop through prices to calculate the conversion rate
        x = pricePerUnit[i] #creates a variable for calculations
        conversion = 1.00/x #calculations for conversion
        conversions.append(conversion) #adds each new conversion to the list
        
    return conversions #returns conversion

    
def addCurrency(names, pricePerUnit, supply, rank):
    '''
    Input: New Name, Price, Supply, and Rank
    Return: New Name, Price, Supply, and Rank at the end of each of the corresponding lists
    '''
    newName = input("Please Input the name of the CryptoCurrency: ") #Prompts User for inputs to add the new currency
    newPricePerUnit = float(input("Please input the price per unit of this CryptoCurrency: "))
    newSupply = int(input("Please input the supply of this CryptoCurrency: "))
    newRank = int(input("Please input the rank of this CryptoCurrency: "))
    names.append(newName) #adds all of the new inputs to their corresponding list
    pricePerUnit.append(newPricePerUnit)
    supply.append(newSupply)
    rank.append(newRank)

    return (names, pricePerUnit, supply, rank) #returns the updated lists


def viewAvailableCurrencies(names, pricePerUnit, supply, rank, conversions): 
    '''
    Input: N/A
    Return: Prints all of the formated currencies
    '''
    for i in range(0, len(names)): #loops based off the length of the names list
        print('Name: ', names[i],'\nPrice: ', pricePerUnit[i], '\nSupply: ', supply[i], '\nRank: ', rank[i],'\nConversion Rate: ', conversions[i], "\n") #prints all lists based off of their index
    

def removeCurrency(names, pricePerUnit, supply, rank):
    '''
    Input: remove name
    Return: new lists excluding one of the elements
    '''
    removeName = input("Please input the name of the CryptoCurrency you would like to remove: ") #prompts user for the name of the cryptocurrency they want to remove
    for i in range(0, len(names)): #loops based off the length of the names list
        if names[i] == removeName: #Compares romove name to names at an index
            del names[i] #deletes all of the values corresponding to the selected currency
            del pricePerUnit[i]
            del supply[i]
            del rank[i]
            break

    return (names, pricePerUnit, supply, rank) #returns updated list
            
    
def updateCurrency(names, pricePerUnit, supply, rank):
    '''
    Input: New names, pricePerUnit, supply, rank 
    Return: updated names, pricePerUnit, supply, rank
    '''
    updateName = input("Please enter the CryptoCurrency you would like to update: ") #prompts user for what they want to update
    for i in range(0, len(names)): #loops based off the length of the names list
        if names[i] == updateName: ##Compares update name to names at an index
            newName = input("Updated Name: ")
            names[i] = newName
            newPrice = float(input("Updated Price: "))
            pricePerUnit[i] = newPrice
            newSup = int(input("New Supply: "))
            supply[i] = newSup
            newRank = int(input("New Rank: "))
            rank[i] = newRank #updates the data within the list
            
          
    return (names, pricePerUnit, supply, rank) #returns updated list


def moneyToCurrency (names, conversions):
    '''
    Input: Money
    Return: Prints conversions
    '''
    money = float(input("Please Input how much movey you have in USD: ")) #prompts user for input of the money they want to invest in cryptocurrency
    moneyCon = [] #blank list for conversions
    print("***************************** \n What your money is worth?")
    for i in range(0, len(conversions)): #loops through a list based on the length of the conversions list
        x = money * conversions[i]
        moneyCon.append(x)
        print(names[i], "\n" , moneyCon[i],  "\n \n")


def main():
    '''
    Input: menu selection and all inputs from functions
    Return: outputs of functions / None
    '''
    names = ['Bitcoin', 'Ethereum', 'Bitcoin Cash', 'Ripple', 'IOTA', 'QTUM', 'Litecoin'] #default cryptocurrency data
    pricePerUnit = [13405.00, 427.15, 1450.84, 0.235933, 3.83, 12.41, 99.97]
    supply = [16724612, 96175068, 16841638, 38739145009, 2779530283, 73696328, 54163283]
    rank = [1, 2, 3, 5, 4, 21, 7]
    flag = False #flag
    while flag == False: #while loop using flag
        conversions = convert(pricePerUnit) #calls convert function
        print("CRYPTO-CURRENCY-CONVERTER \n *******MENU******* \n 1) View Available CryptoCurrency \n 2) Money to Crypto Currency \n 3) Edit \n 4) Exit ") #menu
        menu = int(input("Please select your menu option: ")) #prompts user for menu selection
        if menu == 1:
            viewAvailableCurrencies(names, pricePerUnit, supply, rank, conversions) #calls printing function
        elif menu == 2:
            moneyToCurrency (names, conversions) #calls money conversion function
        elif menu == 3:
            print("*******EDIT******* \n 1) Add Currency \n 2) Remove Currency \n 3) Update Currency \n 4) Return to Main Menu") #nested menu
            select = int(input("Please select your menu option: "))
            if select == 1:
                addCurrency(names, pricePerUnit, supply, rank) #calls add function
            elif select == 2:
                removeCurrency(names, pricePerUnit, supply, rank) #calls remove function
            elif select == 3:
                updateCurrency(names, pricePerUnit, supply, rank) #calls update function
            elif select == 4:
                print("Returning to Main Menu...")
            else:
                print("ERROR: INVALID INPUT - Returning to Main Menu...") #prints error message
        elif menu == 4:
            print("Exiting Program...")
            flag = True
        else:
           print("ERROR: INVALID INPUT")#prints error message
    quit() #exits program


main() #executes main function
