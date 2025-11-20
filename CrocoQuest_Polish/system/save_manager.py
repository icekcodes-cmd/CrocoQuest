import json, os
from datetime import datetime
SAVE_DIR = "saves"
PREVIEW_DIR = os.path.join(SAVE_DIR, "previews")
SAVE_SLOTS = 3
os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(PREVIEW_DIR, exist_ok=True)
def get_slot_file(slot): return os.path.join(SAVE_DIR, f"slot_{slot}.json")
def load_data(slot):
    path = get_slot_file(slot)
    if not os.path.exists(path): return None
    try:
        with open(path,'r') as f: return json.load(f)
    except: return None
def save_progress(slot, level_num, player_name=None, preview_path=None):
    data = load_data(slot) or {}
    if player_name: data['player_name']=player_name
    data['last_level']=level_num
    data['last_played']=datetime.now().strftime('%b %d, %Y - %I:%M %p')
    if preview_path: data['preview_image']=preview_path
    with open(get_slot_file(slot),'w') as f: json.dump(data,f,indent=2)
def delete_slot(slot):
    path=get_slot_file(slot)
    if os.path.exists(path): os.remove(path)
    pre=os.path.join(PREVIEW_DIR,f"slot_{slot}.png")
    if os.path.exists(pre): os.remove(pre)
def capture_preview_stub(slot): return None
