#Proyecto a desarrollar sobre condicionales y el juego de piedra, papel o tijera
import random as rnd

options = ('piedra','papel','tijera')
comp_wins = 0
user_wins = 0
rondas = 1

while True:
  print(f'\n{"*"*15}\nRONDA = {rondas}')
  print(f'Computadora = {comp_wins}\nUsuario = {user_wins}')
  user_input=input(f"¿Piedra, papel o tijera? ")
  user_input=user_input.lower()
  if not user_input in options:
    print(f'Esa opción no es válida')
    continue
    
  computer_option=rnd.choice(options)
  
  print(f'User option = {user_input}\nComputer option = {computer_option}\n')
  
  if user_input == computer_option:
    print('Empate')
    print(f'El usuario escogió {user_input} y la computadora escogió {computer_option}')
  elif user_input=='piedra':
    if computer_option=='tijera':
      print('piedra gana a tijera')
      print('User ganó')
      user_wins+=1
    else:
      print('Papel gana a piedra')
      print('Computer ganó')
      comp_wins+=1
  elif user_input=='papel':
    if computer_option=='piedra':
      print('Papel gana a piedra')
      print('User ganó')
      user_wins+=1
    else:
      print('Tijera gana a papel')
      print('Computer ganó')
      comp_wins+=1
  elif user_input=='tijera':
    if computer_option=='papel':
      print('Tijera gana a papel')
      print('User ganó')
      user_wins+=1
    else:
      print('Piedra gana a tijera')
      print('Computer ganó')
      comp_wins+=1
  if user_wins==2:
    print(f'El ganador es el usuario')
    break
  elif comp_wins==2:
    print(f'El ganador es la computadora')
    break
  rondas+=1