class Hero(object):
    def __init__(self):
        pass

class Friends(object):
    name = "rehaf"
    print "well hello %s" %name
    pass

class Enemies(object):
    pass

class Scene(object):
    pass

class Map(object):
    scenes = {
    'Home':Home(),
    'School':School(),
    'bed room':Bed_room(),
    'death':death()
    }
    def __init__ (self, start_Scene):
        self.start_Scene = start_Scene
    def next_Scene(self, scene_name):
        return Map.scenes.get(scene_name)
    def opening_Scene(self):
        return self.next_Scene(self, start_Scene)
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_Scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Home(Scene):
    def enter(self):
        print " you are in your living room, you look aroud \n",
        "nothing is around here but bordom, where would you like to head to?"
        action = raw_input('room:')
        if action == "bed room":
            pass

class School(Scene):
    pass
class Bed_room(scene):
    pass
