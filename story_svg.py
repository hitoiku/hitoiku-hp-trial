import math

# Bright, optimistic palette (readable on the light "dawn -> sunrise" backgrounds)
TEAL_DEEP = "#0E7C6E"
TEAL = "#12A594"
TEAL_SOFT = "#4FB3A3"
CORAL = "#FF6B45"
CORAL_SOFT = "#FF9466"
GOLD = "#D98C2B"


def _person_shape(pose):
    head = '<circle cx="0" cy="-38" r="14.5" fill="currentColor"/>'
    body = ('<path d="M-28,23 C-28,-10 -15.5,-24 0,-24 C15.5,-24 28,-10 28,23 '
            'C28,37 -28,37 -28,23 Z" fill="currentColor"/>')
    arms = ""
    if pose == "up":  # confident / growing -- arms raised open
        arms = (
            '<path d="M-15,-4 C-30,-16 -34,-34 -25,-46" fill="none" stroke="currentColor" '
            'stroke-width="10" stroke-linecap="round"/>'
            '<path d="M15,-4 C30,-16 34,-34 25,-46" fill="none" stroke="currentColor" '
            'stroke-width="10" stroke-linecap="round"/>'
        )
    return body, arms, head


def person(cx, cy, scale=1.0, pose="stand", color=TEAL, glow=False, opacity=1, delay=0, link=None):
    """A friendly, rounded human silhouette (head + shoulders bust), not a stick figure."""
    link_attr = f' data-link="{link}"' if link is not None else ""
    body, arms, head = _person_shape(pose)
    # NOTE: the transform and the CSS drop-shadow filter must live on separate
    # elements -- Chromium mis-renders the position when both are on the same
    # SVG element (filter is applied on the inner, transform-free group).
    inner_cls = "fig-glow" if glow else ""
    inner = f'<g class="{inner_cls}">{body}{arms}{head}</g>'
    return (f'<g class="fig" transform="translate({cx},{cy}) scale({scale})" '
            f'style="color:{color};--o:{opacity};transition-delay:{delay}s"{link_attr}>{inner}</g>')


def person_gather(ex, ey, escale, sx, sy, sscale, pose="stand", color=TEAL,
                   glow=False, opacity=1, delay=0, link=None):
    """Like person(), but arrives by sliding in from (sx,sy) to (ex,ey) when its
    stage becomes active -- used for a 'people gathering' entrance. Position is
    driven entirely through CSS custom properties (never mixed with the SVG
    presentational transform attribute, and transform-box/origin pinned to
    (0,0) of the view-box) to avoid the Chromium mis-render bug documented in
    person()."""
    link_attr = f' data-link="{link}"' if link is not None else ""
    body, arms, head = _person_shape(pose)
    inner_cls = "fig-glow" if glow else ""
    inner = f'<g class="{inner_cls}">{body}{arms}{head}</g>'
    style = (
        f'color:{color};--o:{opacity};transition-delay:{delay}s;'
        f'--sx:{sx}px;--sy:{sy}px;--s0:{sscale};'
        f'--ex:{ex}px;--ey:{ey}px;--s1:{escale};'
        f'transform-box:view-box;transform-origin:0 0;'
    )
    return f'<g class="fig gather" style="{style}"{link_attr}>{inner}</g>'


def line(x1, y1, x2, y2, color=TEAL, draw=True, sw=2.4, dashed=False, delay=0, link=None):
    cls = "ln line-draw" if draw else "ln"
    dash = 'stroke-dasharray="6 7"' if dashed else ""
    link_attr = f' data-link="{link}"' if link is not None else ""
    return (f'<path class="{cls}" d="M{x1},{y1} L{x2},{y2}" stroke="{color}" '
            f'stroke-width="{sw}" fill="none" stroke-linecap="round" {dash} '
            f'style="--o:1;transition-delay:{delay}s"{link_attr}/>')


