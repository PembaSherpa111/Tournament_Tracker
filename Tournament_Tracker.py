import os.path, csv
#Start Up
print('welcome to Tournament Tracker')
print('=============================')
participant_info = {} #declaring empty dictionary 

Tournament_name = input('Enter the name of the tournament: ')
if os.path.isfile(f'{Tournament_name}.csv'): #checking if the tournament already exists
    csvfile = open(f'{Tournament_name}.csv')
    for row in csvfile:
        row = row.strip('\n')
        (key,value) = row.split(',')
        key=int(key) #we need our key to be integer
        participant_info[key] = value
    num_of_participants = len(participant_info)
    print(f'\nThere are {num_of_participants} participant slots ready for sign ups.')
else:
    num_of_participants = int(input('Enter the number of participants: '))
    print(f'There are {num_of_participants} participant slots ready for sign ups.')
    for i in range(num_of_participants): #populating dictionary
        participant_info[i+1] = 'Empty'

#Main Menu
def main_menu():
    print('\nParticipant Menu')
    print('================')
    print('1. Sign Up \n2. Cancel Sign Up \n3. View Participants \n4. Save Changes \n5. Exit')

#Sign Up
def sign_up():
    print('\nParticipant Sign Up')
    print('===================')
    participant_name = input('Participant Name: ')
    starting_slot = int(input('Desired starting slot: '))
    success = False
    while success == False:
        if participant_info[starting_slot] == 'Empty':
            participant_info.update({starting_slot:participant_name})
            print('\nSuccess:')
            print(f'{participant_name} is signed up in starting slot #{starting_slot}')
            success = True
        else:
            print('\nError:')
            print(f'Slot #{starting_slot} is filled. Please try again')
            starting_slot = input('\nDesired starting slot: ')

#Cancel Sign Up
def cancel_sign_up():
    print('\nParticipant Cancellation')
    print('===================')
    starting_slot = int(input('Starting slot #: '))
    participant_name = input('Participant Name: ')
    success = False
    while success == False:
        if participant_info[starting_slot].lower() == participant_name.lower():
            participant_info.update({starting_slot:'Empty'})
            print('\nSuccess:')
            print(f'{participant_name} has been canclled from starting slot #{starting_slot}')
            success = True
        else:
            print('\nError:')
            print(f'{participant_name} is not in that starting slot.')
            starting_slot = input('\nStarting slot #: ')
            participant_name = input('Participant Name: ')

#View Participants
def view_participants():
    print('\nView Participants')
    print('=================')
    starting_slot = int(input('Starting slot #: '))
    print('\nStarting Slot: Participant')
    if starting_slot < 6:
        for i in range(1,(starting_slot+6)):
            print(f'{i}: {participant_info[i]}')
    else:
        for i in range((starting_slot-5),(starting_slot+6)):
            print(f'{i}: {participant_info[i]}')

#Save Changes
def save_changes():
    print('\nSave Changes')
    print('=============')
    save = input('Save your changes to CSV? [y/n] : ')
    while save.lower() not in {'y','n'}:
        save = input('Save your changes to CSV? [y/n] : ')
    if save.lower() == 'y':
        with open(f'{Tournament_name}.csv', 'w', newline='') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in participant_info.items():
                writer.writerow([key, value])

#Exit
def exit():
    print('\nExit')
    print('=====')
    print('Any unsaved changes will be lost.')
    leave = input('Are you sure you want to exit? [y/n] : ')
    while leave.lower() not in {'y','n'}:
        leave = input('Are you sure you want to exit? [y/n] : ')
    if leave.lower() == 'y':
        print('\nGoodbye!')
        stop = True
        return(stop)
    else:
        stop = False
        return(stop)

#Process
stop = False

while stop == False:
    #print(participant_info)
    main_menu()

    menu = input('\nWhat option would you like to select from Participant Menu: ')
    while menu.lower() not in {'1','2','3','4','5','sign up','cancel sign up','view participants','save changes','exit'}:
        print(f'{menu} is not an available option.')
        menu = input('\nPlease enter an available option from Participants Menu: ')

    if (menu == '1') or (menu.lower() == 'sign up'):    
        sign_up()
    elif (menu == '2') or (menu.lower() == 'cancel sign up'):
        cancel_sign_up()
    elif (menu == '3') or (menu.lower() == 'view participants'):
        view_participants()
    elif (menu == '4') or (menu.lower() == 'save changes'):
        save_changes()
    elif (menu == '5') or (menu.lower() == 'exit'):
        stop = exit()