from icons import icon

CONTENT = f"""
<section class="page-hero">
  <div class="container">
    <h1>私たちについて</h1>
    <div class="about-subnav">
      <a href="#mission" class="about-subnav-item active" data-panel="mission">ミッション<span class="subnav-arrow">{icon('arrow-down')}</span></a>
      <a href="#vision" class="about-subnav-item" data-panel="vision">ビジョン<span class="subnav-arrow">{icon('arrow-right')}</span></a>
      <a href="#company" class="about-subnav-item" data-panel="company">会社概要<span class="subnav-arrow">{icon('arrow-right')}</span></a>
    </div>
  </div>
</section>

<section id="mission">
  <div class="container">
    <div class="mv-box reveal" style="max-width:960px;margin:0 auto;">
      <div class="mv-item" data-panel="mission">
        <h3>UPDATE HUMAN</h3>
        <p>人は本来、成長し、変化し続ける存在。私たちは、人が本来持っている可能性が自然に更新され続ける環境と仕組みをつくります。</p>
      </div>
      <div class="mv-item" id="vision" data-panel="vision" hidden>
        <h3>人の可能性が、動き出す瞬間を。</h3>
        <p>気づき、納得し、やってみようと思えた瞬間。その積み重ねの先に、可能性は自然と動き出すと信じています。</p>
      </div>
    </div>
  </div>
</section>

<section id="company" data-panel="company" hidden>
  <div class="container">
    <div class="section-head reveal">
      <h2>代表紹介</h2>
    </div>
    <div class="profile-hero reveal" style="margin-bottom:96px;">
      <div>
        <div class="profile-photo"><img src="https://www.genspark.ai/api/files/s/OuQLjzyT" alt="満仲 佑哉" onerror="this.style.display='none';this.parentElement.textContent='満仲';"></div>
        <p class="credential-line">現場歴18年 ／ CHRO ／ 公認心理師 ／ 社会福祉士</p>
      </div>
      <div>
        <h3 style="font-size:24px;">満仲 佑哉 <span style="font-size:14px;color:var(--ink-faint);font-weight:500;">Yuya Mitsunaka</span></h3>
        <p style="font-weight:700;color:var(--ink);">Hitoiku CEO ／ 株式会社ナーシング 取締役 CHRO</p>
        <p>「可能性に限界をつくらない。」現場実務18年とCHROとしての経営視点を掛け合わせ、人と組織の可能性が動き出す仕組みづくりに取り組んでいます。</p>
        <button type="button" class="more message-toggle" style="margin-top:8px;" aria-expanded="false">
          <span class="message-toggle-label">代表挨拶を詳しく読む</span>
          <span class="message-toggle-icon">{icon('arrow-right')}</span>
        </button>
        <div class="message-full" hidden>
          <p>Hitoikuのウェブサイトをご覧いただき、誠にありがとうございます。CEOの満仲佑哉でございます。私たちヒトイクは2024年の設立以来、「UPDATE HUMAN」という理念のもと、企業の人事支援に携わってまいりました。</p>
          <div class="quote-block">
            <p>可能性に限界をつくらない。</p>
          </div>
          <p>高校卒業後、技能職として働き始めた頃の私は、本気で「いつか社長になる」と信じていました。けれど現実の中では、年齢、学歴、職種、環境など、本人の意思や努力だけでは越えにくい壁が、確かに存在すると感じる瞬間がありました。</p>
          <p>そのとき私は強い悔しさを覚えると同時に、「このままで終わりたくない」「自分の人生も、誰かの可能性も、最初から決められていいはずがない」と強く思いました。この原体験がHitoikuの原点です。</p>
          <div class="quote-block">
            <p>数字の奥にいる、一人に向き合う。</p>
          </div>
          <p>企業にとっては「1名の離職」「1つの課題」に見えることでも、その一人には一人分の人生があり、経験があり、言葉にならない葛藤や想いがあります。私たちは、そこに向き合いたいと考えています。AIが進化する時代だからこそ、私たちはますます人間力や生き抜く力が問われる時代に入っていると考えています。AIを活用しながらも、最後は人にしかできない対話、伴走、理解、そして背中を押す支援に価値を置いています。</p>
          <div class="quote-block">
            <p>人の可能性が、動き出す社会へ。</p>
          </div>
          <p>私たちは、自然と成長できる構造を体験・制度・人事DXの力でつくり、学びと成長が日常の中に組み込まれていく状態を目指します。それが、<strong>UPDATE HUMAN</strong>。人の可能性を、思想で終わらせず、学びや仕組みで更新することです。</p>
          <p style="margin-top:30px;">2024年　ヒトイク　満仲 佑哉</p>
        </div>
      </div>
    </div>

    <div class="section-head reveal">
      <h2>代表プロフィール</h2>
    </div>
    <div style="margin-bottom:96px;">
      <div class="timeline reveal" style="margin-bottom:32px;">
        <div class="timeline-item"><div class="yr">2008年</div><p>愛知県内の工業高校を卒業後、株式会社アイシンの人材育成部門へ入社。</p></div>
        <div class="timeline-item"><div class="yr">2009年</div><p>株式会社アイシンにて、指導者・管理監督者としてチームを牽引。</p></div>
        <div class="timeline-item"><div class="yr">2016年</div><p>海外拠点の自立化支援を担当。帰国後は働きながら大学で心理学を学ぶ。</p></div>
        <div class="timeline-item message-full" hidden><div class="yr">2023年</div><p>人事部 企画グループへ異動し、全社の育成・組織づくりに関わる企画を推進。</p></div>
        <div class="timeline-item message-full" hidden><div class="yr">2024年</div><p>"ヒトの育成をする会社 Hitoiku" を設立。株式会社ナーシングの取締役CHROにも就任。</p></div>
        <div class="timeline-item message-full" hidden><div class="yr">2026年〜</div><p>経営大学院（MBA）へ入学。</p></div>
      </div>
      <button type="button" class="more message-toggle" aria-expanded="false">
        <span class="message-toggle-label">経歴をすべて見る</span>
        <span class="message-toggle-icon">{icon('arrow-right')}</span>
      </button>
    </div>

    <div class="section-head reveal">
      <h2>会社概要</h2>
    </div>
    <div class="table-wrap reveal">
      <table class="price-table">
        <tbody>
          <tr><th style="width:180px;">会社名</th><td>株式会社Hitoiku</td></tr>
          <tr><th>設立</th><td>2024年1月10日</td></tr>
          <tr><th>資本金</th><td>3,000,000</td></tr>
          <tr><th>CEO</th><td>満仲 佑哉</td></tr>
          <tr><th>メールアドレス</th><td><a href="mailto:hitoiku0110@gmail.com">hitoiku0110@gmail.com</a></td></tr>
          <tr><th>所在地</th><td>〒450-0002<br>愛知県名古屋市中村区名駅4丁目24番5号<br>第2森ビル401</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <a href="contact.html" class="contact-band reveal">
      <div class="contact-band-main">
        <span class="contact-band-title">Contact</span>
      </div>
      <p class="contact-band-desc">これからの組織の話を、はじめませんか。</p>
      <span class="contact-band-circle">{icon('arrow-right')}</span>
    </a>
  </div>
</section>
"""
