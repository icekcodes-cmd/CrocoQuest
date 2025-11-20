from ursina import invoke, camera, Entity, color, destroy, curve
import random
def camera_shake(intensity=0.12, duration=0.35, frequency=0.02):
    original = camera.position
    steps = max(1, int(duration / frequency))
    def _step(i):
        if i >= steps:
            camera.position = original
            return
        offset = (random.uniform(-1,1)*intensity, random.uniform(-1,1)*intensity, 0)
        camera.position = original + offset
        invoke(lambda idx=i+1: _step(idx), delay=frequency)
    _step(0)
def spawn_particles(position=(0,0,0), count=8, color_range=((200,200,200),(255,255,255)), scale=0.12, life=0.9):
    particles = []
    for i in range(count):
        c1, c2 = color_range
        col = tuple(int(c1[j] + random.random()*(c2[j]-c1[j])) for j in range(3))
        e = Entity(model='sphere', color=color.rgb(col[0],col[1],col[2]), scale=scale, position=position)
        e.animate_scale(e.scale*4, duration=life, curve=curve.out_expo)
        destroy(e, delay=life)
        particles.append(e)
    return particles
