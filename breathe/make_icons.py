#!/usr/bin/env python3
"""Generate app icons for 'breathe, as you wish' using only the stdlib.

Draws a still zen pond: an ink field with a soft sage color front and a faint
contained glow — a calm snapshot of the breathing screen mid-inhale.
"""
import math
import struct
import zlib


def smoothstep(e0, e1, x):
    if e1 == e0:
        return 0.0 if x < e0 else 1.0
    t = max(0.0, min(1.0, (x - e0) / (e1 - e0)))
    return t * t * (3 - 2 * t)


def lerp(a, b, t):
    return a + (b - a) * t


def make_png(size, path, maskable=False):
    # palette
    bg = (24, 26, 22)            # #181A16 sage night bg
    fill = (104, 144, 114)       # sage fill
    edge = (185, 214, 190)       # sage edge
    glow = (107, 143, 113)

    cx = cy = size / 2.0
    Rdisp = size * (0.42 if maskable else 0.36)
    pondR = Rdisp * 0.95
    feather = pondR * 0.17
    front = pondR * 0.62          # mid-inhale snapshot

    rows = bytearray()
    for y in range(size):
        rows.append(0)  # filter type 0
        for x in range(size):
            dx = x + 0.5 - cx
            dy = y + 0.5 - cy
            r = math.hypot(dx, dy)

            # base: ink with a soft contained glow
            gd = max(0.0, 1.0 - r / (Rdisp * 1.28))
            gd = gd * gd
            cr = lerp(bg[0], glow[0], gd * 0.30)
            cg = lerp(bg[1], glow[1], gd * 0.30)
            cb = lerp(bg[2], glow[2], gd * 0.30)

            if r <= pondR:
                fillv = 1.0 - smoothstep(front - feather, front + feather, r)
                lead = math.exp(-((r - front) / (feather * 0.95)) ** 2) * 0.8
                rim = 1.0 - smoothstep(pondR * 0.80, pondR, r)
                lead_c = min(1.0, lead)
                fr = lerp(fill[0], edge[0], lead_c)
                fg = lerp(fill[1], edge[1], lead_c)
                fb = lerp(fill[2], edge[2], lead_c)
                a = min(1.0, fillv * 0.85 + lead * 0.5) * rim
                cr = lerp(cr, fr, a)
                cg = lerp(cg, fg, a)
                cb = lerp(cb, fb, a)

            rows.extend((int(cr), int(cg), int(cb), 255))

    raw = zlib.compress(bytes(rows), 9)

    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", raw) + chunk(b"IEND", b"")
    with open(path, "wb") as f:
        f.write(png)
    print("wrote", path, size)


make_png(180, "icon-180.png")
make_png(192, "icon-192.png")
make_png(512, "icon-512.png")
make_png(512, "icon-maskable.png", maskable=True)
