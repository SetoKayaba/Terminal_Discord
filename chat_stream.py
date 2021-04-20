import threading
from DiscordZero import get_key, get_messages, post_message
from time import sleep

if __name__ == '__main__':
    login = get_key('env')
    test_channel = 798778169888210944
    all_messages = get_messages(login,test_channel)

class Chatbox:
    def update(login, location):
        """
        Update the list of messages every 3 seconds. This function will never return.
        Usage: specify usage here
        """
        while True:
            global all_messages
            nm = get_messages(login, location)
            
            # kill me
            try: new_messages = nm[nm.index(all_messages[-1]) + 1:]
            except: 'Return Value Does Not Exist anymore'
            # Would this return a Index error? If so specify it with `except IndexError: blahblahcode`
                
            all_messages += new_messages
            for message in new_messages:
                print(message)
            sleep(3)
            
    def send(key,send_location,message=None):
        if message is None:
            while True:
                message=input(">> ")
                post_message(key,send_location,message)
                sleep(5)

if __name__=='__main__':
    map(lambda message: print(message), all_messages) # instead of the for loop

    t1 = threading.Thread(target=Chatbox().update("Specify shit here"), args = (login, test_channel,)) # Chatbox is a class, not a object!!!!
    t2 = threading.Thread(target=Chatbox().send("Specify shit here"), args = (login,test_channel))
    operate = f'''
        {t1.start()}
        ----------------------------------------------------------------
        {t2.start()}
    '''
