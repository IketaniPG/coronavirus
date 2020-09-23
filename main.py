#colorama

from colorama import init
from colorama import Fore as colorized
from colorama import Back as background

#covid

from covid import Covid

#search
from Functions import functions

#sleep
from time import sleep

init(autoreset=True) #init colorama

covid = Covid()
countries_list = []

returnvar = True
def start():
    print('Welcome to', colorized.RED + 'COVID-19',  'Data-Script!\nMake a choice:\n')
    print('[', colorized.CYAN + '1', '] Search a country data.')
    print('[', colorized.CYAN + '2', '] Show world data.')
    print('[', colorized.CYAN + '3', '] Close application.')

    choice = int(input('\n> '))

    if choice == 1:
        print('\nYou', colorized.GREEN + 'selected', ': Search a country data.')
        print('You have this choices:\n')
        print('[', colorized.CYAN + '1', '] Show countries names and IDs.')
        print('[', colorized.CYAN + '2', '] Proceed to search page.')
        print('[', colorized.CYAN + '3', '] Return to main page.')

        choice_1 = int(input('\n> '))

        if choice_1 == 1:
            print('\nYou', colorized.GREEN + 'selected', ': Show countries names and IDs.')
            print('[', colorized.LIGHTBLUE_EX + 'COUNTRIES LIST', '] Access our countries list on: https://github.com/IketaniPG/coronavirus/\n')
            print('Coming back to main menu.\n')
            sleep(3)

        elif choice_1 == 2:
            print('\nYou', colorized.GREEN + 'selected', ': Proceed to search page.')
            name = str(input('Country name > '))

            searched = functions.search_country(name)
            
            if searched['active'] < 5000:
                status = 1
            elif searched['active'] > 5000:
                status = 2
            elif searched['active'] > 40000:
                status = 3

            confirmed = searched['confirmed']
            active = searched['active']
            deaths = searched['deaths']
            recovered = searched['recovered']

            print(f'Country: {name}')

            if status == 1:
                print('\nStatus: [', colorized.GREEN + 'ESTABILIZED', ']\n')
            elif status == 2:
                print('\nStatus: [', colorized.YELLOW + 'IN WARNING', ']\n')
            elif status == 3:
                print('\nStatus: [', colorized.RED + 'CRITICAL', ']\n')

            print(f'Data:\n\nConfirmed: {confirmed}\nActive: {active}\nDeaths: {deaths}\nRecovered: {recovered}\n')
            print(colorized.RED + 'Coming back' , 'to main menu.\n')
            sleep(3)
                    
        elif choice_1 == 3:
            returnvar = False

    elif choice == 2:
        print('\nYou', colorized.GREEN + 'selected', ': Show world data.')

        active = covid.get_total_active_cases()
        
        if active < 5000:
            status = 1
        elif active > 5000:
            status = 2
        elif active > 40000:
            status = 3

        confirmed = covid.get_total_confirmed_cases()
        deaths = covid.get_total_deaths()
        recovered = covid.get_total_recovered()

        print(f'World Informations')

        if status == 1:
            print('\nStatus: [', colorized.GREEN + 'ESTABILIZED', ']\n')
        elif status == 2:
            print('\nStatus: [', colorized.YELLOW + 'IN WARNING', ']\n')
        elif status == 3:
            print('\nStatus: [', colorized.RED + 'CRITICAL', ']\n')

        print(f'Data:\n\nConfirmed: {confirmed}\nActive: {active}\nDeaths: {deaths}\nRecovered: {recovered}\n')
        print(colorized.RED + 'Coming back' , 'to main menu.\n')
        sleep(3)

    elif choice == 3:
        print('\nYou choosed', colorized.RED + 'close', 'the application.')
        exit()
try:
    while returnvar:
        start()
except KeyboardInterrupt:
    print('\nYou choosed', colorized.RED + 'close', 'the application.')
    exit()
except ValueError:
    print('[', colorized.LIGHTRED_EX + 'ERROR', '] The specified input', colorized.RED + 'is not valid.', background.RED + 'If you are trying to search a country, see our country list in: https://github.com/IketaniPG/coronavirus/')
    start()
