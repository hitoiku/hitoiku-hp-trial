from icons import icon, service_subnav

CONTENT = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">ホーム</a> / <a href="recruiting.html">事業内容</a> / 採用コンサルティング</div>
    <span class="eyebrow">Recruiting Consulting</span>
    <h1>採用コンサルティング</h1>
    <p class="lead">採用担当者ゼロから、採用の仕組みを立ち上げる（0→1）。すでにある採用活動を、次のフェーズへ強化する（1→10）。貴社の"採用部署"そのものを、伴走してつくります。</p>
  </div>
</section>

{service_subnav("recruiting.html")}

<section class="service-hero-image">
  <div class="container">
    <img src="images/service-recruiting.png" alt="採用コンサルティング" loading="eager">
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal" style="max-width:800px;">
      <span class="eyebrow">Challenges</span>
      <h2>こんな状態、心当たりありませんか</h2>
      <p>採用部署の立ち上げ期・強化期の企業様には、共通する構造的な課題があります。</p>
    </div>
    <div class="feature-row reveal">
      <div class="feature-box"><h4><span class="ico">{icon('users')}</span>採用の専任者がいない</h4><p>経営者や他部署の担当者が兼任で採用を行っており、ノウハウが属人化しています。</p></div>
      <div class="feature-box"><h4><span class="ico">{icon('compass')}</span>採用チャネル・手法が定まっていない</h4><p>求人媒体やエージェントを場当たり的に使っており、費用対効果が見えていません。</p></div>
      <div class="feature-box"><h4><span class="ico">{icon('puzzle')}</span>採用の仕組みが整っていない</h4><p>選考フローや評価基準が言語化されておらず、採用のたびに手探りになっています。</p></div>
      <div class="feature-box"><h4><span class="ico">{icon('growth')}</span>採用を強化したいが、方法がわからない</h4><p>採用人数を増やしたい、新しいポジションを採用したいが、体制づくりが追いついていません。</p></div>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Solution</span>
      <h2>解決策："採用部署"を、0→1、1→10でつくる</h2>
      <p>単発の求人代行ではなく、採用の立ち上げ・強化を、仕組みとして構築します。現場18年とCHROとしての経営視点を掛け合わせ、貴社だけの採用の型をつくります。</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">What We Do</span>
      <h2>支援内容</h2>
    </div>
    <div class="service-grid">
      <div class="service-card reveal">
        <div class="icon">{icon('compass')}</div>
        <h3>採用戦略・要件設計</h3>
        <p>採用ペルソナ、募集要件、チャネル選定、訴求メッセージまで、採用の全体設計を行います。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('layers')}</div>
        <h3>採用体制構築（0→1）</h3>
        <p>採用担当者の役割定義、選考フローの型化など、ゼロから採用の仕組みを立ち上げます。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('handshake')}</div>
        <h3>採用実務の伴走支援</h3>
        <p>母集団形成、スカウト運用、書類選考、日程調整まで、実務レベルで一緒に手を動かします。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('chat')}</div>
        <h3>面接官トレーニング</h3>
        <p>評価基準の統一と面接スキルの底上げで、見極め精度とアトラクト力を両立させます。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('growth')}</div>
        <h3>採用チャネル強化（1→10）</h3>
        <p>複数チャネルの使い分けと拡大で、採用力を伸ばしたいフェーズの企業様を支援します。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('chart-bar')}</div>
        <h3>採用データの可視化</h3>
        <p>応募〜内定までの歩留まりを可視化し、継続的な採用改善につなげます。</p>
      </div>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Process</span>
      <h2>支援フロー</h2>
    </div>
    <div class="step-list">
      <div class="step-item reveal"><span class="step-tag">STEP 1</span><h4>ヒアリング・現状分析</h4><p>採用課題と組織の状況を丁寧にヒアリングします。</p></div>
      <div class="step-item reveal"><span class="step-tag">STEP 2</span><h4>採用戦略の設計</h4><p>要件・ペルソナ・チャネル・訴求を組み立てます。</p></div>
      <div class="step-item reveal"><span class="step-tag">STEP 3</span><h4>体制構築・実務伴走</h4><p>採用体制の構築と、実務・面接官トレーニングを並行して実施します。</p></div>
      <div class="step-item reveal"><span class="step-tag">STEP 4</span><h4>運用・振り返り</h4><p>採用状況を確認し、継続的に仕組みを改善します。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-band reveal">
      <div>
        <h2>採用部署づくり、まずは無料相談から。</h2>
        <p>貴社の採用課題をヒアリングし、最適なプランをご提案いたします。</p>
      </div>
      <div class="actions">
        <a href="contact.html" class="btn btn-ghost-light">Contact {icon('arrow-right')}</a>
      </div>
    </div>
  </div>
</section>
"""
