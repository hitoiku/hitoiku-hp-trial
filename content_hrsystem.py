from icons import icon

CONTENT = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">ホーム</a> / <a href="recruiting.html">サービス</a> / 人事制度・組織開発</div>
    <span class="eyebrow">HR System &amp; Organization Development</span>
    <h1>人事制度・組織開発</h1>
    <p class="lead">採用した人が育ち、評価され、活躍し続けるための土台づくり。等級・評価・処遇制度を、現場で機能する形で設計します。</p>
  </div>
</section>

<section class="service-hero-image">
  <div class="container">
    <img src="images/service-hrsystem.jpg" alt="人事制度・組織開発" loading="eager">
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Why It Matters</span>
      <h2>制度は、作っただけでは機能しない</h2>
      <p>人事制度は企業の成長を支える基盤ですが、現場に根づかなければ意味がありません。企業の成長段階、組織文化、経営戦略に合わせた制度設計と、継続的な運用支援が必要です。</p>
    </div>
    <div class="service-grid">
      <div class="service-card reveal">
        <div class="icon">{icon('layers')}</div>
        <h3>等級制度設計</h3>
        <p>役割・職種別の等級を整理し、社員が自身の成長段階とキャリアを見通せる制度をつくります。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('scale')}</div>
        <h3>評価制度設計</h3>
        <p>目標管理制度（MBO）、コンピテンシー評価、360度評価など、公平で納得感のある評価手法を提案・構築します。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('chart-bar')}</div>
        <h3>処遇・報酬制度設計</h3>
        <p>基本給・賞与・インセンティブなど、企業の財務状況と人材戦略に合わせた市場競争力のある処遇制度を設計します。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('chat')}</div>
        <h3>評価者研修</h3>
        <p>評価基準のすり合わせとフィードバックスキルの向上により、制度の運用品質を底上げします。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('handshake')}</div>
        <h3>制度運用支援</h3>
        <p>運用マニュアル作成、定期的な見直しなど、制度が形骸化せず機能し続けるための伴走支援を行います。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('compass')}</div>
        <h3>組織開発・DX支援</h3>
        <p>制度運用を支える人事DXツールの選定・活用まで含め、組織全体の仕組みづくりを支援します。</p>
      </div>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Process</span>
      <h2>構築プロセス</h2>
    </div>
    <div class="step-list">
      <div class="step-item reveal"><span class="step-tag">STEP 1</span><h4>現状分析</h4><p>現在の人事制度の課題を洗い出し、企業の状況を把握します。</p></div>
      <div class="step-item reveal"><span class="step-tag">STEP 2</span><h4>制度設計</h4><p>企業の成長段階に合わせた等級・評価・処遇制度を設計します。</p></div>
      <div class="step-item reveal"><span class="step-tag">STEP 3</span><h4>導入準備</h4><p>運用マニュアル作成、評価者トレーニングを実施します。</p></div>
      <div class="step-item reveal"><span class="step-tag">STEP 4</span><h4>運用・改善</h4><p>制度運用を支援し、現場の声をもとに継続的に改善します。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Recruiting Connection</span>
      <h2>採用と制度をつなげる</h2>
      <p>採用時点の期待値と、入社後の評価・キャリアパスがずれていると、早期離職の原因になります。ヒトイクは採用コンサルティングと制度設計を一体で支援できるため、「採用した人がそのまま育ち、活躍する」流れを一気通貫でつくれます。</p>
      <a href="recruiting.html" class="more" style="color:var(--brand);font-weight:700;">採用コンサルティングを見る {icon('arrow-right')}</a>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="cta-band reveal" style="background:linear-gradient(120deg, var(--brand) 0%, #0A5F55 100%);">
      <div>
        <h2>自社に合う制度、一緒に設計しませんか。</h2>
        <p>現状のヒアリングから、無料でご相談いただけます。</p>
      </div>
      <div class="actions">
        <a href="contact.html" class="btn btn-ghost-light">無料相談を予約する {icon('arrow-right')}</a>
      </div>
    </div>
  </div>
</section>
"""
