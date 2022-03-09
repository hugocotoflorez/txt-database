import re
from typing import Literal
import string
import random

if __name__ == '__main__':#importable modules
    print('\nUSE __ENCRYPTOR LIKE:\n\tfrom __encryptor import __encrypt,__decrypt\n\t__encrypt(String, key) -> __encrypted string \
    \n\tdecrypt(__Encrypted String, key) -> string\n\nKey:alphanumeric string, lenght 8.\n')
else:
    ni = string.ascii_letters+string.digits+'._'
    sep,sep2 = '&&','%&'


def __get_m(key):
    if len(key)>8:key=key[:8]
    while not len(key) == 8:
        key+='0'

    m = (1
        +ni.index(key[0])
        -(ni.index(key[1]) if ni.index(key[1]) < ni.index(key[0]) else 0)
        *((ni.index(key[2])*10+ni.index(key[3])) if ni.index(key[4])%3 else 0)
        +(ni.index(key[5])*10+ni.index(key[6])*2)**ni.index(key[7])
        +sum([ni.index(a) for a in key[::2]])
    )
    return m%len(ni) if m%len(ni) else 1


def __encrypt(key:Literal['len-8 alphanum str'],*text:Literal['Text string'],**dict_text:Literal['Text interable'])->Literal['__Encrypted string']:

    m = __get_m(key=key)

    if text: return "".join([l if not l in ni else ni[(ni.index(l)+x*(x+1)*(2*x+1)//6+m)%len(ni)] for x,l in enumerate(text)])

    return {"".join([l if not l in ni else ni[(ni.index(l)+x*(x+1)*(2*x+1)//6+m)%len(ni)] for x,l in enumerate(a)])
            :
            "".join([l if not l in ni else ni[(ni.index(l)+x*(x+1)*(2*x+1)//6+m)%len(ni)] for x,l in enumerate(b)]) for a,b in dict_text.items()} 


def __decrypt(key:Literal['len-8 alphanum str'],*text:Literal['Text string'],**dict_text:Literal['Text interable'])->Literal['des__encrypted string']:

    #create special movement
    m = __get_m(key=key)
    #returns text string
    if text: return "".join([l if not l in ni else ni[(ni.index(l)-x*(x+1)*(2*x+1)//6-m)%len(ni)] for x,l in enumerate(text)])
    #returns dict
    return {"".join([l if not l in ni else ni[(ni.index(l)-x*(x+1)*(2*x+1)//6-m)%len(ni)] for x,l in enumerate(a)])
            :
            "".join([l if not l in ni else ni[(ni.index(l)-x*(x+1)*(2*x+1)//6-m)%len(ni)] for x,l in enumerate(b)]) for a,b in dict_text.items()} 


def __randomkey():
    return ''.join([random.choice(ni) for a in range(8)])


def get_users(filename)->list:#get users list
    filename = filename if filename.endswith('.txt') else filename+'.txt'
    with open(filename,'r') as f:
        users = list()
        usersRegex = re.compile(r'(.*)!!(.*)@@')#group1
        for ch in f.readlines():
            c = usersRegex.match(ch)
            if not c:continue
            key = c.group(2)
            users.append(__decrypt(key,*c.group(1)))
    return users


def get(filename):#return all data as a dict

    get_dataRegex = re.compile(r'(.*)!!(.*)@@{(.*)}')
    filename = filename if filename.endswith('.txt') else filename+'.txt'
    with open(filename,'a'):pass #evitar notfilefound
    with open(filename,'r') as f:
        to_return = {}
        for ch in f.readlines():
            m = get_dataRegex.match(ch)
            if not m:continue
            key = m.group(2)
            to_return.update({__decrypt(key,*m.group(1)):__decrypt(key,**{a.split(sep)[0]:a.split(sep)[1] for a in m.group(3).split(sep2)})})
    return to_return



def write(filename,**data:Literal['user:{data as a dict}((for add data to a user use: update))']):#write, just to create database from nothing

    filename = filename if filename.endswith('.txt') else filename+'.txt'
    with open(filename,'a'):pass #evitar notfilefound
    users = get_users(filename)           
    with open(filename,'a') as f:
        for dk,da in data.items():
            if not dk in users:
                key = da.get('key',__randomkey())
                b=f'!!{key}'
                da=__encrypt(key,**da)
                f.write('%s%s@@{%s}\n'%(__encrypt(key,*dk),b,sep2.join([sep.join((dak,daa)) for dak,daa in da.items() if dak != 'key'])))
            else:
                update(filename,dk,**da)


def update(filename,keyword:Literal['username'],**args:dict):#write but for an existing user
    
    get_dataRegex = re.compile(r'(.*)!!(.*)@@{(.*)}')
    filename = filename if filename.endswith('.txt') else filename+'.txt'
    with open(filename,'r') as f:
        lineas = list()
        for ch in f.readlines():
            m = get_dataRegex.match(ch)
            if not m:continue
            key = m.group(2)
            d = {__decrypt(key,*m.group(1)):__decrypt(key,**{a.split(sep)[0]:a.split(sep)[1] for a in m.group(3).split(sep2)})}
            if keyword in d.keys():dt =d
            else: None if ch in lineas else lineas.append(ch) 
    for k,a in args.items():
        dt[keyword].update({k:a})
    with open(filename,'w') as f:
        f.writelines(lineas)
        for dk,da in dt.items():
            key = da.get('key',__randomkey())
            b=f'!!{key}'
            da=__encrypt(key,**da)
            f.write('%s%s@@{%s}\n'%(__encrypt(key,*dk),b,sep2.join([sep.join((dak,daa)) for dak,daa in da.items() if dak != 'key'])))

        
def add(filename,user,**args:dict):#add a new user 
    filename = filename if filename.endswith('.txt') else filename+'.txt'
    if user in get_users(filename):print('User exists yet');return
    with open(filename,'a') as f:
        key = args.get('key',__randomkey())
        b=f'!!{key}'
        args=__encrypt(key,**args)
        f.write('%s%s@@{%s}\n'%(__encrypt(key,*user),b,sep2.join([sep.join((dak,daa)) for dak,daa in args.items() if dak != 'key'])))
            
def delete_user(filename,user):#delete user 
    get_dataRegex = re.compile(r'(.*)!!(.*)@@{(.*)}')
    filename = filename if filename.endswith('.txt') else filename+'.txt'
    with open(filename,'r') as f:
        lineas = list()
        for ch in f.readlines():
            m = get_dataRegex.match(ch)
            if not m:continue
            key = m.group(2)
            d = {__decrypt(key,*m.group(1)):__decrypt(key,**{a.split(sep)[0]:a.split(sep)[1] for a in m.group(3).split(sep2)})}
            if user in d.keys():pass
            else: None if ch in lineas else lineas.append(ch) 
    with open(filename,'w') as f:f.writelines(lineas)


def delete_data(filename,user,*keys):#delete some data from user keys
    
    get_dataRegex = re.compile(r'(.*)!!(.*)@@{(.*)}')
    filename = filename if filename.endswith('.txt') else filename+'.txt'
    with open(filename,'r') as f:
        lineas = list()
        for ch in f.readlines():
            m = get_dataRegex.match(ch)
            if not m:continue
            key = m.group(2)
            d = {__decrypt(key,*m.group(1)):__decrypt(key,**{a.split(sep)[0]:a.split(sep)[1] for a in m.group(3).split(sep2)})}
            if user in d.keys():dt =d 
            else: None if ch in lineas else lineas.append(ch) 
    for k in keys:
        if k in dt[user].keys():
            del dt[user][k]
    with open(filename,'w') as f:
        f.writelines(lineas)
        for dk,da in dt.items():
            key = da.get('key',__randomkey())
            b=f'!!{key}'
            da=__encrypt(key,**da)
            f.write('%s%s@@{%s}\n'%(__encrypt(key,*dk),b,sep2.join([sep.join((dak,daa)) for dak,daa in da.items() if dak != 'key'])))


def reconfig(filename,toDo:Literal['change all keys']=None)->None:
    write(filename,**get(filename))

