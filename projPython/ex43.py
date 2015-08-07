from random import randint
from sys import exit

class scene(object):
	# def __init__(self,Hero,Heroine):
		# self.Hero = Hero
		# self.Heroine = Heroine
	
	def enter(self):
		print "this is to overwrite in other scenes"
		exit(1)
		
class First_Meeting(scene):
	
	def enter(self):
		print "Welcome Prakhar"
		print "Your wife has some cool stuff for you"
		print "You remember our first meeting?"
		print "Let's test it baby"
		
		test = raw_input("Write date in mmddyyyy")
		
		if test == "04052015":
			print "Ohhh baby! Good for you"
			print "I know you fall in love on first meeting"
			print "Drooling all over the place and could not resist to kiss me"
			return chicago
		else:
			print "We have not completed even 2 months yet..so sad"
			return 'pitti'
			
class Lava(scene):
	def enter(self):
		print "You will get nothing"
		exit(1)
	
class Chicago():
	pass

class California():
	pass
	
class First_Flight():
	pass
	
class Marriage():
	pass
	
class First_Fight():
	pass
	
class Happy_Ending():
	pass
			
			

class map(object):
	
	scene = {
	'pitti': Lava(),
	'first_meeting': First_Meeting(),
	'chicago': Chicago(),
	'cali': California(),
	'first_fight': First_Flight(),
	'marriage': Marriage(),
	'first_fight': First_Fight(),
	'happy_ending': Happy_Ending()}
	def __init__(self, first_scene):
		self.first_scene = first_scene
		
	def opening_scene(self):
		return map.scene.get(self.first_scene)
	def next_scene(self,scene_name):
		val = map.scene.get(scene_name)
		return val
		
class engine(object):
	def __init__(self,map_object):
		self.map_object = map_object
		
	def play(self):
		current_scene = map_object.opening_scene()
		last_scene = map_object.next_scene('happy_ending')
		
		while current_scene != last_scene:
			next_scene = current_scene.enter()
			print next_scene
			current_scene = map_object.next_scene(next_scene)
		
		current_scene.enter
		
map_object = map("first_meeting")
a_game = engine(map_object)
a_game.play()