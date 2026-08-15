from story_svg import build_story_svg

STAGES = [
    {
        "depth": "STAGE 01",
        "eyebrow": "出会う",
        "title": "採用は、出会いから始まる。",
        "lead": "企業と求職者は、まだお互いのことが見えていない。輪郭だけの状態から、支援は始まります。",
        "tags": ["採用戦略設計", "求人・採用広報", "面接設計", "面接官研修"],
    },
    {
        "depth": "STAGE 02",
        "eyebrow": "選び合う",
        "title": "採るのではなく、選び合う。",
        "lead": "価値観、仕事、将来像。企業と求職者のあいだに、確かな光の線をつなぎます。",
        "tags": ["採用基準の明確化", "ミスマッチの防止", "候補者体験の改善", "自社に合う人材の見極め"],
    },
    {
        "depth": "STAGE 03",
        "eyebrow": "迎え入れる",
        "title": "入社は、ゴールではない。",
        "lead": "採用された人の周りに、先輩・上司・同期が現れる。ここからが、本当のスタートです。",
        "tags": ["オンボーディング設計", "入社後90日支援", "受け入れ体制づくり", "ノビナジ"],
    },
    {
        "depth": "STAGE 04",
        "eyebrow": "つながる",
        "title": "人は、関係性の中で定着する。",
        "lead": "孤立させない。上司や仲間との線を増やし、早期離職のサインを見逃さない仕組みをつくります。",
        "tags": ["1on1", "サーベイ", "上司との関係構築", "早期離職アラート", "定着面談"],
    },
    {
        "depth": "STAGE 05",
        "eyebrow": "成長する",
        "title": "定着の先に、活躍がある。",
        "lead": "姿勢が変わり、自ら動き始める。その光は、まわりの人にも広がっていく。",
        "tags": ["新入社員研修", "リーダー育成", "管理職研修", "人事制度設計", "組織開発"],
    },
]

FINAL = {
    "depth": "STAGE 06",
    "eyebrow": "組織になる",
    "title": "一人の可能性が、組織を動かす。",
    "lead": "採用して終わりではない。人が定着し、成長し、活躍するところまで。ヒトイクは、人と組織の可能性を動かします。",
}


LINKED_STAGES = {1, 2, 3, 4}


def _panel(i, s, extra_class=""):
    linkable = i in LINKED_STAGES
    tags = "".join(
        f'<span{f" class=\"linkable\" data-link=\"{idx}\"" if linkable else ""}>{t}</span>'
        for idx, t in enumerate(s["tags"])
    )
    return f"""
    <div class="story-panel {extra_class}" data-stage="{i}">
      <div class="story-panel-inner">
        <div class="story-num">{s['depth']}</div>
        <div class="story-eyebrow">{s['eyebrow']}</div>
        <h2>{s['title']}</h2>
        <p class="lead">{s['lead']}</p>
        <div class="story-tags">{tags}</div>
      </div>
    </div>
    """


def _final_panel():
    return f"""
    <div class="story-panel final" data-stage="5">
      <div class="story-panel-inner">
        <div class="story-num">{FINAL['depth']}</div>
        <div class="story-eyebrow">{FINAL['eyebrow']}</div>
        <h2>{FINAL['title']}</h2>
        <p class="lead">{FINAL['lead']}</p>
        <a href="contact.html" class="btn btn-primary">採用・定着について相談する</a>
      </div>
    </div>
    """


LOGO_URL = "images/logo.png"


def _typewriter_lines(lines, start_delay=0.0, step=0.055):
    """Wrap each character in its own span with an incrementing transition-delay,
    so the tagline reveals one character at a time."""
    out = []
    delay = start_delay
    for li, line in enumerate(lines):
        if li > 0:
            out.append("<br>")
        for ch in line:
            out.append(f'<span class="ch" style="transition-delay:{delay:.3f}s">{ch}</span>')
            delay += step
    return "".join(out)


TAGLINE_HTML = _typewriter_lines(["人の可能性が、", "動き出す瞬間を。"])

INTRO_HTML = f"""
<div class="intro-splash" id="introSplash">
  <div class="intro-stage intro-logo-stage" id="introLogoStage">
    <img src="{LOGO_URL}" alt="ヒトイク" class="intro-logo-img"
         onerror="this.style.display='none';this.nextElementSibling.style.display='flex';">
    <div class="intro-logo-fallback" style="display:none;"><span class="mark"></span><span>ヒトイク</span></div>
  </div>
  <div class="intro-stage intro-tagline-stage" id="introTaglineStage">
    <p class="intro-tagline">{TAGLINE_HTML}</p>
  </div>
  <button class="intro-skip" id="introSkip" type="button">スキップ</button>
</div>
<script>
(function () {{
  var splash = document.getElementById('introSplash');
  if (!splash) return;
  var logoStage = document.getElementById('introLogoStage');
  var taglineStage = document.getElementById('introTaglineStage');
  var skipBtn = document.getElementById('introSkip');
  var done = false;
  var timers = [];

  function finish() {{
    if (done) return;
    done = true;
    timers.forEach(function (t) {{ clearTimeout(t); }});
    splash.classList.add('hidden');
    document.body.style.overflow = '';
  }}

  document.body.style.overflow = 'hidden';
  timers.push(setTimeout(function () {{ logoStage.classList.add('show'); }}, 100));
  timers.push(setTimeout(function () {{ logoStage.classList.remove('show'); }}, 3000));
  timers.push(setTimeout(function () {{ taglineStage.classList.add('show'); }}, 3700));
  timers.push(setTimeout(function () {{ taglineStage.classList.remove('show'); }}, 7000));
  timers.push(setTimeout(finish, 8600));

  splash.addEventListener('click', finish);
  skipBtn.addEventListener('click', function (e) {{ e.stopPropagation(); finish(); }});
}})();
</script>
"""


def build_story_section():
    panels = "".join(_panel(i, s) for i, s in enumerate(STAGES)) + _final_panel()
    dots = "".join(f'<span class="{"on" if i == 0 else ""}"></span>' for i in range(6))
    svg = build_story_svg()
    return f"""
{INTRO_HTML}
<section class="story-scroll" id="story" data-active="0">
  <div class="story-visual">
    <div class="story-bg"></div>
    <span class="story-depth">HITOIKU STORY — <b>採用から、活躍まで。</b></span>
    <svg class="story-svg" viewBox="0 0 800 800" xmlns="http://www.w3.org/2000/svg">{svg}</svg>
    <div class="story-progress">{dots}</div>
  </div>
  <div class="story-panels">{panels}</div>
</section>
<div class="story-skip"><a href="#after-story">↓ サービス一覧を見る</a></div>
"""
