                                                #SECRET
default_header=['ODA0MTgwMDA2NjExNDUxOTQ1.YBImMw.BVRwcNVYd9eLNl0y8JMRClCPazQ']
channel_list=['482467118860992522','798778169888210944','533062470043172878','244238578400362498']

                    #Imports
import requests
channel_id=None
                            #Getting User_Key and create token format
def get_key(_secret_=None):
    if _secret_==None:
        _secret_=input("Enter Your Access token:\t")
        _secret_ = {
        f'authorization' : _secret_
        }
        return _secret_
    elif _secret_.upper()=='ZERO':
        _secret_=default_header[0]
        _secret_ = {
        f'authorization' : _secret_
        }
        return _secret_
    else:
        _secret_ = {
        f'authorization' : _secret_
        }
        return _secret_
                            # Get Messages from a set Channel
def get_messages(__token__,channel_id=None):
    global message_list
    message_list=[]
    if channel_id is None:
        cpointer=input("Enter The Channel ID you'd like to access: \t")
    elif channel_id.upper()=='POKEMON':
        cpointer=channel_list[0]
    elif channel_id.upper()=='NEUROSIS':
        cpointer=channel_list[1]
    elif channel_id.upper()=='PRINCIPALS':
        cpointer=channel_list[2]
    elif channel_id.upper()=='HANGOUT':
        cpointer=channel_list[3]
        print("-------------------------------------------- \n\n")
    else:
        cpointer=channel_id
    response= requests.get(f'https://discord.com/api/v8/channels/'+cpointer+'/messages',
    headers=__token__)
    response_json=reversed(response.json())
    for msg in response_json:
        userid = msg["id"]
        author=msg["author"]
        username=author["username"]
        content = msg["content"]
        message_list.append(f'{username} :   {content}')
    return message_list
def post_message(__token__=None,__destination=None,__msg=None): #Posts message
    if __token__ is None:
        __token__=input("\nEnter Access Token:")
    if __destination is None:
        __destination=input("\nEnter Channel ID to Post In: \t")
    if __msg is None:
        __msg=input("\nEnter you're Message Below: \n")
        payload={
        'content' : __msg
        }
    elif __msg is not None:
        payload={
        'content' : __msg
        }
    requests.post(f'https://discord.com/api/v8/channels/'+__destination+'/messages', data=payload, headers=__token__)



