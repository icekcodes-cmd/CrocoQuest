from ursina import Ursina, window, color, destroy
from system.audio_manager import AudioManager
from scenes.main_menu import MainMenu
app = Ursina()
window.borderless=False; window.exit_button.visible=False; window.fps_counter.enabled=True
audio = AudioManager()
import builtins; builtins.audio = audio
current_scene=None
def load_scene(scene_class,*args,**kwargs):
    global current_scene
    if current_scene:
        try: destroy(current_scene)
        except: pass
    current_scene = scene_class(*args,**kwargs)
    return current_scene
def start_game():
    load_scene(MainMenu)
if __name__=='__main__':
    start_game(); app.run()
