from icons import icon
from content_story import INTRO_HTML

STATIC_HERO = f"""
{INTRO_HTML}
<section class="static-hero">
  <div class="static-hero-media">
    <img src="images/hero.jpg" alt="採用して終わりではない。人が定着し、成長し、活躍するところまで。"
         width="1536" height="1024">
  </div>
  <div class="static-hero-text">
    <h1>採用して終わりではない。<br>人が定着し、成長し、<br>活躍するところまで。</h1>
    <p>ヒトイクは、採用から定着・活躍までを支援する採用コンサルティング会社です。<br>人と組織の可能性を、いっしょに育てていきます。</p>
  </div>
</section>
"""

CONTENT = f"""
{STATIC_HERO}

<section id="after-story">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">About Hitoiku</span>
      <h2>ヒトイクとは</h2>
    </div>
    <div class="about-intro">
      <div class="about-intro-copy reveal">
        <p>ヒトイクは、2024年1月10日（"ヒトの日"）に設立した、人と組織の可能性を育てる会社です。採用・研修・人事制度という、企業の「人」に関わる領域を横断しながら、目先の課題解決だけでなく、人が本来持っている可能性が自然と動き出す環境と仕組みづくりに取り組んでいます。</p>
        <p>私たちが向き合っているのは、制度や仕組みそのものではなく、その先にいる一人ひとりの人生です。数字の奥にある声に耳を傾けながら、企業と、そこで働く人の両方にとって納得のいく形を、一緒に探していきます。</p>
      </div>
      <div class="mv-box reveal">
        <div class="mv-item">
          <div class="mv-label">MISSION</div>
          <h3>UPDATE HUMAN</h3>
          <p>人は本来、成長し、変化し続ける存在。忙しさや慣習、環境によって「動きたいのに、動けない」状態が生まれることがあります。私たちは、人が本来持っている可能性が自然に更新され続ける環境と仕組みをつくります。</p>
        </div>
        <div class="mv-divider"></div>
        <div class="mv-item">
          <div class="mv-label">VISION</div>
          <h3>人の可能性が、動き出す瞬間を。</h3>
          <p>人が変わるのは、誰かに言われたときではなく、自分の中で「気づき」「納得し」「やってみよう」と思えた瞬間。静かな問い、体験、環境の変化。その積み重ねの先に、可能性は自然と動き出すと信じています。</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Belief</span>
      <h2>どんな想いでやっているか</h2>
    </div>
    <div class="philosophy-grid">
      <div class="reveal">
        <div class="philosophy-quote">
          <p>可能性に限界をつくらない。</p>
        </div>
        <div class="philosophy-body">
          <p>高校卒業後、技能職として働き始めた頃、代表の満仲は本気で「いつか社長になる」と信じていました。けれど現実の中では、年齢、学歴、職種、環境など、本人の意思や努力だけでは越えにくい壁が、確かに存在すると感じる瞬間がありました。</p>
          <p>その悔しさと同時に生まれたのが、「このままで終わりたくない」「自分の人生も、誰かの可能性も、最初から決められていいはずがない」という想いです。これが、ヒトイクの原点になっています。</p>
        </div>
        <a href="message.html" class="more" style="color:var(--brand);font-weight:700;display:inline-flex;align-items:center;gap:6px;margin-top:18px;">代表挨拶を読む {icon('arrow-right')}</a>
      </div>
      <div class="belief-list" style="grid-template-columns:1fr; gap:16px;">
        <div class="belief-item reveal"><div class="num">01</div><h4>現場 × 経営</h4><p>人事の現場実務18年とCHROとしての経営視点。両方の解像度で、机上の空論にならない支援を行います。</p></div>
        <div class="belief-item reveal"><div class="num">02</div><h4>伴走型</h4><p>資料を納品して終わりではなく、実務レベルまで一緒に手を動かし、定着するまで並走します。</p></div>
        <div class="belief-item reveal"><div class="num">03</div><h4>一気通貫</h4><p>採用・育成・制度をバラバラに発注する必要がありません。組織づくりの全体設計をワンストップで。</p></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Services</span>
      <h2>何を支援しているか</h2>
      <p>採用・育成・制度はそれぞれ独立したものではなく、つながって初めて機能します。</p>
    </div>
    <div class="service-grid">
      <div class="service-card reveal">
        <div class="service-card-photo">
          <img src="images/service-recruiting.jpg" alt="採用コンサルティング" loading="lazy">
          <div class="icon">{icon('target')}</div>
        </div>
        <div class="service-card-body">
        <div class="tag">01 / RECRUITING</div>
        <h3>採用コンサルティング</h3>
        <p>採用代行ではなく"採用の仕組み"をつくる。戦略設計から実務、面接官育成、定着支援までを一気通貫でサポートします。</p>
        <ul><li>採用戦略・要件設計</li><li>母集団形成・実務支援</li><li>面接官研修・定着支援</li></ul>
        <a href="recruiting.html" class="more">詳しく見る {icon('arrow-right')}</a>
        </div>
      </div>
      <div class="service-card reveal">
        <div class="service-card-photo">
          <img src="images/service-training.jpg" alt="研修・人材育成" loading="lazy">
          <div class="icon">{icon('brain')}</div>
        </div>
        <div class="service-card-body">
        <div class="tag">02 / TRAINING</div>
        <h3>研修・人材育成</h3>
        <p>心理学×体験学習で、行動変容を生み出す研修。「受けて終わり」にしない、現場で機能する育成をつくります。</p>
        <ul><li>管理職研修・評価者研修</li><li>面接官研修</li><li>リーダーシップ／ロジカルシンキング</li></ul>
        <a href="training.html" class="more">詳しく見る {icon('arrow-right')}</a>
        </div>
      </div>
      <div class="service-card reveal">
        <div class="service-card-photo">
          <img src="images/service-hrsystem.jpg" alt="人事制度・組織開発" loading="lazy">
          <div class="icon">{icon('layers')}</div>
        </div>
        <div class="service-card-body">
        <div class="tag">03 / HR SYSTEM</div>
        <h3>人事制度・組織開発</h3>
        <p>採用した人が育ち、評価され、活躍し続けるための土台づくり。等級・評価・処遇制度を、現場で機能する形で設計します。</p>
        <ul><li>等級・評価・処遇制度設計</li><li>評価者研修</li><li>制度運用支援</li></ul>
        <a href="hr-system.html" class="more">詳しく見る {icon('arrow-right')}</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="section-head center reveal" style="margin-left:auto;margin-right:auto;">
      <span class="eyebrow">Track Record &amp; Members</span>
      <h2>実績・メンバー</h2>
    </div>
    <div class="stat-strip reveal">
      <div class="stat"><b>98%</b><span>研修内容の満足度</span></div>
      <div class="stat"><b>99%</b><span>講師対応の満足度</span></div>
      <div class="stat"><b>98%</b><span>リピート率</span></div>
    </div>
    <div class="case-grid mt-lg">
      <div class="case-card reveal">
        <img class="case-photo" src="images/case-nursing.jpg" alt="株式会社ナーシング様 研修風景" loading="lazy">
        <div class="case-body">
          <span class="badge">研修導入事例</span>
          <h3>見えない課題を教えてくれる唯一のフィードバック</h3>
          <p>社内だけでは気づけない課題や本音の声を初めて知ることができ、業務の質が上がったことを実感。</p>
          <div class="org">株式会社ナーシング 様</div>
        </div>
      </div>
      <div class="case-card reveal">
        <img class="case-photo" src="images/case-karitsu.jpg" alt="カリツー株式会社様 研修風景" loading="lazy">
        <div class="case-body">
          <span class="badge">研修導入事例</span>
          <h3>心理学のエッセンスで、自分・メンバーと真剣に向き合えた</h3>
          <p>自分自身の考え方や在り方を見つめ直し、チームメンバーへの接し方にも変化が生まれた。</p>
          <div class="org">カリツー株式会社 様</div>
        </div>
      </div>
    </div>
    <p class="text-center mt-lg"><a href="works.html" class="btn btn-outline">支援事例をもっと見る {icon('arrow-right')}</a></p>

    <div class="ceo-mini-card reveal">
      <div class="ceo-mini-photo"><img src="https://www.genspark.ai/api/files/s/OuQLjzyT" alt="満仲 佑哉" onerror="this.style.display='none';"></div>
      <div>
        <div class="who">Hitoiku CEO</div>
        <h4>満仲 佑哉</h4>
        <p>現場歴18年 / CHRO / 公認心理師 / 社会福祉士 / キャリアコンサルタント</p>
      </div>
      <a href="message.html" class="more">代表紹介を見る {icon('arrow-right')}</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center reveal" style="margin-left:auto;margin-right:auto;">
      <span class="eyebrow">Explore</span>
      <h2>各サービスへ</h2>
      <p>それぞれの支援内容・支援フロー・料金の目安は、サービスページで詳しくご紹介しています。</p>
    </div>
    <div class="service-link-grid reveal">
      <a href="recruiting.html" class="service-link-card">
        <span class="tag">01 / RECRUITING</span>
        <h4>採用コンサルティング</h4>
        <span class="go">詳しく見る {icon('arrow-right')}</span>
      </a>
      <a href="training.html" class="service-link-card">
        <span class="tag">02 / TRAINING</span>
        <h4>研修・人材育成</h4>
        <span class="go">詳しく見る {icon('arrow-right')}</span>
      </a>
      <a href="hr-system.html" class="service-link-card">
        <span class="tag">03 / HR SYSTEM</span>
        <h4>人事制度・組織開発</h4>
        <span class="go">詳しく見る {icon('arrow-right')}</span>
      </a>
    </div>
    <p class="soft-contact-line mt-lg">貴社の課題について話を聞いてみたい方は、<a href="contact.html">お問い合わせ</a>からお気軽にどうぞ。</p>
  </div>
</section>
"""
