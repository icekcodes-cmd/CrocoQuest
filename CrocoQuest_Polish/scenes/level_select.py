from ursina import *
class LevelSelect(Entity):
    def __init__(self):
        super().__init__(parent=camera.ui)
        Text('Level Select', y=0.4, scale=2)
        y = 0.15
        Button('Level 1', parent=camera.ui, y=y, on_click=self.load1); y -= 0.12
        Button('Level 2', parent=camera.ui, y=y, on_click=self.load2); y -= 0.12
        Button('Level 3', parent=camera.ui, y=y, on_click=self.load3); y -= 0.12
        Button('Back', parent=camera.ui, y=y-0.05, on_click=self.back)
    def load1(self):
        destroy(self); from scenes.level1 import Level1; Level1()
    def load2(self):
        destroy(self); from scenes.level2 import Level2; Level2()
    def load3(self):
        destroy(self); from scenes.level3 import Level3; Level3()
    def back(self):
        destroy(self); from scenes.main_menu import MainMenu; MainMenu()
