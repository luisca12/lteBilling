import os

def greetingString():
        os.system("CLS")
        print('  -------------------------------------------------------------- ')
        print(f"     Welcome to the automated create SW Core Template Script ")
        print('  -------------------------------------------------------------- ')

def menuString():
        print('  -------------------------------------------------------------- ')
        print('\t\t    Menu - Please choose an option')
        print('\t\t     Only numbers are accepted')
        print('  -------------------------------------------------------------- ')
        print('  >\t\t\t 1. East Side - Sites\t\t       <')   
        print('  >\t\t\t 3. Exit\t\t\t       <')
        print('  -------------------------------------------------------------- \n')


def inputErrorString():
        os.system("CLS")
        print('  ------------------------------------------------- ')  
        print('>      INPUT ERROR: Only numbers are allowed       <')
        print('  ------------------------------------------------- ')

# greetingString()
# menuString("2160 Gulf to Bay Blvd Clearwater, FL 33765")
# inputErrorString()