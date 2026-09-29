from icons import icon

CONTENT = f"""
<section class="page-hero">
  <div class="container">
    <h1>私たちについて</h1>
    <div class="about-subnav">
      <a href="#mission" class="about-subnav-item active" data-panel="mission">経営理念<span class="subnav-arrow">{icon('arrow-down')}</span></a>
      <a href="#company" class="about-subnav-item" data-panel="company">会社概要<span class="subnav-arrow">{icon('arrow-right')}</span></a>
    </div>
  </div>
</section>

<section id="mission">
  <div class="container">
    <div class="mv-box fade-in-scroll" style="max-width:960px;">
      <div class="mv-item">
        <span class="eyebrow eyebrow-both eyebrow-gray-dash">Mission</span>
        <h3 style="font-size:clamp(50px, 7vw, 84px);">UPDATE HUMAN</h3>
        <p>人は本来、成長し、変化し続ける存在。私たちは、人が本来持っている可能性が自然に更新され続ける環境と仕組みをつくります。</p>
      </div>
      <div class="mv-divider"></div>
      <div class="mv-item" id="vision">
        <span class="eyebrow eyebrow-both eyebrow-gray-dash">Vision</span>
        <h3>人の可能性が、動き出す瞬間を。</h3>
        <p>気づき、納得し、やってみようと思えた瞬間。その積み重ねの先に、可能性は自然と動き出すと信じています。</p>
      </div>
    </div>
  </div>
</section>

<div class="container"><div class="divider"></div></div>

<section>
  <div class="container">
    <div class="section-head fade-in-scroll" style="max-width:1100px;">
      <span class="eyebrow eyebrow-both eyebrow-gray-dash">Values</span>
      <h2 class="nowrap-desktop" style="font-size:clamp(36px, 5vw, 60px);">私たちの大切な価値観</h2>
      <p style="font-size:35px; line-height:2; color:var(--ink);">私たちは、次の5つの価値観を軸に、日々の仕事に向き合います。</p>
    </div>
    <div class="values-list fade-in-scroll">
      <div class="values-list-item">
        <div class="values-left">
          <div class="values-row"><span class="num">01</span><span class="vline"></span><h3>中の人より、中の人。</h3></div>
          <p>お客様以上に、その会社の未来を考える。</p>
        </div>
        <p class="values-desc">外から支援するだけで終わらない。お客様の事業や人、未来を深く知り、<br>自分事のように考え、本当に必要なことを一緒につくる。</p>
      </div>
      <div class="values-list-item">
        <div class="values-left">
          <div class="values-row"><span class="num">02</span><span class="vline"></span><h3>今、ここ。</h3></div>
          <p>目の前に、本気で向き合う。</p>
        </div>
        <p class="values-desc">過去やまだ起きていない未来にとらわれすぎない。目の前の人、状況、<br>今できることに向き合い、未来を動かすのは、今ここから。</p>
      </div>
      <div class="values-list-item">
        <div class="values-left">
          <div class="values-row"><span class="num">03</span><span class="vline"></span><h3>面白がる。</h3></div>
          <p>夢中が、想像を超えていく。</p>
        </div>
        <p class="values-desc">難しさも変化も、どうせやるなら面白がる。好奇心と遊び心で、<br>新しいアイディアと挑戦を生み出す。</p>
      </div>
      <div class="values-list-item">
        <div class="values-left">
          <div class="values-row"><span class="num">04</span><span class="vline"></span><h3>選択を、正解にする。</h3></div>
          <p>選んだ道を、最高のストーリに。</p>
        </div>
        <p class="values-desc">仕事に、最初から正解があるとは限らない。だからこそ、自分たちで考え、<br>選び、選んだ道で最善を尽くす。「これでよかったのか」ではなく<br>「これを、よかった」にする。</p>
      </div>
      <div class="values-list-item">
        <div class="values-left">
          <div class="values-row"><span class="num">05</span><span class="vline"></span><h3>可能性を、ひらく。</h3></div>
          <p>見えない可能性を、見つけにいこう。</p>
        </div>
        <p class="values-desc">私たちは、もっとできる。まだ見ぬ可能性を信じ、一人ひとりの可能性を<br>ひらくことで、新しい未来をつくっていく。</p>
      </div>
    </div>
  </div>
</section>

<section id="company" data-panel="company" hidden>
  <div class="container">
    <div class="section-head reveal" style="max-width:820px;margin-bottom:96px;">
      <h2>実務経験と専門性を兼ね備えた、<br>人と組織のプロフェッショナルチーム</h2>
      <p style="font-size:15px;line-height:1.9;">Hitoikuには、トヨタグループ企業での勤務経験を持つメンバーや、現在も勤務するメンバーが在籍しています。加えて、ベンチャー企業から大企業まで、多様な組織や事業フェーズで実務経験を積んだメンバーで構成されています。そこで培った経験と、人事・採用・育成・組織開発の専門性を掛け合わせ、企業ごとの課題に合わせた支援を行います。<br><span style="font-size:11.5px;color:var(--ink-faint);">※当社とトヨタ自動車株式会社およびトヨタグループ各社との間に、資本関係、業務提携その他これらに類する関係があることを示すものではありません。</span></p>
    </div>

    <div class="section-head reveal">
      <h2>代表紹介</h2>
    </div>
    <div class="profile-hero reveal" style="margin-bottom:96px;">
      <div>
        <div class="profile-photo"><img src="https://www.genspark.ai/api/files/s/OuQLjzyT" alt="満仲 佑哉" onerror="this.style.display='none';this.parentElement.textContent='満仲';"></div>
        <p class="credential-line">公認心理師 ／ 社会福祉士</p>
      </div>
      <div>
        <h3 style="font-size:24px;">満仲 佑哉 <span style="font-size:14px;color:var(--ink-faint);font-weight:500;">Yuya Mitsunaka</span></h3>
        <p style="font-weight:700;color:var(--ink);">株式会社Hitoiku 代表取締役CEO ／ 株式会社ナーシング 取締役 CHRO</p>
        <p>「可能性に限界をつくらない。」現場実務18年とCHROとしての経営視点を掛け合わせ、<br>人と組織の可能性が動き出す仕組みづくりに取り組んでいます。</p>
        <div class="message-full">
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
          <p style="margin-top:30px;text-align:right;">2024年　株式会社Hitoiku 代表取締役CEO　満仲佑哉</p>
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
          <tr><th>設立</th><td>2024年1月10日（ヒトの日）</td></tr>
          <tr><th>資本金</th><td>3,000,000円</td></tr>
          <tr><th>代表者</th><td>代表取締役CEO  満仲 佑哉</td></tr>
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
