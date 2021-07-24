# Blacklisted words.
words = ['Pog', 'Chad']

# Set user login details.
regusername = 'WideLuke'
regpassword = '12345'

# Login form.
print('Login')
logusername = input('Username:')
logpassword = input('Password:')

# Checks if user details are correct.
if logusername == regusername and logpassword == regpassword:
    choice = input(logusername + ':')

# Allows the user to send a message. If message contains a blacklisted word then the message gets stored in a txt file, else the message is ignored.
if choice == 'Send message':
    message = input(logusername + ': ')
    for word in words:
        if word in message:
            print('Uh oh, bad word!')
            f = open(r"C:\Users\LukeF\Documents\GitHub\MessageFilter\message.txt", "a")
            f.write(logusername + ': ' + message + ', ')
            f.close

# Prints words from messages that are blacklisted. 
if choice == 'Check messages':
    with open(r"C:\Users\LukeF\Documents\GitHub\MessageFilter\message.txt", "r") as file:
        contents = file.read()
        for word in words:
            if word in contents:
                print(word)
            else:
                print('No words found')