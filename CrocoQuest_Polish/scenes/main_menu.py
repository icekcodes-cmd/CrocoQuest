from ursina import *
from system.audio_manager import AudioManager
from system.save_manager import load_data, SAVE_SLOTS
audio = AudioManager()
class MainMenu(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)
        camera.ui.enabled = True
        self.title = Text('🐊 CROCOQUEST 🌀', y=0.38, scale=3, color=color.cyan)
        self.t = 0
        self.bg = Entity(model='quad', texture='assets/textures/water_tile.png', scale=(8,4), z=1)
        self.float_croc = Entity(parent=camera.ui, model='quad', texture='assets/textures/croc_slot1.png', scale=(0.4,0.25), y=0.15)
        self.create_slot_buttons()
        audio.fade_in('assets/sounds/menu_loop.wav', duration=1.0, target_vol=0.5)
    def create_slot_buttons(self):
        start_y = 0.05
        for i in range(1, SAVE_SLOTS+1):
            data = load_data(i)
            if data:
                label = "Slot %d: %s - L%d" % (i, data.get('player_name','Player'), data.get('last_level',1))
            else:
                label = "Slot %d: Empty - New Game" % i
            Button(text=label, parent=camera.ui, y=start_y, scale=(0.6,0.08), on_click=lambda i=i, d=data: self.load_slot(i,d))
            start_y -= 0.12
        Button('Level Select', parent=camera.ui, y=start_y-0.02, scale=(0.25,0.07), on_click=self.open_level_select)
        Button('Settings', parent=camera.ui, y=start_y-0.14, scale=(0.25,0.07), on_click=self.open_settings)
        Button('Quit', parent=camera.ui, y=start_y-0.26, scale=(0.25,0.07), on_click=application.quit)
    def load_slot(self, slot, data):
        destroy(self)
        if data:
            from scenes.level1 import Level1
            Level1(slot=slot, player_name=data.get('player_name'))
        else:
            from scenes.profile_menu import ProfileMenu
            ProfileMenu(slot=slot)
    def open_settings(self):
        from ui.pause_menu import SettingsPanel
        SettingsPanel()
    def open_level_select(self):
        destroy(self)
        from scenes.level_select import LevelSelect
        LevelSelect()
    def update(self):
        self.t += time.dt
        self.float_croc.y = 0.15 + math.sin(self.t*1.2)*0.02
