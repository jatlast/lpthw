from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this."
        , "Your Mom would be proud...if she were smarter."
        , "Such a luser."
        , "I have a small puppy that's better at this."
        , "You're worse that your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Parcel #25 have invaded your ship and
            destroyed your entire crew.  You are the last surviving 
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and 
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate-filled
            body.  He's blocking the door to the Armory and 
            about to pull a weapon to blast you.
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
            Quick on the draw you yank out your blaster and fire
            it at the Gothon.  His clown costume is flowing and
            moving around his boxy, which throws off oyur aim.
            Your laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his mother
            bought him, which makes him fly into an insane rage
            and blast you repeatedly in the face until you are 
            dead.  Then he eats you
            """))
            return 'death'

        elif action == "dodge":
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head.  In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out.  You wake up shortly after only to
                die as the Gothon stomps on your head and eats you.
            """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
            Lucky fo you they mad you learn Gothon insults in
            the academy.  You tell the on Gothon joke you know:
            Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
            fur fvgf nebhaq gur ubhfr.  The Gothon stops, tries
            not to laugh, then busts out laughing and can't move.
            While he's laughing you run up and shoot hime square in
            the head putting him down, then jump through the 
            Weapon Armory door.
            """))
            return 'laser_weapon_armory'

        else:
            print("DOES NO COMPUTE!")
            return 'central_corridor'
            
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        ... The armory
        """))

        code = f"{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print(f"BZZZZEDDD! {guesses} down {10 - guesses -1} to go. Hint, the code is {code}")
            guesses += 1
            guess = input("[keyboard]> ")

        if guess == code:
            print(dedent("""
            The container clicks open...
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            The lock buzzez...
            """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        ... The bridge...
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
            In a panic...
            """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
            You point your blaster......
            """))
            return 'escape_pod'

        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        ... Escape pod ...
        """))

        good_pod = randint(1,5)
        #print(f"Hint, the correct pod is #{good_pod}")
        guess = input(f"[pod #]> Hint, the correct pod is #{good_pod}> ")

        if int(guess) != good_pod:
            print(dedent(f"""
            You jump into pod {guess}...
            """))
            return 'death'
        else:
            print(dedent(f"""
            You jump into pod {guess}......
            You won!
            """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won!  Good Job.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor()
        , 'laser_weapon_armory': LaserWeaponArmory()
        , 'the_bridge': TheBridge()
        , 'escape_pod': EscapePod()
        , 'death': Death()
        , 'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
