# ========================================
# 10 NEW PSYCHEDELIC VARIATIONS
# All based on π×e scaling with unique mathematical twists
# ========================================

# ========================================
# VARIATION 9: KALEIDOSCOPE FLOWER
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
    
    # Kaleidoscope flower
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(theta * 16) * 1.2 +
        np.cos(r/6 - theta * 8 + t*2) * 0.8,
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

frames[0].save("psychedelic_09_kaleidoscope_flower.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 10: QUANTUM RIPPLE
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
    
    # Quantum ripple
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(r/4 + t*3) * np.cos(r/16 - t) * 2.0,
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

frames[0].save("psychedelic_10_quantum_ripple.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 11: HYPNOTIC VORTEX
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
    
    # Hypnotic vortex
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        theta * 3 * np.sin(t) +
        np.cos(r/7 + theta*5 - t*2) * 1.5,
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

frames[0].save("psychedelic_11_hypnotic_vortex.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 12: PLASMA FIELD
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
    
    # Plasma field
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(x/20 + t*2) * 1.5 +
        np.cos(y/20 - t*1.5) * 1.5,
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

frames[0].save("psychedelic_12_plasma_field.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 13: FRACTAL BURST
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
    
    # Fractal burst
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(r/3) * np.sin(theta * 10 + t) * 1.8,
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

frames[0].save("psychedelic_13_fractal_burst.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 14: COSMIC WEB
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
    
    # Cosmic web
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(theta * 7 + r/15 + t) * 1.3 +
        np.cos(theta * 11 - r/20 - t*1.5) * 0.9,
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

frames[0].save("psychedelic_14_cosmic_web.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 15: BREATHING RINGS
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
    
    # Breathing rings
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        r * 0.1 * np.sin(t*3) +
        np.cos(r/10 + t*2) * 2.5,
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

frames[0].save("psychedelic_15_breathing_rings.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 16: ELECTRIC LOTUS
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
    
    # Electric lotus
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(theta * 20) * 0.6 +
        np.sin(r/5 + theta*10 + t*2.5) * 1.4,
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

frames[0].save("psychedelic_16_electric_lotus.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 17: TIME WARP
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
    
    # Time warp
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.power(r/100, 1.5) * np.sin(theta*6 + t*2) * 5.0,
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

frames[0].save("psychedelic_17_time_warp.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)


# ========================================
# VARIATION 18: NEURAL NETWORK
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
    
    # Neural network
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.tanh(r/30 - 5) * np.sin(theta*9 + t) * 3.0 +
        np.cos(r/12 + t*1.8) * 1.2,
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

frames[0].save("psychedelic_18_neural_network.gif", save_all=True, append_images=frames[1:], duration=50, loop=0)

print("All 10 new psychedelic variations complete! 🌈🔥")
