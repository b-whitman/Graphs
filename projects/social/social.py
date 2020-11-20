import random
from util import Queue

class User:
	def __init__(self, name):
		self.name = name

class SocialGraph:
	def __init__(self):
		self.last_id = 0
		self.users = {}
		self.friendships = {}

	def add_friendship(self, user_id, friend_id):
		"""
		Creates a bi-directional friendship
		"""
		if user_id == friend_id:
			# print("WARNING: You cannot be friends with yourself")
			return False
		elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
			# print("WARNING: Friendship already exists")
			return False
		else:
			self.friendships[user_id].add(friend_id)
			self.friendships[friend_id].add(user_id)
			return True

	def add_user(self, name):
		"""
		Create a new user with a sequential integer ID
		"""
		self.last_id += 1  # automatically increment the ID to assign the new user
		self.users[self.last_id] = User(name)
		self.friendships[self.last_id] = set()

	def fisher_yates_shuffle(self, l):
		for i in range(0, len(l)):
			random_index = random.randint(i, len(l) - 1)
			l[random_index], l[i] = l[i], l[random_index]

	def populate_graph(self, num_users, avg_friendships):
		"""
		Takes a number of users and an average number of friendships
		as arguments

		Creates that number of users and a randomly distributed friendships
		between those users.

		The number of users must be greater than the average number of friendships.
		"""
		# Reset graph
		self.last_id = 0
		self.users = {}
		self.friendships = {}

		# Add users
		for user in range(num_users):
			self.add_user(user)
		
		# Create friendships
		total_friendships = avg_friendships * num_users

		friendship_combos = []

		for user_id in range(1, num_users + 1):
			for friend_id in range(user_id + 1, num_users + 1):
				friendship_combos.append((user_id, friend_id))

		self.fisher_yates_shuffle(friendship_combos)

		friendships_to_make = friendship_combos[:(total_friendships // 2)]

		for friendship in friendships_to_make:
			self.add_friendship(friendship[0], friendship[1])

	def populate_graph_linear(self, num_users, avg_friendships):
		"""
		Takes a number of users and an average number of friendships
		as arguments

		Creates that number of users and a randomly distributed friendships
		between those users.

		The number of users must be greater than the average number of friendships.
		"""
		# Reset graph
		self.last_id = 0
		self.users = {}
		self.friendships = {}

		# Add users
		for user in range(num_users):
			self.add_user(user)
		
		# Create friendships
		total_friendships = avg_friendships * num_users
		friendships_made = 0

		while friendships_made < total_friendships:
			first_user = random.randint(1, num_users)
			second_user = random.randint(1, num_users)
			friendship_made = self.add_friendship(first_user, second_user)

			if friendship_made:
				friendships_made += 2

	def get_friends(self, user_id):
		"""
		"""
		return self.friendships[user_id]

	def bfs(self, starting_vertex, destination_vertex):
		"""
		Return a list containing the shortest path from
		starting_vertex to destination_vertex in
		breath-first order.
		"""
		q = Queue()
		visited = set()
		q.enqueue([starting_vertex])

		while q.size() > 0:
			current_path = q.dequeue()
			current_node = current_path[-1]

			if current_node == destination_vertex:
				return current_path
			if current_node not in visited:
				visited.add(current_node)

				friends = self.get_friends(current_node)
				for friend in friends:
					path_copy = current_path + [friend]
					q.enqueue(path_copy)

	def get_all_social_paths(self, user_id):
		"""
		Takes a user's user_id as an argument

		Returns a dictionary containing every user in that user's
		extended network with the shortest friendship path between them.

		The key is the friend's ID and the value is the path.
		"""
		visited = {}  # Note that this is a dictionary, not a set
		for user in self.users:
			path = self.bfs(user_id, user)
			if path != None:
				visited[user] = path
		return visited


if __name__ == '__main__':
	sg = SocialGraph()
	sg.populate_graph_linear(10000, 5)
	print(len(sg.friendships[1]))
	print(sg.friendships[1])
	connections = sg.get_all_social_paths(1)
	print(len(connections))
	# 134, 95, 85, 122, 232, 172, 109, 3:45, 252, 2:64, 8:195, 6:171, 3:98, 6:125, 3:115, 3:100, 4:85, 
	print(connections)
