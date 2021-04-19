from DiscordZero import get_key, get_messages, post_message
import threading
import time

if __name__=='__main__':
    login=get_key('Zero')
    test_channel='798778169888210944'
    all_messages=get_messages(login,test_channel)

class Chatbox:
    def update(login, location):
    # Update the list of messages every 3 seconds. This function will never return.
        while True:
            global all_messages
            new_messages = get_messages(login, location)
            try:
                new_messages = new_messages[new_messages.index(all_messages[-1])+1:]
            except:
                'Return Value Does Not Exist anymore'
            all_messages += new_messages
            for message in new_messages:
                print(message)
            time.sleep(3)
    def send(key,send_location,message=None):
        if message is None:
            while True:
                message=input(">> ")
                post_message(key,send_location,message)
                time.sleep(5)

if __name__=='__main__':
    for message in all_messages:
        print(message)
    t1= threading.Thread(target=Chatbox.update, args= (login, test_channel,))
    t2= threading.Thread(target=Chatbox.send, args=(login,test_channel))
    operate=f'''{t1.start()}
    {print('----------------------------------------------------------------')}
    {t2.start()}'''
