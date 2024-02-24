# txt-database
Creator: @hugoocf

install module throw: pip install txt-database-manager

example file: mydatabase.py

## modules:

(with) from database_manager import *

## ~get_users(filename)
returns users list

## ~get(filename)
return all data as a dict

## ~write(filename,**data:dict)
write, just to create database from nothing

## ~update(filename,username,**args:dict)
write but only for an existing user, for change or update data 

## ~add(filename,user,**args:dict)
add a new user 

## ~delete_user(filename,user)
delete user 

## ~delete_data(filename,user,*keys)
delete all data from a user key

## ~reconfig(filename)->None
change all encrypt keys

## ~clear()
clear the terminal
