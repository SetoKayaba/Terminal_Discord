"""
READ ME PLEASE
So first of all, why in gods name are you using actual requests to Discords API
Check out my github repos for how to selfbot using the Discord.py wrapper
Link: https://www.github.com/brni-dev
!! IMPORTANT !! do a pip freeze and include a requirements.txt for your thing
"""

from os import getenv
from dotenv import load_dotenv

# loads .env file and gets the TOKEN variable from the .env file
load_dotenv()
default_header = list(getenv('TOKEN'))

# idk wtf this channel_list is but each user has a different channel list so gl
channel_list = [
    '482467118860992522', 
    '798778169888210944',
    '533062470043172878',
    '244238578400362498'
]

# Imports
import requests
channel_id=None

def get_key(_secret_=None):
    """
    Getting User_Key and create token format
    Usage: specify usage here
    """
    
    # fixed alotta shit here, also you should really learn what global scopes and local scopes are
    if _secret_ == None:
        _secret_ = input("Enter Your Access token:\t")
        return {'authorization': _secret_}
        # fixed indentation, also you cannot specify the variable itself as a variable
     
    elif _secret_.lower() == 'env': return {'authorization': default_header[0]}
    # why were u using a f string here, btw fixed indentation and why do you want this token as a list?
    
    else: return {'authorization' : _secret_} # fixed indentation

    
def get_messages(_token, channel_id=None): # declaring shit with __example__ means you're declaring a special variable so imma change that
    """
    Get Messages from a set Channel
    Usage: declare usage here
    """
    
    global message_list
    message_list=[]
    
    # oh jesus fucking christ, yandere dev 2.0 incoming
    if channel_id==None:cpointer=input("Enter The Channel ID you'd like to access: \t")
    elif channel_id.upper()=='POKEMON':cpointer=channel_list[0]
    elif channel_id.upper()=='NEUROSIS':cpointer=channel_list[1]
    elif channel_id.upper()=='PRINCIPALS':cpointer=channel_list[2]
    elif channel_id.upper()=='HANGOUT':cpointer=channel_list[3]
    print("-------------------------------------------- \n\n")
    else:cpointer=channel_id
  
    response = requests.get(f'https://discord.com/api/v8/channels/{cpointer}/messages', headers = _token) # YOURE USING A F STRING HERE, SO WHY ARE YOU DOING IT WITH PLUSES
    response_json=reversed(response.json())
    
    for msg in response_json:
        # made this more readable
        userid    = msg["id"]
        author    = msg["author"]
        username  = author["username"]
        content   = msg["content"]
        message_list.append(f'{username} :   {content}')
    return message_list
  
def post_message(_token=None, _destination=None, _msg=None):
    """
    Posts message
    Usage: declare usage here
    """
    
    if _token == None: _token = input("\nEnter Access Token:")
    if _destination == None: _destination = input("\nEnter Channel ID to Post In: \t")
        
    if _msg == None:
        _msg = input("\nEnter you're Message Below: \n")
        payload = {'content' : _msg} # fixed indentation
        
    elif _msg != None: payload = {'content' : __msg} # fixed indentation for the 923125427648723613th time yes
        
    requests.post(f'https://discord.com/api/v8/channels/{_destination}/messages', data = payload, headers = _token) # you just need to leave ONE empty space for parsers, also again using f string with pluses makes no sense
