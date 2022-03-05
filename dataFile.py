from encryptor import decrypt,encrypt
import re
from typing import Literal


def get(filename,sep='&& %&'):
    
    sep,sep2 = sep.split(' ')
    if sep == sep2: raise Exception('Separators have to be different, try to use defaults')

    get_dataRegex = re.compile(r'(.*)(:key:.*)?@@{(.*)}')

    filename = filename if filename.endswith('.txt') else filename+'.txt'
    with open(filename,'a'):pass #evitar notfilefound

    with open(filename,'r') as f:
        to_return = {}
        for ch in f.readlines():
            m = get_dataRegex.match(ch)
            if not m:continue
            key = 'aaaaaaaa' if not m.group(2) else m.group(2).split(':')[-1]
            to_return.update({decrypt(key,*m.group(1)):decrypt(key,**{a.split(sep)[0]:a.split(sep)[1] for a in m.group(3).split(sep2)})})
    
    return to_return





def write(filename,sep='&& %&',**data:Literal['user:{data as a dict}((for add data to a user use:update))']):
    
    sep,sep2 = sep.split(' ')
    if sep == sep2: raise Exception('Separators have to be different, try to use defaults')

    filename = filename if filename.endswith('.txt') else filename+'.txt'
    with open(filename,'a') as f:
        for dk,da in data.items():
            b= '' if not 'key' in da.keys() else f':key:{da["key"]}'
        
            f.write('%s%s@@{%s}\n'%(dk,b,sep2.join([sep.join((dak,daa)) for dak,daa in da.items() if dak != 'key'])))



write('data',**{'hugo':{'password':'1234','dia':'12 febrero'}})