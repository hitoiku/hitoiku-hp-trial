from icons import icon

CONTENT = f"""
<style>.reveal{{ transition: opacity 2s ease, transform 2s ease; }}</style>
<section class="page-hero">
  <div class="container">
    <h1>事業内容</h1>
  </div>
</section>

<section class="service-hero-image">
  <div class="container">
    <img src="images/recruiting-cityscape.webp" alt="" loading="eager" class="is-short reveal">
  </div>
</section>

<section>
  <div class="container">
    <p class="about-teaser-statement reveal" style="max-width:820px;margin-bottom:16px;">Hitoikuは一緒に考え、一緒に動き、変化をつくる。</p>
    <p class="reveal" style="max-width:760px;font-size:16px;color:var(--ink);line-height:2;">Hitoikuは、採用・育成・人事制度・組織開発を通じて、人と組織の可能性を動かす支援をしています。現場に寄り添い、実行まで伴走し、超参加型の関わりによって、一人ひとりの行動変化と組織の成長につなげていきます。</p>
  </div>
</section>

<section id="recruiting" style="padding-bottom:0;">
  <div class="container">
    <div class="section-head reveal" style="max-width:800px;margin-bottom:20px;">
      <h2><span style="color:var(--ink);">01</span><br>採用コンサルティング</h2>
    </div>
  </div>
</section>

<section class="service-hero-image" style="padding-top:0;">
  <div class="container" style="display:flex; align-items:center; gap:40px; flex-wrap:wrap;">
    <img src="images/service-recruiting-2.webp" alt="採用コンサルティング" loading="lazy" class="reveal" style="width:420px;height:auto;border-radius:0;box-shadow:none;flex-shrink:0;">
    <div class="reveal" style="flex:1; min-width:280px;">
      <p style="font-size:22px; font-weight:700; color:var(--ink); margin-bottom:14px;">採用のプロと、採れる仕組みをつくる。</p>
      <p style="font-size:15px; color:var(--ink); line-height:2;">Hitoikuの採用コンサルティングは、採用計画の見直しから母集団形成、エージェント対応、選考設計、内定承諾までを一気通貫で支援します。採用担当者と伴走しながら、応募が集まらない・選考が進まない・内定辞退が多いといった採用課題を解決する。</p>
    </div>
  </div>
</section>


<section>
  <div class="container">
    <div class="section-head reveal" style="max-width:800px;">
      <h2>支援内容</h2>
    </div>
    <div class="phase-grid">
      <div class="phase-col reveal">
        <div class="phase-num-row"><span class="phase-num">01</span></div>
        <div class="phase-head">
          <h3 class="phase-title">設計</h3>
          <p class="phase-desc">採用の土台をつくり、<br>全体像を設計する</p>
        </div>
        <div class="phase-item">
          <h4>採用戦略・要件設計</h4>
          <p>採用ペルソナ、募集要件、チャネル選定、訴求メッセージまで、採用の全体設計を行います。</p>
        </div>
        <div class="phase-item">
          <h4>採用体制構築（0→1）</h4>
          <p>採用担当者の役割定義、選考フローの型化など、ゼロから採用の仕組みを立ち上げます。</p>
        </div>
      </div>
      <div class="phase-col reveal">
        <div class="phase-num-row"><span class="phase-num">02</span></div>
        <div class="phase-head">
          <h3 class="phase-title">実行</h3>
          <p class="phase-desc">現場に寄り添い、<br>採用活動を動かす</p>
        </div>
        <div class="phase-item">
          <h4>採用実務の伴走支援</h4>
          <p>母集団形成、スカウト運用、書類選考、日程調整まで、実務レベルで一緒に手を動かします。</p>
        </div>
        <div class="phase-item">
          <h4>面接官トレーニング</h4>
          <p>評価基準の統一と面接スキルの底上げで、見極め精度とアトラクト力を両立させます。</p>
        </div>
      </div>
      <div class="phase-col reveal">
        <div class="phase-num-row"><span class="phase-num">03</span></div>
        <div class="phase-head">
          <h3 class="phase-title">改善</h3>
          <p class="phase-desc">データと経験から、<br>継続的に成果を高める</p>
        </div>
        <div class="phase-item">
          <h4>採用チャネル強化（1→10）</h4>
          <p>複数チャネルの使い分けと拡大で、採用の打ち手を継続的に強化します。</p>
        </div>
        <div class="phase-item">
          <h4>採用データの可視化</h4>
          <p>応募〜内定までの歩留まりを可視化し、継続的な採用改善につなげます。</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="pain-band" style="background:#fff; padding-top:0;">
  <div class="container">
    <div class="section-head reveal">
      <h2>支援フロー</h2>
    </div>
    <div class="step-flow">
      <div class="step-flow-item reveal"><div class="dot-line"><span class="dot"></span><span class="line"></span></div><h4>ヒアリング・現状分析</h4><p>採用課題と組織の状況を丁寧にヒアリングします。</p></div>
      <div class="step-flow-item reveal"><div class="dot-line"><span class="dot"></span><span class="line"></span></div><h4>採用戦略の設計</h4><p>要件・ペルソナ・チャネル・訴求を組み立てます。</p></div>
      <div class="step-flow-item reveal"><div class="dot-line"><span class="dot"></span><span class="line"></span></div><h4>体制構築・実務伴走</h4><p>採用体制の構築と、実務・面接官トレーニングを並行して実施します。</p></div>
      <div class="step-flow-item reveal"><div class="dot-line"><span class="dot"></span><span class="line"></span></div><h4>運用・振り返り</h4><p>採用状況を確認し、継続的に仕組みを改善します。</p></div>
    </div>
  </div>
</section>

<div class="container"><div class="divider"></div></div>

<section id="training" style="padding-bottom:0;">
  <div class="container">
    <div class="section-head reveal" style="max-width:800px;margin-bottom:20px;">
      <h2><span style="color:var(--ink);">02</span><br>研修・人材育成</h2>
    </div>
  </div>
</section>

<section class="service-hero-image" style="padding-top:0;">
  <div class="container" style="display:flex; align-items:center; gap:40px; flex-wrap:wrap;">
    <img src="images/service-training-2.webp" alt="研修・人材育成" loading="lazy" class="reveal" style="width:420px;height:auto;border-radius:0;box-shadow:none;flex-shrink:0;">
    <div class="reveal" style="flex:1; min-width:280px;">
      <p style="font-size:22px; font-weight:700; color:var(--ink); margin-bottom:14px;">学びを、行動に変える。</p>
      <p style="font-size:15px; color:var(--ink); line-height:2;">Hitoikuの研修・人材育成は、企業や現場の課題に合わせた研修設計から、超参加型ワーク、実践、振り返りまでを一貫して支援します。一方的に「教える」研修ではなく、自ら考え、対話し、行動する機会をつくることで、研修を受けて終わりではなく、現場での行動変容と人材の成長につなげます。</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <h2>研修メニュー</h2>
    </div>
    <div class="menu-list">
      <div class="menu-list-item reveal">
        <div><h4>管理職研修</h4></div>
        <p>マネジメントスキル、リーダーシップ、チームビルディングなど、管理職に必要な能力を体系的に習得。部下育成の実践力を強化します。</p>
      </div>
      <div class="menu-list-item reveal">
        <div><h4>評価者研修</h4></div>
        <p>評価基準のすり合わせと、フィードバックの質を高めるトレーニング。公平で納得感のある評価運用を実現します。</p>
      </div>
      <div class="menu-list-item reveal">
        <div><h4>面接官研修</h4></div>
        <p>採用の見極め精度を高める評価基準の統一と、候補者に選ばれるための面接スキルを習得します。</p>
      </div>
      <div class="menu-list-item reveal">
        <div><h4>コミュニケーション研修</h4></div>
        <p>効果的なコミュニケーションスキルを習得し、チーム内の連携を強化。傾聴力・伝達力を実践的に学びます。</p>
      </div>
      <div class="menu-list-item reveal">
        <div><h4>リーダーシップ研修</h4></div>
        <p>次世代リーダーに必要なビジョン構築力、戦略思考、人を動かす力を育成し、組織を牽引する人材を育てます。</p>
      </div>
      <div class="menu-list-item reveal">
        <div><h4>ロジカルシンキング研修</h4></div>
        <p>論理的思考力と問題解決力を鍛え、現場での意思決定・提案の質を高めます。</p>
      </div>
    </div>
  </div>
</section>

<section class="pain-band" style="background:#fff; padding-top:0;">
  <div class="container">
    <div class="section-head reveal">
      <h2>研修の特徴</h2>
    </div>
    <div class="feature-flow reveal">
      <div class="feature-flow-item"><div class="num-icon"><span class="num">01</span><span class="ico">{icon('brain')}</span></div><h4>行動心理学に基づく設計</h4><p>科学的根拠に基づいた、行動変容を促すプログラム設計。</p></div>
      <div class="feature-flow-item col-b"><div class="num-icon"><span class="num">02</span><span class="ico">{icon('growth')}</span></div><h4>アクティブラーニング</h4><p>体験型・参加型の学習で、知識ではなく実践力を高めます。</p></div>
      <div class="feature-flow-divider"></div>
      <div class="feature-flow-item"><div class="num-icon"><span class="num">03</span><span class="ico">{icon('puzzle')}</span></div><h4>カスタマイズ対応</h4><p>企業の課題に合わせた完全オーダーメイドのプログラム。</p></div>
      <div class="feature-flow-item col-b"><div class="num-icon"><span class="num">04</span><span class="ico">{icon('clock')}</span></div><h4>フォローアップ</h4><p>研修後の状態確認まで、継続的にサポートします。</p></div>
    </div>
  </div>
</section>

<div class="container"><div class="divider"></div></div>

<section id="hr-system" style="padding-bottom:0;">
  <div class="container">
    <div class="section-head reveal" style="max-width:800px;margin-bottom:20px;">
      <h2><span style="color:var(--ink);">03</span><br>人事制度・組織開発</h2>
    </div>
  </div>
</section>

<section class="service-hero-image" style="padding-top:0;">
  <div class="container" style="display:flex; align-items:center; gap:40px; flex-wrap:wrap;">
    <img src="images/service-hrsystem-2.webp" alt="人事制度・組織開発" loading="lazy" class="reveal" style="width:420px;height:auto;border-radius:0;box-shadow:none;flex-shrink:0;">
    <div class="reveal" style="flex:1; min-width:280px;">
      <p style="font-size:22px; font-weight:700; color:var(--ink); margin-bottom:14px;">制度を、組織の成長につなげる。</p>
      <p style="font-size:15px; color:var(--ink); line-height:2;">Hitoikuの人事制度・組織開発は、等級・評価・報酬制度の設計から運用支援、評価者育成、組織課題の改善までを一貫して支援します。制度をつくって終わりではなく、現場で正しく運用され、一人ひとりの成長と組織の成果につながる仕組みづくりを支援します。</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <h2>支援内容</h2>
    </div>
    <div class="menu-grid">
      <div class="menu-grid-item reveal">
        <div class="row-head"><h4><span class="num">01</span>等級制度設計</h4></div>
        <p>役割・職種別の等級を整理し、社員が自身の成長段階とキャリアを見通せる制度をつくります。</p>
      </div>
      <div class="menu-grid-item reveal">
        <div class="row-head"><h4><span class="num">02</span>評価制度設計</h4></div>
        <p>目標管理制度（MBO）、コンピテンシー評価、360度評価など、公平で納得感のある評価手法を提案・構築します。</p>
      </div>
      <div class="menu-grid-divider"></div>
      <div class="menu-grid-item reveal">
        <div class="row-head"><h4><span class="num">03</span>処遇・報酬制度設計</h4></div>
        <p>基本給・賞与・インセンティブなど、企業の財務状況と人材戦略に合わせた市場競争力のある処遇制度を設計します。</p>
      </div>
      <div class="menu-grid-item reveal">
        <div class="row-head"><h4><span class="num">04</span>評価者研修</h4></div>
        <p>評価基準のすり合わせとフィードバックスキルの向上により、制度の運用品質を底上げします。</p>
      </div>
      <div class="menu-grid-divider"></div>
      <div class="menu-grid-item reveal">
        <div class="row-head"><h4><span class="num">05</span>制度運用支援</h4></div>
        <p>運用マニュアル作成、定期的な見直しなど、制度が形骸化せず機能し続けるための伴走支援を行います。</p>
      </div>
      <div class="menu-grid-item reveal">
        <div class="row-head"><h4><span class="num">06</span>組織開発・DX支援</h4></div>
        <p>制度運用を支える人事DXツールの選定・活用まで含め、組織全体の仕組みづくりを支援します。</p>
      </div>
    </div>
  </div>
</section>

<section class="pain-band" style="background:#fff; padding-top:0;">
  <div class="container">
    <div class="section-head reveal">
      <h2>構築プロセス</h2>
    </div>
    <div class="step-flow">
      <div class="step-flow-item reveal"><div class="dot-line"><span class="dot"></span><span class="line"></span></div><h4>現状分析</h4><p>現在の人事制度の課題を洗い出し、企業の状況を把握します。</p></div>
      <div class="step-flow-item reveal"><div class="dot-line"><span class="dot"></span><span class="line"></span></div><h4>制度設計</h4><p>企業の成長段階に合わせた等級・評価・処遇制度を設計します。</p></div>
      <div class="step-flow-item reveal"><div class="dot-line"><span class="dot"></span><span class="line"></span></div><h4>導入準備</h4><p>運用マニュアル作成、評価者トレーニングを実施します。</p></div>
      <div class="step-flow-item reveal"><div class="dot-line"><span class="dot"></span><span class="line"></span></div><h4>運用・改善</h4><p>制度運用を支援し、現場の声をもとに継続的に改善します。</p></div>
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
