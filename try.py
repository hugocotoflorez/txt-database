from database_manager import *

data={
    'hugo':{'password':'hugo1003','edad':'16'},
    'hugoocf':{'password':'1003','edad':'16'},
    'hugocf':{'password':'hugo1003','edad':'16'},
    'hugocoto':{'password':'hug1003','edad':'16'},
    'hugoocoto':{'password':'huo1003','edad':'16','localidad':'Espana','anno nacimiento':'2005'},
    'hugod':{'password':'hu03','edad':'16'},
    'hugoc':{'password':'hugo103','edad':'16'},
    'hugoccff':{'password':'hu03','edad':'16'}
}
#write('data',**data)
mire_data = {'edad':'16','password':'1234'}

add('data','mire',**mire_data)

update('data','mire',**{'algo':'1987'})

print(get('data')['mire'])

delete_data('data','mire',*['edad','anno'])

print(get('data')['mire'])

#delete_user('data','mire')

print(get('data').keys())



reconfig('data')