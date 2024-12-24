'''
THIS IS A PYTHON RECONSTRUCTION OF A PROGRAM
I ORIGINALLY WROTE IN JAVA
'''
# TODO 1: Make while loop for moviePicker so the system asks for a movie over and over until movie is selected
# TODO 1a: Curently moviePicker just prints "Invalid Selection" and ends the program

# TODO 2: Create userAuth object and add Admin/Customer types to it
# TODO 3: Allow admin to edit and maybe add movies/prices
# TODO 4: If movieTitle is an invalid selection reset ticketPice/ticketsPurchased to zero
companyName = 'Monarchy Cinema'

firstName = input('Enter First Name: ')  # user inputs first and last name
lastName = input('Enter Last Name: ')
username = firstName.lower() + lastName.lower()  # names concatinate into username

# displays movie selections to user
print('[1] Coraline\n[2] Pacific Rim\n[3] Breezed')
print('[4] The Crow\n[5] Fantastic Mr. Fox\n[6] Isle of Dogs\n[7] Who\'s your Daddy')

movie = int(input('Select movie: '))  # gets int from user to choose movie
moviePick = ''
movieTime = ''
match movie:  # match statement to choose movie
    case 1:
        moviePick = 'Coraline'
    case 2:
        moviePick = 'Pacific Rim'
    case 3:
        moviePick = 'Breezed'
    case 4:
        moviePick = 'The Crow'
    case 5:
        moviePick = 'Fantastic Mr. Fox'
    case 6:
        moviePick = 'Isle of Dogs'
    case 7:
        moviePick = 'Who\'s your Daddy'
    case _:
        print('[ERROR] Invalid Selection')  # displays error if selection is invaild

print('[1]12pm\n[2]1:30pm\n[3]3pm\n[4]4:30pm\n[5]6pm\n[6]7:30pm\n[7]9pm')  # displays viewing times for movies
time = int(input('Select viewing time: '))  # gets int from user to pick viewing time
match time:  # match statement to choose viewing time
        case 1:
            movieTime = '12pm'
        case 2:
            movieTime = '1:30pm'
        case 3:
            movieTime = '3pm'
        case 4:
            movieTime = '4:30pm'
        case 5:
            movieTime = '6pm'
        case 6:
            movieTime = '7:30pm'
        case 7:
            movieTime = '9pm'
        case _:
            print('[ERROR] Invalid Selection')  # displays error if selection is invaild

perTicket = 11  # sets cost per ticket
ticketCount = int(input('How many tickets would you like to purchase: '))  # gets int from user to pick how many tickets to purchase
cost = (ticketCount * perTicket) * 1.07  # cost of tickets
totalCost = "{:.2f}".format(cost)  # format ticket cost to currency form

# final info screen
print("_______________[INFO]________________")
print('\nUsername: [', username, ']')
print('Movie: [', moviePick, ']')
print('Movie Time: [', movieTime, ']')
print('Price per ticket: [', perTicket, ']')
print('Total price of [', ticketCount, '] tickets: [', totalCost, ']')
print('_____________________________________')

# thank user for using the system
print("\nThank you for choosing " + companyName + " for your movie going experience.\nEnjoy your movie!\n")
print(username, moviePick, movieTime, totalCost)