from ursina import Audio, invoke
class AudioManager:
    def __init__(self):
        self.current_music = None
        self.music_volume = 0.8
        self.sfx_volume = 0.8
    def play_music(self, path, loop=True, volume=None):
        if self.current_music:
            try: self.current_music.stop()
            except: pass
        vol = self.music_volume if volume is None else volume
        self.current_music = Audio(path, autoplay=True, loop=loop, volume=vol)
        return self.current_music
    def fade_in(self, path, duration=2.0, target_vol=None, loop=True):
        target = self.music_volume if target_vol is None else target_vol
        aud = Audio(path, autoplay=True, loop=loop, volume=0)
        self.current_music = aud
        steps = 8
        step_t = duration / steps
        for i in range(1, steps+1):
            invoke(lambda v=target*(i/steps): setattr(aud, 'volume', v), delay=step_t * i)
        return aud
    def fade_out(self, duration=1.0):
        aud = self.current_music
        if not aud: return
        steps = 8
        step_t = duration / steps
        for i in range(1, steps+1):
            invoke(lambda v=max(0, aud.volume*(1 - i/steps)): setattr(aud, 'volume', v), delay=step_t * i)
        invoke(lambda: aud.stop(), delay=duration + 0.05)
        self.current_music = None
    def play_sfx(self, path, volume=None):
        vol = self.sfx_volume if volume is None else volume
        Audio(path, autoplay=True, volume=vol)
