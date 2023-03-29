from getpass import getpass as input

print("MORE EPIC 🪨  📄 ✂️  BATTLE")

i = 0

score1 = 0
score2 = 0

while True:
  i += 1
  print("Round", i)
  print("Select your move (R, P, or S)")
  player1 = input("Player 1 > ")
  player2 = input("Player 2 > ")
  
  if player1 == "R" and player2 == "P":
    score2 += 1
    print("Player 1's 🪨  is smothered by Player 2's 📄!")
  elif player1 == "P" and player2 == "S":
    score2 += 1
    print("Player 1's 📄 is teared by Player 2's ✂️!")
  elif player1 == "S" and player2 == "R":
    score2 += 1
    print("Player 1's ✂️  is destroyed by player 2's 🪨!")
  elif player1 == "P" and player2 == "R":
    score1 += 1
    print("Player 2's 🪨  is smothered by Player 1's 📄!")
  elif player1 == "S" and player2 == "P":
    score1 += 1
    print("Player 2's 📄  is teared by Player 1's ✂️!")
  elif player1 == "R" and player2 == "S":
    score1 += 1
    print("Player 2's ✂️  is broked by Player 1's 🪨!")
  elif player1 == player2:
    print("It is a draw. Try again!")
  elif score1 == 3:
    print("")
  else:
    print("Seems like someone put the wrong input. Try again!")

  if score1 == 3:
    print("Player 1 wins the game!", score1, "vs", score2)
    exit()
  elif score2 == 3:
    print("Player 2 wins the game!", score2, "vs", score1)
    exit()
  else:
    continue