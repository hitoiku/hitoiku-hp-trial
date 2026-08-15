import os

ROOT = os.path.dirname(os.path.abspath(__file__))

HEAD_TOP = """<!doctype html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22><rect width=%2232%22 height=%2232%22 rx=%229%22 fill=%22%230E7C6E%22/><path d=%22M9 17l5 5 9-11%22 stroke=%22white%22 stroke-width=%223%22 fill=%22none%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22/></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@500;700;900&family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/styles.css">
<noscript><style>
.reveal{{opacity:1 !important; transform:none !important;}}
.story-visual{{display:none;}}
.story-scroll{{height:auto !important; padding:60px 0;}}
.story-panels{{position:static !important;}}
.story-panel{{height:auto !important; position:static !important; padding:26px 8vw !important; justify-content:flex-start !important; text-align:left !important;}}
.story-panel-inner{{opacity:1 !important; transform:none !important; max-width:640px !important;}}
.story-tags{{justify-content:flex-start !important;}}
.story-skip{{display:none;}}
</style></noscript>
</head>
<body>
"""

def header(active):
    def cls(key):
        return " active" if active == key else ""
    return f"""<header class="site-header">
  <div class="header-inner">
    <a href="index.html" class="logo"><img src="images/logo.png" alt="ヒトイク" class="logo-img" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="eager"><span class="logo-fallback" style="display:none;"><span class="mark"></span><span>ヒトイク<small>UPDATE HUMAN</small></span></span></a>
    <nav class="main-nav">
      <ul>
        <li><a class="nav-link{cls('home')}" href="index.html">ホーム</a></li>
        <li class="has-dropdown">
          <a class="nav-link{cls('service')}" href="recruiting.html">サービス</a>
          <ul class="dropdown">
            <li><a href="recruiting.html">採用コンサルティング<span>採用の仕組みをつくる</span></a></li>
            <li><a href="training.html">研修・人材育成<span>行動が変わる研修</span></a></li>
            <li><a href="hr-system.html">人事制度・組織開発<span>定着と成長を支える制度</span></a></li>
          </ul>
        </li>
        <li><a class="nav-link{cls('works')}" href="works.html">支援事例</a></li>
        <li><a class="nav-link{cls('message')}" href="message.html">代表紹介</a></li>
        <li><a class="nav-link{cls('faq')}" href="faq.html">よくある質問</a></li>
        <li><a class="nav-link{cls('contact')}" href="contact.html">お問い合わせ</a></li>
      </ul>
    </nav>
    <div class="header-cta">
      <a href="contact.html" class="btn btn-primary btn-sm">無料相談を予約</a>
      <button class="nav-toggle" aria-label="メニュー"><span></span></button>
    </div>
  </div>
</header>
"""

FOOTER = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="logo"><img src="images/logo.png" alt="ヒトイク" class="logo-img" onerror="this.style.display='none';this.nextElementSibling.style.display='flex';" loading="lazy"><span class="logo-fallback" style="display:none;"><span class="mark"></span><span>ヒトイク</span></span></a>
        <p>採用を入口に、定着・育成・組織づくりまで伴走する。人と組織の可能性が動き出す瞬間をつくります。</p>
      </div>
      <div>
        <h4>サービス</h4>
        <ul>
          <li><a href="recruiting.html">採用コンサルティング</a></li>
          <li><a href="training.html">研修・人材育成</a></li>
          <li><a href="hr-system.html">人事制度・組織開発</a></li>
        </ul>
      </div>
      <div>
        <h4>会社情報</h4>
        <ul>
          <li><a href="works.html">支援事例</a></li>
          <li><a href="message.html">代表紹介</a></li>
          <li><a href="faq.html">よくある質問</a></li>
          <li><a href="privacy.html">プライバシーポリシー</a></li>
        </ul>
      </div>
      <div>
        <h4>お問い合わせ</h4>
        <ul>
          <li><a href="contact.html">お問い合わせフォーム</a></li>
          <li><a href="mailto:hitoiku0110@gmail.com">hitoiku0110@gmail.com</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2024 Hitoiku. All rights reserved.</span>
      <span>愛知県名古屋市中村区名駅4丁目24番5号 第2森ビル401 / Est. 2024.1.10</span>
    </div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""

def page(filename, title, desc, active, content, extra_css=None, extra_js=None):
    head = HEAD_TOP.format(title=title, desc=desc)
    if extra_css:
        head = head.replace("</head>", f'<link rel="stylesheet" href="{extra_css}">\n</head>')
    footer = FOOTER
    if extra_js:
        footer = footer.replace('<script src="js/main.js"></script>',
                                 f'<script src="js/main.js"></script>\n<script src="{extra_js}"></script>')
    html = head + header(active) + content + footer
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)
