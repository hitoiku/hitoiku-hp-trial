from icons import icon
from content_story import INTRO_HTML

STATIC_HERO = f"""
{INTRO_HTML}
<section class="hero-v2">
  <div class="hero-v2-media-full" id="heroMediaFrame">
    <div class="hero-v2-slide hero-v2-slide-logo is-active">
      <img src="images/logo.png" alt="ヒトイク" class="hero-v2-logo-img" loading="eager">
    </div>
    <div class="hero-v2-slide hero-v2-slide-photo">
      <img src="images/hero.png" alt="人の可能性が、動き出す瞬間を。" loading="eager" width="1672" height="941">
    </div>
    <div class="hero-v2-slide hero-v2-slide-nursing">
      <img src="images/case-rooftop.jpg" alt="人の可能性が、動き出す瞬間を。" loading="lazy">
    </div>
  </div>
  <div class="container hero-v2-content">
    <div class="hero-v2-inner">
      <h1 class="hero-v2-title">人の可能性が、<br>動き出す瞬間を。</h1>
    </div>
  </div>
  <a href="#after-story" class="hero-v2-scroll" aria-label="スクロールして次のセクションへ">
    <span>Scroll</span>
    {icon('arrow-down')}
  </a>
</section>
<script>
(function () {{
  var frame = document.getElementById('heroMediaFrame');
  if (!frame) return;
  var slides = Array.prototype.slice.call(frame.querySelectorAll('.hero-v2-slide'));
  if (slides.length < 2) return;
  var reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var idx = 0;
  var fired = false;
  function show(i) {{
    slides.forEach(function (s, si) {{ s.classList.toggle('is-active', si === i); }});
  }}
  function next() {{
    idx = (idx + 1) % slides.length;
    show(idx);
    setTimeout(next, 4000); /* slide every 4s */
  }}
  function start() {{
    if (fired) return;
    fired = true;
    if (reduced) {{ show(slides.length - 1); return; }}
    setTimeout(next, 4000);
  }}
  document.addEventListener('hitoiku:introDone', start);
  setTimeout(start, 6000); /* fallback if the intro splash is skipped/absent */
}})();
</script>
"""

CONTENT = f"""
{STATIC_HERO}

<section id="after-story" class="about-teaser">
  <div class="about-teaser-shapes" aria-hidden="true">
    <span class="shape shape-a"></span>
    <span class="shape shape-b"></span>
  </div>
  <div class="container about-teaser-inner reveal">
    <p class="about-teaser-statement">私たちは、まだ見えていない可能性を<br class="teaser-break-sm">信じ、<br>人が変わるきっかけをつくる会社です。</p>
    <a href="about.html" class="about-teaser-link">
      <span class="about-teaser-circle">{icon('arrow-right')}</span>
      <span>Hitoikuをもっと知る</span>
    </a>
  </div>
</section>

<section class="services-band">
  <div class="services-panel">
    <div class="container">
      <div class="section-head section-head-title-only">
        <span class="eyebrow eyebrow-lg slide-in-left">Our Services</span>
      </div>
      <div class="service-list">
        <a href="recruiting.html" class="service-list-item slide-in-left">
          <div class="service-list-icon"><img src="images/service-icon-recruiting.png" alt="" loading="lazy"></div>
          <div class="service-list-body">
            <h3>採用コンサルティング</h3>
          </div>
          <span class="service-list-arrow">{icon('arrow-right')}</span>
        </a>
        <a href="training.html" class="service-list-item slide-in-left">
          <div class="service-list-icon"><img src="images/service-icon-training.png" alt="" loading="lazy"></div>
          <div class="service-list-body">
            <h3>研修・人材育成</h3>
          </div>
          <span class="service-list-arrow">{icon('arrow-right')}</span>
        </a>
        <a href="hr-system.html" class="service-list-item slide-in-left">
          <div class="service-list-icon"><img src="images/service-icon-hrsystem.png" alt="" loading="lazy"></div>
          <div class="service-list-body">
            <h3>人事制度・組織開発</h3>
          </div>
          <span class="service-list-arrow">{icon('arrow-right')}</span>
        </a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="company-deck reveal">
      <div class="company-deck-text">
        <h2><span class="nowrap">Hitoikuを、</span><br><span class="nowrap">もっと知る。</span></h2>
      </div>
      <a href="contact.html" class="company-deck-media">
        <img src="images/company-deck.jpg" alt="Hitoiku 会社紹介" loading="lazy">
        <span class="company-deck-link">
          <span class="company-deck-play">{icon('play')}</span>
          <span>会社資料をみる</span>
          {icon('arrow-right')}
        </span>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <a href="contact.html" class="contact-band">
      <div class="contact-band-main">
        <span class="contact-band-title">Contact</span>
      </div>
      <p class="contact-band-desc">これからの組織の話を、はじめませんか。</p>
      <span class="contact-band-circle">{icon('arrow-right')}</span>
    </a>
  </div>
</section>
"""
