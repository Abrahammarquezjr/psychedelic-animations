# ========================================
# 10 FINAL DIFFERENT PSYCHEDELIC ANIMATIONS
# Advanced mathematical patterns and geometric forms
# ========================================

# ========================================
# VARIATION 1: AURORA WAVES
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
    
    # Aurora borealis waves
    v = np.mod(
        np.sin(y/30 + t*2) * 3 +
        np.sin((x + y/2)/25 + t*1.5) * 2.5 +
        np.cos(x/35 - t) * 2 +
        np.sin(r/20 + theta*2 + t*0.5) * 1.5,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_01_aurora_waves.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 2: HEXAGONAL TESSELLATION
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
    
    # Hexagonal tessellation
    hex1 = np.sin(x/20 + t)
    hex2 = np.sin((x * np.cos(pi/3) + y * np.sin(pi/3))/20 + t*1.3)
    hex3 = np.sin((x * np.cos(2*pi/3) + y * np.sin(2*pi/3))/20 + t*0.7)
    
    v = np.mod(
        hex1 * 2.5 + hex2 * 2.5 + hex3 * 2.5 +
        r/60 +
        theta * 0.5,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_02_hexagonal_tessellation.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 3: VORONOI CELLS
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
    
    # Voronoi cells simulation
    v = np.mod(
        np.sin(r/25 + theta*7 + t*2) * 2.5 +
        np.cos(r/18 - theta*5 - t*1.5) * 2.5 +
        np.abs(np.sin(theta * 11)) * 2 +
        np.sin(r/12 + t) * 1.5,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_03_voronoi_cells.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 4: POLAR ROSE
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
    
    # Polar rose pattern
    rose = np.sin(theta * 7) * r/60
    
    v = np.mod(
        rose * 5 +
        np.sin(r/15 + t*2) * 2.5 +
        np.cos(theta * 14 + t) * 2 +
        theta * 2,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_04_polar_rose.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 5: MOIRÉ INTERFERENCE
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
    
    # Interference moiré
    v = np.mod(
        np.sin(x/12 + y/12 + t*2) * 3 +
        np.sin(x/12 - y/12 - t*2) * 3 +
        np.cos(r/15 + t) * 1.5 +
        theta * 0.4,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_05_moire_interference.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 6: CARDIOID HEART
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
    
    # Cardioid heart pattern
    cardioid = r - 100 * (1 + np.cos(theta))
    
    v = np.mod(
        cardioid/30 +
        np.sin(r/10 + t*2) * 2.5 +
        np.cos(theta * 8 + t*1.5) * 2 +
        theta * 1.5,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_06_cardioid_heart.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 7: SUNFLOWER SEEDS
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
    
    # Sunflower seed pattern
    n = np.arange(500)
    angle = n * 2.4  # Golden angle
    radius = np.sqrt(n) * 10
    
    v = np.mod(
        np.sin(r/10 + theta * 13 + t*2) * 2.5 +
        np.cos(r/15 - theta * 21 - t*1.3) * 2.5 +
        theta * 3,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_07_sunflower_seeds.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 8: EPICYCLOID WHEELS
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
    
    # Epicycloid wheels
    v = np.mod(
        np.sin(theta * 4 + r/10 + t*2) * 2 +
        np.cos((theta * 4 + r/15) * 3 - t) * 2 +
        r/30 +
        np.sin(theta * 8) * np.cos(r/20 + t*1.5) * 2,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_08_epicycloid_wheels.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 9: DIFFRACTION GRATING
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
    
    # Diffraction grating
    v = np.mod(
        np.power(np.sin(x/15 + t), 2) * 5 +
        np.power(np.cos(y/15 - t*1.3), 2) * 5 +
        r/80 +
        theta * 0.5,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_09_diffraction_grating.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 10: HYPOCYCLOID GEARS
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
    
    # Hypocycloid gears
    v = np.mod(
        np.sin(theta * 7 - r/18 + t*2) * 2.5 +
        np.cos(theta * 5 + r/25 - t*1.7) * 2.5 +
        np.sin(r/10 + t*1.2) * 2 +
        theta * 1.8,
        1.0
    )

    h_ = v
    s_ = np.ones_like(v)
    v_ = np.ones_like(v)

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

frames[0].save("final_10_hypocycloid_gears.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)

print("All 10 final different animations complete! 🌟💫")
