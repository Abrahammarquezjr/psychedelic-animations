# ========================================
# 10 NEW DIFFERENT PSYCHEDELIC ANIMATIONS
# Unique mathematical patterns and effects
# ========================================

# ========================================
# VARIATION 1: FIBONACCI EXPLOSION
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
    
    # Fibonacci spiral explosion
    phi = (1 + np.sqrt(5)) / 2
    v = np.mod(
        theta * phi * 2 + 
        np.sqrt(r) * pi + 
        np.sin(r/10 + t*2) * 2.5 +
        np.cos(theta * phi * 3 - t) * 1.5,
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

frames[0].save("new_01_fibonacci_explosion.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 2: HYPERBOLIC STARGATE
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
    
    # Hyperbolic stargate
    v = np.mod(
        np.arctan(r/50) * 5 + 
        theta * 7 + 
        np.sinh(r/150) * np.sin(t) * 2 +
        np.cos(theta * 14 + t*2) * 1.5,
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

frames[0].save("new_02_hyperbolic_stargate.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 3: DNA HELIX
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
    
    # DNA helix
    v = np.mod(
        x/30 * np.sin(y/40 + t) + 
        y/30 * np.cos(x/40 - t) +
        np.sin(np.sqrt(x**2 + y**2)/20 + t*3) * 2.0 +
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

frames[0].save("new_03_dna_helix.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 4: CHECKERBOARD WARP
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
    
    # Checkerboard warp
    v = np.mod(
        np.sin(x/10 + t) * np.cos(y/10 - t) * 3 +
        r/50 +
        np.sin(r/15 + theta * 5 + t*2) * 2.0,
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

frames[0].save("new_04_checkerboard_warp.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 5: MOBIUS STRIP
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
    
    # Mobius strip
    v = np.mod(
        theta * 2 + 
        np.sin(theta + t) * r/30 +
        np.cos(r/20 + theta * 2 - t*2) * 2.5 +
        np.sin(theta * 4) * np.cos(r/25 + t) * 1.5,
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

frames[0].save("new_05_mobius_strip.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 6: CRYSTALLINE LATTICE
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
    
    # Crystalline lattice
    v = np.mod(
        np.sin(x/25) * 2 + 
        np.sin(y/25) * 2 + 
        np.sin((x + y)/20 + t) * 2 +
        np.cos((x - y)/20 - t*1.5) * 2 +
        theta * 0.3,
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

frames[0].save("new_06_crystalline_lattice.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 7: SIERPINSKI FRACTAL
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
    
    # Sierpinski triangle fractal
    v = np.mod(
        np.sin(x/20 + y/30 + t) * 2.5 +
        np.cos(x/30 - y/20 - t*1.3) * 2.5 +
        np.sin(r/15 + theta * 3 + t*2) * 1.5 +
        (np.sin(x/10) * np.sin(y/10)) * 2,
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

frames[0].save("new_07_sierpinski_fractal.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 8: TORUS KNOT
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
    
    # Torus knot
    v = np.mod(
        np.sin(theta * 3 + r/20 + t*2) * 2.5 +
        np.cos(theta * 5 - r/15 - t) * 2.5 +
        r/40 +
        np.sin(theta * 2) * np.cos(r/25 + t*1.5) * 1.5,
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

frames[0].save("new_08_torus_knot.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 9: PENTAGONAL SYMMETRY
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
    
    # Pentagonal symmetry
    v = np.mod(
        theta * 5 + 
        np.sin(r/12 + t*2) * 2.5 +
        np.cos(theta * 10 + t) * 1.5 +
        np.sin(r/8 - theta * 5 + t*1.5) * 2.0 +
        np.abs(np.sin(theta * 5)) * 1.5,
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

frames[0].save("new_09_pentagonal_symmetry.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 10: LISSAJOUS CURVES
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
    
    # Lissajous curves
    v = np.mod(
        np.sin(x/30 + t) * 3 +
        np.sin(y/25 + t*1.3) * 3 +
        np.sin((x + y)/35 - t*1.7) * 2 +
        theta * 0.8 +
        r/100,
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

frames[0].save("new_10_lissajous_curves.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)

print("All 10 new different animations complete! 🎨✨")
