from icons import icon

CONTENT = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">ホーム</a> / <a href="recruiting.html">サービス</a> / 研修・人材育成</div>
    <span class="eyebrow">Training &amp; Development</span>
    <h1>研修・人材育成</h1>
    <p class="lead">心理学 × 体験学習で、行動変容を生み出す。「受けて終わり」にしない、現場で機能する研修を設計します。</p>
  </div>
</section>

<section class="service-hero-image">
  <div class="container">
    <img src="images/service-training.jpg" alt="研修・人材育成" loading="eager">
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Programs</span>
      <h2>研修メニュー</h2>
      <p>採用後の定着・活躍を見据え、階層・目的別にプログラムをカスタマイズします。</p>
    </div>
    <div class="service-grid">
      <div class="service-card reveal">
        <div class="icon">{icon('users')}</div>
        <h3>管理職研修</h3>
        <p>マネジメントスキル、リーダーシップ、チームビルディングなど、管理職に必要な能力を体系的に習得。部下育成の実践力を強化します。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('scale')}</div>
        <h3>評価者研修</h3>
        <p>評価基準のすり合わせと、フィードバックの質を高めるトレーニング。公平で納得感のある評価運用を実現します。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('chat')}</div>
        <h3>面接官研修</h3>
        <p>採用の見極め精度を高める評価基準の統一と、候補者に選ばれるための面接スキルを習得します。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('handshake')}</div>
        <h3>コミュニケーション研修</h3>
        <p>効果的なコミュニケーションスキルを習得し、チーム内の連携を強化。傾聴力・伝達力を実践的に学びます。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('compass')}</div>
        <h3>リーダーシップ研修</h3>
        <p>次世代リーダーに必要なビジョン構築力、戦略思考、人を動かす力を育成し、組織を牽引する人材を育てます。</p>
      </div>
      <div class="service-card reveal">
        <div class="icon">{icon('brain')}</div>
        <h3>ロジカルシンキング研修</h3>
        <p>論理的思考力と問題解決力を鍛え、現場での意思決定・提案の質を高めます。</p>
      </div>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Features</span>
      <h2>研修の特徴</h2>
    </div>
    <div class="feature-row reveal">
      <div class="feature-box"><h4><span class="ico">{icon('brain')}</span>行動心理学に基づく設計</h4><p>科学的根拠に基づいた、行動変容を促すプログラム設計。</p></div>
      <div class="feature-box"><h4><span class="ico">{icon('growth')}</span>アクティブラーニング</h4><p>体験型・参加型の学習で、知識ではなく実践力を高めます。</p></div>
      <div class="feature-box"><h4><span class="ico">{icon('puzzle')}</span>カスタマイズ対応</h4><p>企業の課題に合わせた完全オーダーメイドのプログラム。</p></div>
      <div class="feature-box"><h4><span class="ico">{icon('clock')}</span>フォローアップ</h4><p>研修後の状態確認まで、継続的にサポートします。</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head center reveal" style="margin-left:auto;margin-right:auto;">
      <span class="eyebrow">Voice</span>
      <h2>受講企業様の声</h2>
    </div>
    <div class="stat-strip reveal">
      <div class="stat"><b>98%</b><span>研修内容の満足度</span></div>
      <div class="stat"><b>99%</b><span>講師対応の満足度</span></div>
      <div class="stat"><b>98%</b><span>リピート率</span></div>
    </div>
    <div class="case-grid mt-lg">
      <div class="case-card reveal">
        <span class="badge">株式会社セキュア 様</span>
        <h3>人生そのものを学ぶ時間</h3>
        <p>講義の内容はもちろん、講師の姿勢や生き方から学ぶことが多くありました。一つひとつの言葉に説得力があります。</p>
      </div>
      <div class="case-card reveal">
        <span class="badge">中日青葉学園 様</span>
        <h3>超参加型だからこそ気づけた、本当の自分と仲間の想い</h3>
        <p>お互いの想いや価値観を共有する中で、チームの一体感が確実に高まったと感じています。</p>
      </div>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="cta-band reveal" style="background:linear-gradient(120deg, var(--brand) 0%, #0A5F55 100%);">
      <div>
        <h2>研修導入のご相談も、無料で承ります。</h2>
        <p>貴社の課題に合わせたプログラムをご提案いたします。</p>
      </div>
      <div class="actions">
        <a href="contact.html" class="btn btn-ghost-light">無料相談を予約する {icon('arrow-right')}</a>
      </div>
    </div>
  </div>
</section>
"""
