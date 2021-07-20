words = ['Pog', 'Chad']
regusername = 'WideLuke'
regpassword = '12345'

print('Login')
logusername = input('Username:')
logpassword = input('Password:')

if logusername == regusername and logpassword == regpassword:
    choice = input(logusername + ':')

if choice == 'Send message':
    message = input(logusername + ': ')
    for word in words:
        if word in message:
            print('Uh oh, bad word!')
            f = open(r"C:\Users\LukeF\Documents\GitHub\MessageFilter\message.txt", "a")
            f.write(logusername + ': ' + message + ', ')
            f.close

if choice == 'Check messages':
    with open(r"C:\Users\LukeF\Documents\GitHub\MessageFilter\message.txt", "r") as file:
        contents = file.read()
        for word in words:
            if word in contents:
                print(word)
            else:
                print('No words found')