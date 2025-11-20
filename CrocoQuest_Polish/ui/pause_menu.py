from ursina import *
from system.save_manager import save_progress, capture_preview_stub
from system.config import set_music_volume, set_sfx_volume, set_difficulty, get_config

class PauseMenu(Entity):
    def __init__(self, level_entity=None):
        super().__init__(parent=camera.ui)
        self.level = level_entity
        self.panel = Entity(parent=self, model='quad', scale=(0.6,0.6), color=color.rgba(0,0,0,200))
        Text('PAUSED', parent=self.panel, y=0.22, scale=2, color=color.gold)
        self.resume_btn = Button('Resume', parent=self.panel, y=0.06, on_click=self.resume)
        self.save_btn = Button('Save', parent=self.panel, y=-0.06, on_click=self.save)
        self.exit_btn = Button('Exit to Menu', parent=self.panel, y=-0.18, on_click=self.exit_to_menu)
        self.settings_btn = Button('Settings', parent=self.panel, y=-0.30, on_click=self.open_settings)
    def resume(self): destroy(self)
    def save(self):
        if not self.level: return
        save_progress(self.level.slot, getattr(self.level,'current_level',1), getattr(self.level,'player_name',None), preview_path=capture_preview_stub(self.level.slot))
        popup = Text('💾 Saved', y=0.3, color=color.lime, parent=camera.ui)
        destroy(popup, delay=1.5)
    def exit_to_menu(self):
        from scenes.main_menu import MainMenu
        destroy(self.level); destroy(self); MainMenu()
    def open_settings(self):
        SettingsPanel()

class SettingsPanel(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)
        self.panel = Entity(parent=self, model='quad', scale=(0.6,0.5), color=color.rgba(10,10,10,220))
        Text('Settings', parent=self.panel, y=0.2, scale=1.3)
        cfg = get_config()
        self.music_slider = Slider(min=0, max=1, step=0.05, value=cfg['music_volume'], y=0.05, parent=self.panel)
        self.sfx_slider = Slider(min=0, max=1, step=0.05, value=cfg['sfx_volume'], y=-0.06, parent=self.panel)
        self.difficulty_dropdown = Dropdown(['easy','normal','hard'], default=cfg['difficulty'], y=-0.18, parent=self.panel)
        Button('Close', parent=self.panel, y=-0.36, on_click=self.close)
    def close(self):
        set_music_volume(self.music_slider.value)
        set_sfx_volume(self.sfx_slider.value)
        set_difficulty(self.difficulty_dropdown.selected)
        destroy(self)
