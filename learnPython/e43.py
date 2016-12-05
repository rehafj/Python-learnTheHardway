from sys import exit
from random import randint


class Scene(object):
    def enter(slef):
        print "not yet configured - exiting "
        exit(1)
        pass

# super classes
class Map (object):
    def __init__(self, start_scene):
        pass
    def next_scene(self, scene):
        pass
    def opening_scene(scene):
        pass


class Engine (object):
    """ the engine class runs the map """

    def __init__(self, mapinstance):
        self.mapinstance = mapinstance

    def play(self):
    	current_scene = self.mapinstance.opening_scene()
        while True:
            print " \n --------"
            pass
            next_scene_name = current_scene.enter()
            current_scene = self.mapinstance.next_scene(next_scene_name)




# sub class / inherited classes
class Death(Scene):
    quips = ["yo died looser",
            "you suck at this",
            "your mom would be so proud",
            "my cat can do better..."]
    def enter(slef):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        pass

class Central_coridor(Scene):
    pass
class Weapon_Armory(Scene):
    pass
class Bridge(Scene):
    pass
class Escape_Pod(Scene):
    pass


a_map = Map('Central_coridor')
a_Game = Engine(a_map)
a_Game.play()
