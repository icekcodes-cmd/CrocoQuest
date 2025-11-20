from ursina import *
from system.save_manager import save_progress
class ProfileMenu(Entity):
    def __init__(self, slot=1):
        super().__init__(parent=camera.ui)
        self.slot = slot
        Text('Create Your Croco', y=0.35, scale=2)
        Text('Name:', y=0.15)
        self.name_input = InputField(y=0.08, scale=(0.5,0.06))
        Button('Confirm', y=-0.05, on_click=self.confirm)
        Button('Back', y=-0.15, on_click=self.back)
    def confirm(self):
        name = self.name_input.text.strip() or 'Player'
        save_progress(self.slot, 1, player_name=name)
        destroy(self)
        from scenes.level1 import Level1
        Level1(slot=self.slot, player_name=name)
    def back(self):
        destroy(self)
        from scenes.main_menu import MainMenu
        MainMenu()