def curve(x1, y1, cx, cy, x2, y2, color=TEAL, sw=2.4, delay=0, link=None):
    link_attr = f' data-link="{link}"' if link is not None else ""
    return (f'<path class="ln line-draw" d="M{x1},{y1} Q{cx},{cy} {x2},{y2}" '
            f'stroke="{color}" stroke-width="{sw}" fill="none" stroke-linecap="round" '
            f'style="--o:1;transition-delay:{delay}s"{link_attr}/>')


def dot(cx, cy, r=5, color=CORAL, pulse=False, delay=0, link=None):
    cls = "pulse" if pulse else "spark"
    link_attr = f' data-link="{link}"' if link is not None else ""
    return (f'<g class="dot-wrap" style="--o:1;transition-delay:{delay}s"{link_attr}>'
            f'<circle class="{cls}" cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/></g>')


def stage_group(n, inner):
    return f'<g class="st" data-stage="{n}">{inner}</g>'


def build_story_svg():
    parts = []

    # ---- Stage 0: 出会う -- two figures approaching from afar ----
    s0 = (
        person(160, 460, scale=1.05, pose="stand", color=CORAL_SOFT, opacity=.9, delay=0) +
        person(640, 460, scale=1.05, pose="stand", color=TEAL_SOFT, opacity=.9, delay=.12) +
        line(232, 460, 322, 460, color=TEAL, sw=1.8, dashed=True, delay=.3) +
        line(478, 460, 568, 460, color=TEAL, sw=1.8, dashed=True, delay=.42)
    )
    parts.append(stage_group(0, s0))

    # ---- Stage 1: 選び合う -- each value marker lines up with a tag in the text ----
    # 4 tags: 採用基準の明確化(0) / ミスマッチの防止(1) / 候補者体験の改善(2) / 自社に合う人材の見極め(3)
    s1 = (
        person(230, 460, scale=1.1, pose="stand", color=CORAL, opacity=1, delay=0) +
        person(570, 460, scale=1.1, pose="stand", color=TEAL_DEEP, opacity=1, delay=.1) +
        line(292, 442, 508, 442, color=TEAL, sw=2.6, delay=.2) +
        dot(338, 442, 5, GOLD, True, delay=.35, link=0) +
        dot(380, 442, 5, TEAL, True, delay=.5, link=1) +
        dot(420, 442, 5, CORAL, True, delay=.65, link=2) +
        dot(462, 442, 5, TEAL_DEEP, True, delay=.8, link=3)
    )
    parts.append(stage_group(1, s1))

    # ---- Stage 2: 迎え入れる -- people arrive and gather around the new hire ----
    # tags: オンボーディング設計(0) / 入社後90日支援(1) / 受け入れ体制づくり(2) / ノビナジ(3)
    s2 = (
        line(280, 250, 280, 560, color="rgba(14,124,110,.16)", sw=2, draw=False, delay=0, link=2) +
        line(280, 250, 520, 250, color="rgba(14,124,110,.16)", sw=2, draw=False, delay=0, link=2) +
        line(520, 250, 520, 560, color="rgba(14,124,110,.16)", sw=2, draw=False, delay=0, link=2) +
        person_gather(400, 470, 1.3, 400, 660, 0.85, pose="stand", color=CORAL,
                      glow=True, opacity=1, delay=0) +
        person_gather(290, 540, 0.68, 130, 660, 0.4, pose="stand", color=TEAL_SOFT,
                      opacity=.9, delay=.35, link=0) +
        person_gather(510, 540, 0.68, 670, 660, 0.4, pose="stand", color=TEAL_SOFT,
                      opacity=.9, delay=.5, link=1) +
        person_gather(400, 300, 0.68, 400, 110, 0.4, pose="stand", color=TEAL_SOFT,
                      opacity=.85, delay=.65, link=3) +
        curve(305, 520, 350, 488, 395, 448, color=TEAL, sw=2.2, delay=1.5, link=0) +
        curve(495, 520, 450, 488, 405, 448, color=TEAL, sw=2.2, delay=1.65, link=1) +
        curve(400, 325, 400, 368, 400, 420, color=TEAL, sw=2.2, delay=1.8, link=3) +
        dot(400, 440, 6, GOLD, True, delay=1.95, link=2)
    )
    parts.append(stage_group(2, s2))

    # ---- Stage 3: つながる -- relationship lines radiate to colleagues ----
    # tags: 1on1(0) / サーベイ(1) / 上司との関係構築(2) / 早期離職アラート(3) / 定着面談(4)
    s3 = (
        person(400, 470, scale=1.3, pose="stand", color=CORAL, glow=True, delay=0) +
        person(290, 540, scale=0.68, pose="stand", color=TEAL, opacity=.95, delay=.15, link=2) +
        person(510, 540, scale=0.68, pose="stand", color=TEAL, opacity=.95, delay=.3, link=0) +
        person(400, 300, scale=0.68, pose="stand", color=TEAL, opacity=.95, delay=.45, link=4) +
        curve(400, 445, 350, 485, 300, 522, color=TEAL, sw=2, delay=.2, link=2) +
        curve(400, 445, 450, 485, 500, 522, color=TEAL, sw=2, delay=.35, link=0) +
        curve(400, 425, 400, 365, 400, 325, color=TEAL, sw=2, delay=.5, link=4) +
        dot(400, 400, 6, CORAL, True, delay=.65, link=3)
    )
    parts.append(stage_group(3, s3))

    # ---- Stage 4: 成長する -- pose changes to confident, light spreads ----
    # tags: 新入社員研修(0) / リーダー育成(1) / 管理職研修(2) / 人事制度設計(3) / 組織開発(4)
    s4 = (
        person(400, 460, scale=1.5, pose="up", color=CORAL, glow=True, delay=0, link=1) +
        person(260, 560, scale=0.72, pose="stand", color=CORAL_SOFT, glow=True, opacity=.95, delay=.18, link=0) +
        person(540, 560, scale=0.72, pose="stand", color=TEAL, glow=True, opacity=.95, delay=.32, link=2) +
        person(400, 280, scale=0.72, pose="stand", color=TEAL, glow=True, opacity=.95, delay=.46, link=3) +
        dot(400, 195, 4, GOLD, delay=.6, link=4) + dot(220, 380, 4, TEAL, delay=.66, link=4) +
        dot(580, 380, 4, TEAL, delay=.72, link=4) +
        dot(300, 625, 4, CORAL_SOFT, delay=.78, link=4) + dot(500, 625, 4, CORAL_SOFT, delay=.84, link=4)
    )
    parts.append(stage_group(4, s4))

    # ---- Stage 5: 組織になる -- network of many figures, org-wide light ----
    crowd = []
    cx, cy, R = 400, 440, 210
    n = 9
    palette = [TEAL, CORAL_SOFT, TEAL_SOFT]
    for i in range(n):
        ang = (2 * math.pi / n) * i - math.pi / 2
        px = cx + R * math.cos(ang)
        py = cy + R * math.sin(ang) * 0.62
        d = .12 + i * .06
        crowd.append(curve(cx, cy - 10, (cx + px) / 2, (cy + py) / 2 - 10, px, py,
                            color="rgba(14,124,110,.35)", sw=1.6, delay=d))
        crowd.append(person(px, py, scale=0.56, pose="stand", color=palette[i % 3],
                             glow=(i % 3 == 0), opacity=.95, delay=d + .05))
    sparkles = "".join(dot(cx + (i * 53) % 460 - 230, cy + (i * 37) % 260 - 130, 3, GOLD, delay=.8 + i * .03)
                        for i in range(14))
    s5 = "".join(crowd) + person(cx, cy, scale=1.35, pose="up", color=CORAL, glow=True, delay=0) + sparkles
    parts.append(stage_group(5, s5))

    return "".join(parts)
