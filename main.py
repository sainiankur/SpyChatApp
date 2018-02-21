from spy_detail import spy,friends
from spy_detail import Spy, ChatMessage,Spy_friend
from steganography.steganography import Steganography    # import steganography which is used to send encrypted message to the friend
from datetime import datetime
from termcolor import colored
import csv

print "hi.."
print "Welcome to the SpyChat"


def load_friends():

    with open('friend.csv', 'rU') as friends_data:
        reader = list(csv.reader(friends_data, dialect='excel'))
        for row in reader[1:]:
            if row:
                name = row[0]
                age = (row[1])
                rating = (row[2])
                spy = Spy(name, age, rating)
                friends.append(spy)
#==========================================================================================================================================================================

def Chatload_friends():
    with open('Chats.csv', 'rU') as chats_data:
        reader = list(csv.reader(chats_data, dialect='excel'))
        for row in reader[1:]:
            if row:
                sender = row[0]
                message_sent_to= row[1]
                text = row[3]
                time = row[4]
                sent_by_me= row[4]
                chatlist = [sender,message_sent_to,text,time,sent_by_me]
#===========================================================================================================================================================================
STATUS_MESSGAES = ['available', 'sleeping', 'playing']
# creating a friends list
load_friends()
Chatload_friends()


def add_status(current_status_message):  # Function created add_status

    if current_status_message != None:
        print "your current status message is " + current_status_message
    else:
        print "you don't have any status message currently"

    status = raw_input("Do you want to select from old status? Y or N: ")
    if len(status) >= 1:
        if status.upper() == 'Y':
            serial_no = 1
            for old_status in STATUS_MESSGAES:
                print str(serial_no) + old_status
                serial_no = serial_no + 1
            user_selection = input(
                "which one you want to select: ")  # we are taking the input from user to select the old status
            if len(STATUS_MESSGAES) >= user_selection:
                new_status = STATUS_MESSGAES[user_selection - 1]
            else:
                print "invalid seletion"
            return new_status  # returning new_status if user want to update the old status

        elif status.upper() == 'N':
            new_status = raw_input("enter your new status")
            if len(new_status) > 1:
                STATUS_MESSGAES.append(new_status)
            else:
                print "please enter something atleast"
            return new_status  # returning new_status if user doesn't want to update old status

        else:
            print "invalid entry"
    else:
        set_status = "No status"
        return set_status

#=======================================================================================================================================================================

def add_friend():  # declaration of add_friend function which is used to add friend
    new_friend = {
        'name': '',
        'salutation': "",
        'age': 0,
        'ratings': 0.0,
        'online': True,
        'chats': []

    }
    valid_name = True
    valid_salutation = True
    while valid_name:
        new_friend['name'] = raw_input("what is the name of friend ?:  ")
        if len(new_friend['name']) >= 3:
            while valid_salutation:
                new_friend['salutation'] = raw_input("what we call your frnd : ")
                if len(new_friend['salutation']) >= 2:
                    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
                    valid_name = False
                    valid_salutation = False
                else:
                    print 'invalid salutaion'
        else:
            print "please enter valid name"
    valid_age = True
    while valid_age:
        new_friend['age'] = raw_input("Age of frnd")
        if len(new_friend['age']) > 0:
            valid_age = False
        else:
            print 'invalid age'
    valid_rating = True
    while valid_rating:
        new_friend['rating'] = raw_input("Rating of  a frnd")
        if len(new_friend['rating']) > 0:
            valid_rating = False
        else:
            print 'invalid ratings'
        new_friend['online'] = True
        if len(new_friend['name']) >= 3 and 55 >= int(new_friend['age']) >= 12 and new_friend['rating'] >= spy.rating:                                                                        # We are givig a certain conditon to add a friend
            friends.append(new_friend['name'])
            with open('friend.csv', 'a') as friends_data:
                writer = csv.writer(friends_data)
                writer.writerow([new_friend['name'], new_friend['rating'], new_friend['age'], new_friend['online']])
        else:
            print "friend cannot be added "
    return len(friends)

#=================================================================================================================================================================================

def select_a_friend():                                                                                       # We are declaring a functon select_a_friend which is used to select a friend to send a message
    serial_no = 1
    for frnd in friends:
        print  str(serial_no) + " " + frnd.name
        serial_no = serial_no + 1
    user_selected_frnd = input("select your frnd: ")
    user_index = user_selected_frnd - 1
    return user_index                                                                                         # we are returning a user_index above declare function which is used to select a friend to send a message

#======================================================================================================================================================================================

