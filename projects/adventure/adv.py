from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {player.current_room.id : {dir : '?' for dir in player.current_room.get_exits()}}
dir_dict = {'n': 's',
            's': 'n',
            'e': 'w',
            'w': 'e'}
print(traversal_graph)

while len(traversal_graph) < len(world.rooms):
    # Could be a list comp
    unexplored_exits = []
    print(player.current_room.id)
    for key, value in traversal_graph[player.current_room.id].items():
        if value == '?':
            unexplored_exits.append(key)
    if len(unexplored_exits) > 0:
        # Pick a direction and travel
        direction = random.choice(unexplored_exits)
        prev_room = player.current_room.id
        player.travel(direction)
        traversal_path.append(direction)

        # Update traversal_graph
        if player.current_room.id not in traversal_graph:
            traversal_graph[player.current_room.id] = {dir : '?' for dir in player.current_room.get_exits()}
        traversal_graph[prev_room][direction] = player.current_room.id
        traversal_graph[player.current_room.id][dir_dict[direction]] = prev_room
    
    # Take steps in a DFS
    # Update traversal_path with each step taken
    # Update traversal_graph each time you visit a new room


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
