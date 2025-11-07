player_alexie = 0
player_nicole = 0

treasure_e = 5
treasure_y = 3
game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
  move = input("Enter move (up/down/left/right): ").lower()

if move == "up":
  player_nicole += 1
if move == "down":
  player_nicole -= 1
if move == "left":
  player_alexie -= 1
if move == "right":
  player_alexie += 1
if move == "q":
  print("Maybe next time=(")
  break
else:
  print("invalid move!)
        
print(f"player position: ({player_alexie}, {player_nicole})")
        
if player_x == treasure_x and player_y == treasure_y:
  print("You Found the treasure!")
  game_running = False