def send_message():  # declare a function send_message used to send a Encrypted message to friend using steagnography
    user_frnd_index = select_a_friend()
    original_image = raw_input("what is the name of your image? ")
    text = raw_input("what is your secret message? ")
    output_path = 'output.jpg'
    Steganography.encode(original_image, output_path, text)
    print "your secret message is ready! "
    new_chat = {
        "sender": spy.name,
        "message_sent_to": friends[user_frnd_index].name,
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }
    friends[user_frnd_index].chats.append(new_chat)
    with open('chats.csv', 'a') as chats_data:
        writer = csv.writer(chats_data)
        writer.writerow([new_chat['sender'], new_chat['message_sent_to'], new_chat['message'], new_chat['time'], new_chat['sent_by_me']])

#===========================================================================================================================================================================================


def read_message():                                                                  # declare a function read_message to read a encypted message send by the friend
    sender = select_a_friend()
    output_path = raw_input(colored("what is the name of the file u want to decode? ","red"))
    secret_text = Steganography.decode(output_path)
    print colored("This is the secret message send by your friend" + " " + secret_text,"red")
    new_text =(secret_text.upper()).split()
    if 'SOS' in new_text or 'ALERT' in new_text or 'HELP' in new_text:
        print colored("I am fine,we will meet Tommorow","blue")

#===========================================================================================================================================================================================
def ReadChatload_friends(choice):
    name_friend = friends[choice].name
    with open('Chats.csv', 'rU') as chats_data:
        reader = list(csv.reader(chats_data, dialect='excel'))
        check = False
        for row in reader[1:]:
            if row:
                    if (row[1]==name_friend):
                        check =True
                        print  colored(row[2],"red")
                        print  colored(row[3],"blue")
                    elif len(row[1]==name_friend)>0:
                        print "no chat"







#=============================================================================================================================================================================================
def start_spyChat(spy_name, spy_age, spy_rating):  # function define start_spyChat
    current_status_message = None
    show_menu = True
    while show_menu:  # used while loop for taking input from the user several time whithout ending process
        spy_menu_choice = input("""what do you want to do:
         1: Add a status update
         2: Add a new friend
         3. Send a message
         4. Read a message
         5. Show chat messages history
         0: Exit""")

        if (spy_menu_choice == 1):
            current_status_message = add_status(current_status_message)  # function call add_status and save it into the current status
            if len(current_status_message) >= 1:
                if current_status_message == 'No status':
                    print "you didn't select status correctly"
                else:
                    print "your status has been updated to" + current_status_message
            else:
                print "you didn't select the status correctly"
        elif (spy_menu_choice == 2):
            no_of_frnds = add_friend()  # function call add_friend
            print "you have " + str(no_of_frnds) + " friend"
        elif (spy_menu_choice == 3):
            send_message()  # function call send_message
        elif (spy_menu_choice == 4):
            read_message()  # function call read_message
        elif (spy_menu_choice == 5):
            print "select a friend whom you want to see the chat"
            choice = select_a_friend()
            ReadChatload_friends(choice)
        elif (spy_menu_choice == 0):
            print 'you are log out'
            show_menu = False
        else:
            print 'wroung choice'

#=============================================================================================================================================================================================

spy_exist = raw_input("Are you existing spy? Y or N ")  # we are asking user that he is existing user or not

if (spy_exist.upper() == 'Y'):
    print 'we have already your details'
    start_spyChat(spy.name, spy.age, spy.rating)  # function call start_spyChat

#===============================================================================================================================================================================================

elif (spy_exist.upper() == 'N'):

    spy.name = raw_input("Enter your name ")
    if len(spy.name) >= 3:
        print "welcome" + spy.name + ", i like to know about you."
        spy.salutation = raw_input("what should we call you(Mr. or Ms.)? ")
        if (spy.salutation) > 0:
            spy.name = spy.salutation + " " + spy.name
            print "Alright" + spy.name + ", i like to know more about you.."
            spy.ratings = input("please enter your ratings ")
            if (spy.ratings) >= 5.0:
                print 'Expert spy'
            elif (spy.ratings) <= 4.0:
                print('good spy')
            elif (spy.ratings) <= 3.0:
                print('bad spy')
            else:
                print('wroung entry')
            spy.age = input("Enter your age ")
            if spy.age > 20 and spy.age < 50:
                print "you are eligible to be spy"
            else:
                print "you are not eligible for spy"
            print "spy name is %s and spy age is %d and rating is %.2f " % (spy.name, spy.age, spy.ratings)
        else:
            print "not valid"
    else:
        print "enter a 3 character name"
else:
    print "invalid"

#=============================================================================================================================================