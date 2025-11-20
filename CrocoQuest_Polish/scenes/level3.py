from ursina import *
from system.utils import camera_shake, spawn_particles
class Level3(Entity):
    def __init__(self, slot=1, player_name='Player'):
        super().__init__()
        Text('Level 3 - Whispering Glade (Demo)', y=0.3)
        self.player = Entity(model='quad', texture='assets/textures/croc_slot1.png', scale=(1.5,1), position=(0,1,0))
    def input(self, key):
        if key == 'e':
            camera_shake(); spawn_particles(self.player.position)
