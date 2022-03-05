from typing import Literal
import string

if __name__ == '__main__':#importable modules
    print('\nUSE ENCRYPTOR LIKE:\n\tfrom encryptor import encrypt,decrypt\n\tencrypt(String, key) -> encrypted string \n\tdecrypt(Encrypted String, key) -> string\n\nKey:alphanumeric string, lenght 8.\n')
ni = string.ascii_letters+string.digits+'._'


def __get_m(key):
    #get mov
    #number interable access like ni.index('x')
    if len(key)>8:key=key[:8]
    while not len(key) == 8:
        key+='0'

    m = (
        0
        +ni.index(key[0])
        -(ni.index(key[1]) if ni.index(key[1]) < ni.index(key[0]) else 0)
        *(
            (ni.index(key[2])*10+ni.index(key[3])) if ni.index(key[4])%3 else 0)
        +(ni.index(key[5])*10+ni.index(key[6])*2)**ni.index(key[7])
        +sum([ni.index(a) for a in key[::2]])
    )
    m = m if m else 1

    return m


def encrypt(key:Literal['len-8 alphanum str'],*text:Literal['Text string'],**dict_text:Literal['Text interable'])->Literal['Encrypted string']:

    m = __get_m(key=key)

    if text: return "".join([l if not l in ni else ni[(ni.index(l)+x*(x+1)*(2*x+1)//6+m)%len(ni)] for x,l in enumerate(text)])

    return {"".join([l if not l in ni else ni[(ni.index(l)+x*(x+1)*(2*x+1)//6+m)%len(ni)] for x,l in enumerate(a)])
            :
            "".join([l if not l in ni else ni[(ni.index(l)+x*(x+1)*(2*x+1)//6+m)%len(ni)] for x,l in enumerate(b)]) for a,b in dict_text.items()} 


def decrypt(key:Literal['len-8 alphanum str'],*text:Literal['Text string'],**dict_text:Literal['Text interable'])->Literal['desencrypted string']:

    #create special movement
    m = __get_m(key=key)
    #returns text string
    if text: return "".join([l if not l in ni else ni[(ni.index(l)-x*(x+1)*(2*x+1)//6-m)%len(ni)] for x,l in enumerate(text)])
    #returns dict
    return {"".join([l if not l in ni else ni[(ni.index(l)-x*(x+1)*(2*x+1)//6-m)%len(ni)] for x,l in enumerate(a)])
            :
            "".join([l if not l in ni else ni[(ni.index(l)-x*(x+1)*(2*x+1)//6-m)%len(ni)] for x,l in enumerate(b)]) for a,b in dict_text.items()} 



    

