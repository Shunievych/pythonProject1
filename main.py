from random import *

atribut = ['камінь', 'ножиці', 'папір']

robot = choice(atribut)

player = input('Виберіть зі списку(камінь, ножиці або папір): ')

print('робот вибрав' + robot)

print(player+' vs '+robot)

if (player == 'камінь' and robot == 'ножіці') or (player == 'папір' and robot == 'камінь') or (player == 'ножиці' and robot == 'папір'):
    print('користувач переміг')

if robot == player:
    print('нічия')
