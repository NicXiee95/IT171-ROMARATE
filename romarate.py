player_alexie = 0
player_nicole = 0

treasure_e = 5
treasure_y = 3
game_running = True

print(f"Find the treasure at ({treasure_x}, {treasure_y})!")
while game_running:
  move = input("Enter move (up/down/left/right): ")
# TODO: update player_x and player_y based on move
print(f"Player position: ({player_x}, {player_y})")
# TODO: check if player has reached the treasure
move = input("Enter move (up/down/left/right): ")
if move == "w":
  player_y += 1
if move == "s":
  player_y -= 1
if move == "a":
  player_x -= 1
if move == "d":
  player_x += 1
if move == "q":
  game_running = False
else:
  print("invalid move!)
print(f"player position: ({player_x}, {player_y})")
if player_x == treasure_x and player_y == treasure_y:
  print("You Found the treasure!")
  game_running = False
