import random

# Messages
victory_menssage = 'Has ganado'
defeat_message = 'Has perdido'
tie_message = 'Empate'
invalid_option_message = 'Opción no valida :('
user_win_message = 'El ganador es el usuario'
computer_win_message = 'El ganador es la computadora'

# Show messages
def show_message(message):
  return print(message)

def run_game():
  rounds = 1
  user_win = 0
  computer_win = 0
  
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    rounds += 1

    # Select a option
    def select_option():
      options = ('piedra', 'papel', 'tijera')
      user_option = input('Piedra, papel o tijera => ').lower()
      computer_option = random.choice(options)
          
      if user_option in options:
        print("Usuario = ", user_option)
        print("Computadora = ", computer_option)
      elif not user_option in options:
        show_message(invalid_option_message)
        #continue
        
      return user_option, computer_option
  
    def rules_of_game(user_option, computer_option, user_win, computer_win):
      if user_option == computer_option:
        show_message(tie_message)
        
      elif user_option == "piedra":
        if computer_option == "papel":
          show_message(defeat_message)
          computer_win += 1
      
        elif computer_option == "tijera":
          show_message(victory_menssage)
          user_win += 1
      
      elif user_option == "papel":
        if computer_option == "piedra":
          show_message(victory_menssage)
          user_win += 1
      
        elif computer_option == "tijera":
          show_message(defeat_message)
          computer_win += 1
          
      elif user_option == "tijera":
        if computer_option == "piedra":
          show_message(defeat_message)
          computer_win += 1
      
        elif computer_option == "papel":
          show_message(victory_menssage)
          user_win += 1
  
      return user_win, computer_win
    
    
    
    user_option, computer_option = select_option()
    user_win, computer_win = rules_of_game(user_option, computer_option, user_win, computer_win)
    
    # Show results of each round
    print('Resultados:')
    print(f"Usuario => {user_win}")
    print(f"Computadora => {computer_win}")
    print("-" * 50)
  
    if user_win == 3:
      show_message(user_win_message)
      break
    elif computer_win == 3:
      show_message(computer_win_message)
      break

run_game()