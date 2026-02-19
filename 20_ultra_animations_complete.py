# ========================================
# 20 ULTRA PSYCHEDELIC ANIMATIONS COLLECTION
# Advanced patterns with diverse mathematical techniques
# ========================================

import numpy as np
from PIL import Image

# ========================================
# VARIATION 1: FRACTAL ZOOM
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.log1p(r/20) * 8 * np.sin(t*2) + theta * 6 + np.sin(r/10 + t*3) * 2,
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

frames[0].save("ultra_01_fractal_zoom.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 2: PINWHEEL ROTATION
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        theta * 6 + np.sin(theta * 12 + t*2) * 2 + r/40 + np.cos(r/15 - t) * 1.5,
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

frames[0].save("ultra_02_pinwheel.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 3: ZEBRA STRIPES
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.sin(y/10 + t*2) * 4 + np.cos(x/15 - t*1.5) * 3,
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

frames[0].save("ultra_03_zebra_stripes.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 4: SPIRAL GALAXY ARMS
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        theta * 3 + r/25 + np.sin(theta * 6 - r/20 + t*2) * 3,
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

frames[0].save("ultra_04_spiral_arms.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 5: PSYCHEDELIC CHECKERBOARD
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.floor(x/30 + t) + np.floor(y/30 - t) + np.sin(r/20 + t) * 2,
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

frames[0].save("ultra_05_psychedelic_checker.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 6: ROTATING TRIANGLES
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.sin(theta * 3 + t) * r/25 + np.cos(theta * 6 - t*1.5) * 2.5 + theta * 4,
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

frames[0].save("ultra_06_rotating_triangles.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 7: RADIAL RAINBOW
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        theta * 2 + np.sin(r/8 + t*2.5) * 3,
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

frames[0].save("ultra_07_radial_rainbow.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 8: TUNNEL VISION
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        1/(r/80 + 0.2) + theta * 8 + np.sin(t*3) * 2,
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

frames[0].save("ultra_08_tunnel_vision.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 9: FLOWER PETALS
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.abs(np.sin(theta * 7)) * 3 + r/30 + np.sin(r/12 + t*2) * 2,
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

frames[0].save("ultra_09_flower_petals.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 10: ELECTRIC GRID
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.sin(x/12 + t*2) * 3 + np.sin(y/12 + t*2) * 3 + r/80,
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

frames[0].save("ultra_10_electric_grid.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 11: CROSSHATCH PATTERN
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.sin((x + y)/18 + t*2) * 2.5 + np.sin((x - y)/18 - t*2) * 2.5 + theta * 0.5,
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

frames[0].save("ultra_11_crosshatch.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 12: PULSE WAVES
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.sin(r/6 + t*3) * 4 + theta * 1.2,
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

frames[0].save("ultra_12_pulse_waves.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 13: STAR FIELD
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        theta * 48 + np.sin(r/15 + t*2) * 2 + r/50,
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

frames[0].save("ultra_13_star_field.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 14: WARPED REALITY
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.tanh(r/80) * 5 + theta * 10 + np.sin(theta * 20 + t*2) * 2,
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

frames[0].save("ultra_14_warped_reality.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 15: COSMIC RAYS
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        theta * 20 + np.sin(r/12 + theta*10 + t*2) * 3 + r/80,
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

frames[0].save("ultra_15_cosmic_rays.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 16: BUBBLE CHAMBER
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.sin(r/8 + t*2) * 3 + np.sin(r/12 - t*2.5) * 3 + np.sin(r/16 + t*1.5) * 2,
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

frames[0].save("ultra_16_bubble_chamber.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 17: OSCILLATING DIAMONDS
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.abs(x - 256)/12 + np.abs(y - 256)/12 + np.sin(t*3) * 5,
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

frames[0].save("ultra_17_oscillating_diamonds.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 18: SINUSOIDAL MESH
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.sin(x/15 + y/10 + t*2) * 3 + np.cos(x/10 - y/15 - t*1.5) * 3,
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

frames[0].save("ultra_18_sinusoidal_mesh.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 19: HYPNOTIC SPIRAL
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        theta * 12 + np.sqrt(r) * 0.8 + np.sin(t*2.5) * 3,
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

frames[0].save("ultra_19_hypnotic_spiral.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 20: QUANTUM FOAM
# ========================================

w, h = 512, 512
pi = np.pi

frames = []
num_frames = 60

cy, cx = h//2, w//2
y, x = np.indices((h, w))
r = np.sqrt((x - cx)**2 + (y - cy)**2)
theta = np.arctan2(y - cy, x - cx)

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    v = np.mod(
        np.sin(x/20 + t*2) * 2 + np.sin(y/20 - t*2) * 2 + 
        np.sin(r/15 + theta*5 + t) * 2,
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

frames[0].save("ultra_20_quantum_foam.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)

print("All 20 ultra psychedelic animations complete! 🎆🌟🎨")
