import database_manager as dbm
import time,os,sys

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
    for timeout in range(100):
        #get user
        user = input('User: ')
        if not user in users: print('[!] Unfound user, retry.');continue
        #get password
        for a in range(3):
            password = input('Password (".." to go back): ')
            if password == '..':break
            else:
                cup =  check_UP(data,user,password)
                if cup[0]:return(data[user],user)
                else:print('[!] ',cup[1],'. Remainig attempts: ',2-a,sep='')
        print('[!] Timeout: ',timeout,'s',sep='')
        time.sleep(timeout)


    else:
        while True:
            input('|$|~PERMABAN~|$|')


def access(*args):
    global data
    udata,user = args
    os.system('clear' if sys.platform == 'Win' else 'cls')
    print('Wellcome ',user,'!',sep='')
    while True:
        i = input('''
    [1]: View data.
    [2]: Add/edit data.
    [3]: Delete data.
    [4]: Change password.
    [5]: Delete user.
    [.]: Log out
    \n>> ''')

        if not i in '12345.':print('Invalid entry. Please retry.');continue

        elif i == '1':
            print('My data:\n'+'.'*30)
            print('\n'.join([f'{a}: {b}' for a,b in udata.items() if a!='password']))
            input('.'*30+'\nPress any key to return.')

        elif i == '2':
            print('Add data:\n'+'.'*30)
            to_add = {}
            while True:
                key = input('Key (".." to return): ')
                if not key:print('invalid key');continue
                elif key == '..':break
                args = input(f'Args for {key}: ')
                if not args:print('invalid args');continue
                to_add.update({key:args})
                data.update({key:args})
                udata.update({key:args})
                print(f'({key}: {args}) Successfully added')
            if len(to_add)!=0:dbm.update(datafile,user,**to_add)
            print('.'*30)

        elif i == '3':
            print('My data:\n'+'.'*30)
            print('\n'.join([f'[{ind}] {a}: {b}' for ind,(a,b) in enumerate(udata.items()) if a!='password']))
            inp = input('.'*30+'\nIndex of the data to delete: ')
            if not inp in ''.join([str(a) for a in range(len(data))]):print('Unfound index');continue

            



        elif i == '4':pass
        elif i == '5':pass

        else:print('going back.');break

        


def main():
    while True:
        try:access(*login())
        except KeyboardInterrupt: 
            if input('\nAre you sure you want to go out? (Y/n): ') \
                in ('y','Y','Yes','YES','yes'): break



if __name__ == '__main__':
    main()
    



    