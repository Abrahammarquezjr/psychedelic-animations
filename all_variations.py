# ========================================
# VARIATION 1: DOUBLE WAVE INTERFERENCE
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
    
    # Double wave interference
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 + 
        np.cos(r/12 - t*1.5) * 1.5,
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

frames[0].save(
    "pi_e_double_wave.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0
)


# ========================================
# VARIATION 2: ANGULAR MODULATION
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
    
    # Angular modulation
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(theta * 8 + t * 2) * 0.8,
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

frames[0].save(
    "pi_e_angular_mod.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0
)


# ========================================
# VARIATION 3: GOLDEN RATIO (PHI)
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
    
    # Fibonacci-inspired scaling
    phi = (1 + np.sqrt(5)) / 2
    v = np.mod(
        r * pi * e / phi + 
        np.sin(r/8 + t) * 2.0 +
        np.cos(r/15 + t * phi) * 1.2,
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

frames[0].save(
    "pi_e_phi_golden.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0
)


# ========================================
# VARIATION 4: TURBULENT RIPPLES
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
    
    # Turbulent ripples
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(r/5 + t*2.5) * 1.2 +
        np.cos(r/20 - t*0.8) * 0.7,
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

frames[0].save(
    "pi_e_turbulent.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0
)


# ========================================
# VARIATION 5: SPIRAL WAVE HYBRID
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
    
    # Spiral wave hybrid
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        theta * 1.5 +
        np.sin(r/10 - theta*3 + t) * 1.0,
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

frames[0].save(
    "pi_e_spiral_wave.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0
)


# ========================================
# VARIATION 6: FAST PULSE
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
    
    # Faster oscillation
    v = np.mod(
        r * pi * e + 
        np.sin(r/6 + t*2) * 3.0 +
        np.sin(r/11 - t*1.3) * 1.8,
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

frames[0].save(
    "pi_e_fast_pulse.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0
)


# ========================================
# VARIATION 7: LOGARITHMIC MODULATION
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
    
    # Logarithmic modulation
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.log1p(r/50) * 3.0 * np.sin(t*2),
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

frames[0].save(
    "pi_e_logarithmic.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0
)


# ========================================
# VARIATION 8: MANDALA STYLE
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
    
    # Mandala-style with rotational symmetry
    v = np.mod(
        r * pi * e + 
        np.sin(r/8 + t) * 2.0 +
        np.sin(theta * 12) * 0.5 +
        np.cos(r/10 + theta * 6 - t) * 1.0,
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

frames[0].save(
    "pi_e_mandala.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,
    loop=0
)

print("All 8 variations complete! 🔥")
