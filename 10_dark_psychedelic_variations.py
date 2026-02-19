# ========================================
# 10 DARK PSYCHEDELIC VARIATIONS
# Black backgrounds with vibrant neon colors
# ========================================

# ========================================
# DARK VARIATION 1: NEON RIPPLES
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
    
    # Dark neon ripples
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.cos(r/12 - t*1.5) * 1.5,
        1.0
    )
    
    # Create intensity mask (darker base)
    intensity = np.sin(r/10 + t) * 0.5 + 0.5
    intensity = np.power(intensity, 2.5)  # Make it darker

    h_ = v
    s_ = np.ones_like(v)
    v_ = intensity  # Use intensity instead of full brightness

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

frames[0].save("dark_01_neon_ripples.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# DARK VARIATION 2: SPIRAL VORTEX
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
    
    # Dark spiral vortex
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        theta * 2.5 +
        np.sin(r/10 - theta*4 + t) * 1.5,
        1.0
    )
    
    # Dark intensity with bright centers
    intensity = 1.0 / (1.0 + r/80)
    intensity = np.power(intensity, 1.8)

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

frames[0].save("dark_02_spiral_vortex.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# DARK VARIATION 3: ELECTRIC MANDALA
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
    
    # Dark electric mandala
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(theta * 12) * 0.8 +
        np.cos(r/6 + theta * 6 - t*2) * 1.2,
        1.0
    )
    
    # Pulsing intensity
    intensity = np.abs(np.sin(theta * 12)) * 0.6 + 0.2
    intensity = intensity * (np.sin(r/15 + t) * 0.3 + 0.4)

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

frames[0].save("dark_03_electric_mandala.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# DARK VARIATION 4: PLASMA WAVES
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

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Dark plasma waves
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(x/15 + t*2) * 1.8 +
        np.cos(y/15 - t*1.8) * 1.8,
        1.0
    )
    
    # Plasma intensity
    intensity = np.sin(x/20 + t) * np.cos(y/20 - t) * 0.35 + 0.35
    intensity = np.power(intensity, 2.0)

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

frames[0].save("dark_04_plasma_waves.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# DARK VARIATION 5: COSMIC EYE
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
    
    # Dark cosmic eye
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        theta * 4 * np.cos(t*0.5) +
        np.sin(r/12 - theta*3 + t*2) * 1.8,
        1.0
    )
    
    # Eye-like intensity
    intensity = np.exp(-r/120) * 0.9 + np.sin(r/8 + t) * 0.15 + 0.1
    intensity = np.clip(intensity, 0, 1)

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

frames[0].save("dark_05_cosmic_eye.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# DARK VARIATION 6: FRACTAL FLOWER
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
    
    # Dark fractal flower
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(theta * 16) * 1.5 +
        np.sin(r/5 + theta*8 - t*2.5) * 1.2,
        1.0
    )
    
    # Petal intensity
    intensity = np.abs(np.sin(theta * 8)) * 0.7 + 0.15
    intensity = intensity * (1.0 / (1.0 + r/100))

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

frames[0].save("dark_06_fractal_flower.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# DARK VARIATION 7: QUANTUM FIELD
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

for i in range(num_frames):
    t = i / num_frames * 4 * pi
    
    # Dark quantum field
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(r/4 + t*3) * np.cos(r/16 - t) * 2.5,
        1.0
    )
    
    # Quantum glow
    intensity = np.sin(r/5 + t*2) * 0.3 + 0.2
    intensity = intensity * np.exp(-r/200)
    intensity = np.clip(intensity, 0, 1)

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

frames[0].save("dark_07_quantum_field.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# DARK VARIATION 8: STARBURST
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
    
    # Dark starburst
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(theta * 24) * 0.8 +
        np.cos(r/7 - t*2) * 1.5,
        1.0
    )
    
    # Radial glow
    intensity = np.abs(np.sin(theta * 12)) * (1.0 / (1.0 + r/60))
    intensity = np.power(intensity, 1.5)

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

frames[0].save("dark_08_starburst.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# DARK VARIATION 9: HYPNOTIC TUNNEL
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
    
    # Dark hypnotic tunnel
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.log1p(r/40) * 4.0 * np.sin(t) +
        theta * 1.5,
        1.0
    )
    
    # Tunnel depth
    intensity = 1.0 / (1.0 + np.power(r/100, 2))
    intensity = intensity * (np.sin(r/10 - t) * 0.3 + 0.5)

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

frames[0].save("dark_09_hypnotic_tunnel.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# DARK VARIATION 10: NEBULA WEB
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
    
    # Dark nebula web
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(theta * 9 + r/12 + t*1.5) * 1.4 +
        np.cos(theta * 15 - r/18 - t) * 0.9,
        1.0
    )
    
    # Nebula glow
    intensity = np.sin(theta * 9 + t) * 0.25 + 0.25
    intensity = intensity * np.exp(-r/150) + 0.05

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

frames[0].save("dark_10_nebula_web.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)

print("All 10 dark psychedelic variations complete! 🌌✨")
