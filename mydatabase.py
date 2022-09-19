import database_manager as dbm
import time
from database_manager import clear

#set variables
datafile = 'data.txt'
data = dict()
users = list()

#set data
data = dbm.get(datafile)
#set users_list
users = dbm.get_users(datafile)

def check_UP(data,user,password):
    if data[user].get('password','')==password:
        return 1, 'Correct'
    else:
        return 0, 'Incorrect Password'


def login():
    clear()
    for timeout in range(100):
        #get user
        user = input('User: ')
        pas =1
        if not user in users: print('[!] Unfound user.\nDo you want to sign up? (Y/n): ',end='');pas = signup(user);
        if not pas:continue
        #get password
        for a in range(3):
            password = input('Password ("." to go back): ') if not pas or pas ==1 else pas
            if password == '.':break
            else:
                cup =  check_UP(data,user,password)
                if cup[0]:return(data[user],user)
                else:print('[!] ',cup[1],'. Remainig attempts: ',2-a,sep='')
        print('[!] Timeout: ',timeout,'s',sep='')
        time.sleep(timeout)


    else:
        while True:
            try:input('|$|~PERMABAN~|$|')
            except:pass


def signup(username):
    global users, data
    if input('') in ('y','Y','Yes','YES','yes'):
        print('Create a password for ',username,':',sep='',end='')
        pw = input()
        pw2 = input('Retype the password, please: ')
        if pw == pw2: 
            data.update({username:{'password':pw}})
            users.append(username)
            dbm.add(datafile,username,**{'password':pw})
            return pw
        else:print('[!] Passwords dont match. \nDo you want to retry? (Y/n): ',end='');return signup(username)
    else: return 0
        


def access(*args):
    global data
    udata,user = args
    print('Wellcome ',user,'!',sep='')
    while True:
        clear()
        i = input('.'*30+'''
    [1]: View data.
    [2]: Add/edit data.
    [3]: Delete data.
    [4]: Personal info.
    [5]: Delete user.
    [.]: Log out\n'''
    +'.'*30+'\n[>]: ')

        if not i in '12345.':print('Invalid entry. Please retry.');continue

        elif i == '1':
            clear()
            print('My data:\n'+'.'*30)
            print('\n'.join([f'{a}: {b}' for a,b in udata.items() if a!='password']))
            input('.'*30+'\nPress any key to return.')

        elif i == '2':
            clear()
            print('Add data:\n'+'.'*30)
            to_add = {}
            while True:
                key = input('Key ("." to return): ')
                if not key:print('invalid key');continue
                elif key == '.':break
                args = input('Args for {}: '.format(key))
                if not args:print('invalid args');continue
                to_add.update({key:args})
                data.update({key:args})
                udata.update({key:args})
                print('({}: {}) Successfully added'.format(key,args))
            if len(to_add)!=0:dbm.update(datafile,user,**to_add)
            print('.'*30)

        elif i == '3':
            clear()
            print('My data:\n'+'.'*30)
            print('\n'.join(['[{}] {}: {}'.format(ind,a,b) for ind,(a,b) in enumerate(udata.items()) if a!='password']))
            print('.'*30)
            inp = input('Index to delete ("." to return): ')
            if inp == '.':continue
            key = [a for a in udata.keys()][int(inp)]
            if key == 'password':continue
            del udata[key]  
            dbm.delete_data(datafile,user,*[key])
            print('{} deleted successfully.'.format(key))
            

        elif i == '4':
            clear()
            print('Personal info:\n'+'.'*30)
            personalkeys = ('username','name','surname','password','biography','address','link','others')
            for pk in personalkeys:
                print('{}: {}'.format(pk,udata.get(pk,'__') \
                    if not pk  in ('password','username') else user if pk =='username' else '*'*len(udata.get('password',0) if udata.get('password',0) else '__')))
            inp = input('.'*30+'\n[1]: Edit\n[.]: Return\n[>]: ') 
            if inp in ('1','.'):
                if inp == '.':continue
                else:
                    while True:
                        personalkeys = ('name','surname','password','biography','address','link','others')
                        personaldata = {k:udata.get(k,'__') for k in personalkeys}
                        clear()
                        print('Edit personal info:\n'+'.'*30)
                        print('\n'.join(['[{}] {}: {}'.format(ind,a,b if a!= 'password' else '*'*len(b)) for ind,(a,b) in enumerate(personaldata.items())]))
                        print('.'*30)
                        inp = input('Index to change ("." to return): ')
                        if inp == '.':break
                        elif inp not in [str(a) for a in range(len(personalkeys))]:print('Invalid key.');continue
                        key = [a for a in personaldata.keys()][int(inp)]
                        if key == 'password':
                            if udata.get('password','') == input('Confirm password: '):udata.update({'password':input('New password: ')});continue
                            else:print('[!] Password dont match.');continue
                        narg = input('[{}]: '.format(key))
                        udata.update({key:narg})
                        print(udata)
                    dbm.update(datafile,user,**udata)
                    continue
        
            else:print('[!] Invalid key.')
    

        elif i == '5':
            if input('\n[!] Are you sure you want to delete all data?\n This action cant be undone. (Y/n): ') \
                    in ('y','Y','Yes','YES','yes'): 
                if udata.get('password','') == input('Confirm password: '):
                    del data[user]
                    dbm.delete_user(datafile,user)
                    break
                else:print('[!] Password dont match.')

            else:print('going back.');break



        


def main():
    while True:
        try:  access(*login())

        except KeyboardInterrupt: 
            try:
                if input('\nAre you sure you want to go out? (Y/n): ') in ('y','Y','Yes','YES','yes'): break
            except KeyboardInterrupt: continue
            



if __name__ == '__main__':
    main()
    



    
