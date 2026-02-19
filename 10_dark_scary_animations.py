# ========================================
# 10 DARK & SCARY PSYCHEDELIC ANIMATIONS
# Ominous, eerie, and unsettling patterns
# ========================================

# ========================================
# VARIATION 1: ABYSSAL VOID EYE
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Abyssal void eye
    v = np.mod(
        theta * 6 + 
        np.sin(r/8 + t*1.5) * 3 +
        np.cos(theta * 12 - t*2) * 2,
        1.0
    )
    
    # Dark intensity - bright center fading to black
    intensity = np.exp(-np.power(r/100, 2)) * 0.8
    intensity = intensity * (1 + np.sin(t*3) * 0.3)

    h_ = v
    s_ = np.ones_like(v) * 0.95
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_01_abyssal_void.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 2: WRITHING TENTACLES
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Writhing tentacles
    v = np.mod(
        theta * 8 +
        np.sin(r/10 + theta*4 + t*2.5) * 3 +
        np.cos(r/15 - theta*6 - t*1.8) * 2.5 +
        np.sin(theta * 16) * 1.5,
        1.0
    )
    
    # Pulsing organic darkness
    intensity = np.abs(np.sin(theta * 8)) * 0.5 + 0.15
    intensity = intensity * (1.0 / (1.0 + r/80))
    intensity = intensity * (0.7 + np.sin(t*4) * 0.3)

    h_ = v
    s_ = np.ones_like(v)
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_02_writhing_tentacles.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 3: HAUNTED MIRROR CRACKS
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Haunted mirror cracks
    v = np.mod(
        np.sin(x/20 + y/30 + t*1.5) * 3 +
        np.cos(x/30 - y/20 - t*2) * 3 +
        r/40 +
        np.abs(np.sin(theta * 7)) * 2,
        1.0
    )
    
    # Shattered glass intensity
    crack = np.abs(np.sin(x/15) * np.sin(y/15))
    intensity = crack * 0.4 + 0.1
    intensity = intensity * (np.sin(t*2.5) * 0.2 + 0.6)

    h_ = v
    s_ = np.ones_like(v) * 0.8
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_03_haunted_mirror.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 4: DEMONIC PENTAGRAM
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Demonic pentagram
    v = np.mod(
        theta * 5 + 
        np.sin(r/12 + t*2) * 2.5 +
        np.cos(theta * 10 + t*1.5) * 2 +
        np.abs(np.sin(theta * 5)) * 3,
        1.0
    )
    
    # Pentragram glow
    star_intensity = np.abs(np.sin(theta * 5)) * 0.6
    intensity = star_intensity * (1.0 / (1.0 + r/70)) + 0.05
    intensity = intensity * (0.8 + np.sin(t*5) * 0.2)

    h_ = v
    s_ = np.ones_like(v)
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_04_demonic_pentagram.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 5: CRAWLING INSECTS
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Crawling insects
    v = np.mod(
        np.sin(x/8 + t*3) * 2.5 +
        np.sin(y/8 - t*3.5) * 2.5 +
        np.cos((x + y)/10 + t*2) * 2 +
        r/50,
        1.0
    )
    
    # Skittering darkness
    intensity = np.sin(x/10 + t*3) * np.cos(y/10 - t*3) * 0.25 + 0.15
    intensity = intensity * np.exp(-r/180)
    intensity = np.clip(intensity, 0, 1)

    h_ = v
    s_ = np.ones_like(v) * 0.9
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_05_crawling_insects.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 6: SPIRALING INTO MADNESS
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Spiraling into madness
    v = np.mod(
        theta * 9 + 
        np.log1p(r/30) * 6 * np.sin(t*1.5) +
        np.sin(r/8 + t*2) * 3 +
        np.cos(theta * 18 - t*2.5) * 2,
        1.0
    )
    
    # Descent into darkness
    intensity = 1.0 / (1.0 + np.power(r/90, 1.5))
    intensity = intensity * (0.5 + np.sin(t*3) * 0.3)
    intensity = intensity * (0.8 + np.sin(theta * 9 + t) * 0.2)

    h_ = v
    s_ = np.ones_like(v)
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_06_spiraling_madness.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 7: PULSATING VEINS
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Pulsating veins
    v = np.mod(
        np.sin(r/15 + t*2.5) * 3 +
        np.cos(r/10 - t*3) * 2.5 +
        np.sin(theta * 13 + t) * 2 +
        theta * 2,
        1.0
    )
    
    # Organic pulsing
    pulse = np.sin(r/12 + t*4) * 0.3 + 0.3
    intensity = pulse * (np.sin(r/8 - t*2) * 0.2 + 0.4)
    intensity = intensity * np.exp(-r/200)

    h_ = v
    s_ = np.ones_like(v) * 0.95
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_07_pulsating_veins.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 8: NIGHTMARE PORTAL
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Nightmare portal
    v = np.mod(
        theta * 11 + 
        np.sin(r/6 + t*2.8) * 3.5 +
        np.power(r/100, 1.3) * np.sin(theta*22 + t*2) * 4,
        1.0
    )
    
    # Vortex of dread
    vortex = (1.0 / (1.0 + r/60)) * 0.7
    flicker = np.sin(t*8) * 0.15 + 0.85
    intensity = vortex * flicker + 0.05

    h_ = v
    s_ = np.ones_like(v)
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_08_nightmare_portal.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 9: SKELETAL FINGERS
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Skeletal fingers
    v = np.mod(
        np.sin(theta * 20 + t*1.5) * 2.5 +
        np.cos(r/12 + theta*10 - t*2) * 2.5 +
        r/35 +
        np.abs(np.sin(theta * 10)) * 2,
        1.0
    )
    
    # Bony grasping
    fingers = np.abs(np.sin(theta * 10)) * 0.6
    intensity = fingers * (1.0 / (1.0 + r/75)) + 0.08
    intensity = intensity * (0.7 + np.sin(t*6) * 0.2)

    h_ = v
    s_ = np.ones_like(v) * 0.85
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_09_skeletal_fingers.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 10: CORRUPTED REALITY GLITCH
# ========================================

import numpy as np
from PIL import Image

w, h = 512, 512
pi = np.pi
e = np.e

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Corrupted reality glitch
    v = np.mod(
        np.sin(x/12 + np.sin(t*4) * 5) * 3 +
        np.cos(y/12 + np.cos(t*3.5) * 5) * 3 +
        np.sin(r/10 + theta*7 + t*2) * 2 +
        theta * 1.5,
        1.0
    )
    
    # Glitching darkness
    glitch = np.sin(y/8 + np.sin(t*10) * 3) * 0.3 + 0.2
    intensity = glitch * (np.cos(t*7) * 0.2 + 0.5)
    intensity = np.clip(intensity, 0.05, 0.6)

    h_ = v
    s_ = np.ones_like(v)
    v_ = intensity

    i_ = (h_ * 6.0).astype(int)
    f = (h_ * 6.0) - i_
    p = v_ * (1.0 - s_)
    q = v_ * (1.0 - f * s_)
    t_ = v_ * (1.0 - (1.0 - f) * s_)

    i_mod = i_ % 6

    r_ = np.choose(i_mod, [v_, q, p, p, t_, v_])
    g_ = np.choose(i_mod, [t_, v_, v_, q, p, p])
    b_ = np.choose(i_mod, [p, p, t_, v_, v_, q])

    img = np.stack([r_, g_, b_], axis=-1)
    img = (img * 255).astype(np.uint8)

    frames.append(Image.fromarray(img))

frames[0].save("scary_10_reality_glitch.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)

print("All 10 dark & scary psychedelic animations complete! 💀🕷️👁️")
