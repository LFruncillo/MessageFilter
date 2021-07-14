words = ['Pog', 'Chad']

username = input('Username:')
text = input('Message:')

for word in words:
    if word in text:
        print('Uh oh, bad word!')
        f = open(r"C:\Users\LukeF\Documents\GitHub\rps\message.txt", "a")
        f.write(text + '*bad word detected :O*, ')
        f.close