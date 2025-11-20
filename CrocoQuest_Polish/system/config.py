_config = {"music_volume":0.7,"sfx_volume":0.8,"difficulty":"normal"}
def set_music_volume(v): _config["music_volume"]=max(0.0,min(1.0,v))
def set_sfx_volume(v): _config["sfx_volume"]=max(0.0,min(1.0,v))
def set_difficulty(d): 
    if d in ("easy","normal","hard"): _config["difficulty"]=d
def get_config(): return _config.copy()
