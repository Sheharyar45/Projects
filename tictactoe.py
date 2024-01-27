import random 
import math 
 
game  = {}
for i in range(1,10):
  game[i] = i


def print_game(game):
   
  for num in game:
    if num % 3 != 0 :
      print(str(game[num]) + ' | ', end = '')
    else:
      print(str(game[num]))


def exhaust(game):
  for num in game:
    if game[num] == num:
      return False
  return True



def winner(game):
  if (game[1] == game[2] == game[3]) or (game[4] == game[5] == game[6]) or (game[7] == game[8] == game[9]):
    return True
  elif (game[1] == game[4] == game[7]) or (game[2] == game[5] == game[8]) or (game[3] == game[6] == game[9]):
    return True
  elif (game[1] == game[5] == game[9]) or (game[3] == game[5] == game[7]):
    return True 
  return False


  
def take_input(game):
  print_game(game)
  choice = int(input('enter the position you want to choose  '))

  while choice not in game or game[choice] != choice:
    choice = int(input('Invalid choice try again  '))
  game[choice] = 'x'
  if winner(game):
    print('User won!')


def close(game):

  if (game[1] == game[2] == 'x' and game[3] == 3)  or (game[1] == game[3] == 'x' and game[2] == 2) or (game[3] == game[2] == 'x' and game[1] == 1):  
    for i in range(1,4):
      if game[i] == i:
        return i
  if (game[4] == game[5] == 'x' and game[6] == 6)  or (game[4] == game[6] == 'x' and game[5] == 5) or (game[5] == game[6] == 'x' and game[4] == 4):  
    for i in range(4,7):
      if game[i] == i:
        return i
  if (game[7] == game[8] == 'x' and game[9] == 9)  or (game[7] == game[9] == 'x' and game[8] == 8) or (game[8] == game[9] == 'x' and game[7] == 7):  
    for i in range(7,10):
      if game[i] == i:
        return i
  if (game[1] == game[4] == 'x' and game[7] == 7)  or (game[1] == game[7] == 'x' and game[4] == 4) or (game[7] == game[4] == 'x' and game[1] == 1):  
    for i in range(1,8,3):
      if game[i] == i:
        return i
  if (game[2] == game[5] == 'x' and game[8] == 8)  or (game[2] == game[8] == 'x' and game[5] == 5) or (game[8] == game[5] == 'x' and game[2] == 2):  
    for i in range(2,9,3):
      if game[i] == i:
        return i 
  if (game[3] == game[6] == 'x' and game[9] == 9)  or (game[3] == game[9] == 'x' and game[6] == 6) or (game[9] == game[6] == 'x' and game[3] == 3):  
    for i in range(3,10,3):
      if game[i] == i:
        return i 

  if (game[1] == game[5] == 'x' and game[9] == 9)  or (game[1] == game[9] == 'x' and game[5] == 5) or (game[5] == game[9] == 'x' and game[1] == 1):  
    for i in range(1,10,4):
      if game[i] == i:
        return i

  if (game[3] == game[5] == 'x' and game[7] == 7)  or (game[3] == game[7] == 'x' and game[5] == 5) or (game[7] == game[5] == 'x' and game[3] == 3):  
    for i in range(3,8,2):
      if game[i] == i:
        return i

  return 0                                           



def winning(game):
  if (game[1] == game[2] == 'o' and game[3] == 3)  or (game[1] == game[3] == 'o' and game[2] == 2) or (game[3] == game[2] == 'o' and game[1] == 1):  
    for i in range(1,4):
      if game[i] == i:
        return i
  if (game[4] == game[5] == 'o' and game[6] == 6)  or (game[4] == game[6] == 'o' and game[5] == 5) or (game[5] == game[6] == 'o' and game[4] == 4):  
    for i in range(4,7):
      if game[i] == i:
        return i
  if (game[7] == game[8] == 'o' and game[9] == 9)  or (game[7] == game[9] == 'o' and game[8] == 8) or (game[8] == game[9] == 'o' and game[7] == 7):  
    for i in range(7,10):
      if game[i] == i:
        return i
  if (game[1] == game[4] == 'o' and game[7] == 7)  or (game[1] == game[7] == 'o' and game[4] == 4) or (game[7] == game[4] == 'o' and game[1] == 1):  
    for i in range(1,8,3):
      if game[i] == i:
        return i
  if (game[2] == game[5] == 'o' and game[8] == 8)  or (game[2] == game[8] == 'o' and game[5] == 5) or (game[8] == game[5] == 'o' and game[2] == 2):  
    for i in range(2,9,3):
      if game[i] == i:
        return i 
  if (game[3] == game[6] == 'o' and game[9] == 9)  or (game[3] == game[9] == 'o' and game[6] == 6) or (game[9] == game[6] == 'o' and game[3] == 3):  
    for i in range(3,10,3):
      if game[i] == i:
        return i 

  if (game[1] == game[5] == 'o' and game[9] == 9)  or (game[1] == game[9] == 'o' and game[5] == 5) or (game[5] == game[9] == 'o' and game[1] == 1):  
    for i in range(1,10,4):
      if game[i] == i:
        return i

  if (game[3] == game[5] == 'o' and game[7] == 7)  or (game[3] == game[7] == 'o' and game[5] == 5) or (game[7] == game[5] == 'o' and game[3] == 3):  
    for i in range(3,8,2):
      if game[i] == i:
        return i

  return 0






def comp_input(game):


  if winning(game) != 0 :
    game[winning(game)] = 'o'

  elif close(game) != 0:
    game[close(game)] = 'o'
  else:
    num = random.randint(1,9)
    while game[num] != num:
      num = random.randint(1,9)
    game[num] = 'o'
  
  if winner(game):
    print_game(game)
    print('Computer won!')









while not exhaust(game) and not winner(game):
  take_input(game)
  if not exhaust(game) and not winner(game):
    comp_input(game)


if exhaust(game):
  print('No winner.')




