from icons import icon

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeZlL0OIho6RS2qT0XHRUkNSlb5WwN1jwob5Ap6ArMgbOg42g/viewform"

CONTENT = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">ホーム</a> / お問い合わせ</div>
    <span class="eyebrow">Contact</span>
    <h1>お問い合わせ</h1>
    <p class="lead">採用・研修・人事制度など、どんな段階のお悩みでもお気軽にご相談ください。初回のご相談は無料です。</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="contact-grid">
      <div class="contact-card primary reveal">
        <h3>Contact</h3>
        <p style="font-size:14px;">下記フォームより、ご都合の良い日時とお悩みの概要をお送りください。1〜2営業日以内に担当よりご連絡いたします。</p>
        <a href="{FORM_URL}" target="_blank" rel="noopener" class="btn btn-primary" style="margin-top:10px;">フォームを開く {icon('arrow-right')}</a>

        <div class="flow-mini">
          <div class="flow-mini-item"><div class="n">1</div><p>フォームより、貴社の課題・ご希望内容をご入力ください。</p></div>
          <div class="flow-mini-item"><div class="n">2</div><p>担当より、日程調整のご連絡をいたします。</p></div>
          <div class="flow-mini-item"><div class="n">3</div><p>オンライン or 対面にて、無料ヒアリングを実施します。</p></div>
          <div class="flow-mini-item"><div class="n">4</div><p>ヒアリング内容をもとに、最適なプランをご提案します。</p></div>
        </div>
      </div>

      <div class="contact-card reveal">
        <h3>その他のお問い合わせ方法</h3>
        <div class="contact-method">
          <div class="ico">{icon('mail')}</div>
          <div><div class="lbl">メール</div><div class="val"><a href="mailto:hitoiku0110@gmail.com">hitoiku0110@gmail.com</a></div></div>
        </div>
        <div class="contact-method">
          <div class="ico">{icon('map')}</div>
          <div><div class="lbl">拠点</div><div class="val">〒450-0002<br>愛知県名古屋市中村区名駅4丁目24番5号<br>第2森ビル401<br><span style="font-weight:500;font-size:13px;color:var(--ink-faint);">（全国オンライン対応可）</span></div></div>
        </div>
        <div class="contact-method">
          <div class="ico">{icon('clock')}</div>
          <div><div class="lbl">対応時間</div><div class="val">平日 9:00〜18:00</div></div>
        </div>
        <p style="margin-top:20px;font-size:13.5px;color:var(--ink-faint);">お急ぎの場合は、メールにて直接ご連絡いただいても構いません。<br>内容を確認の上、担当より折り返しご連絡いたします。</p>
      </div>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="section-head center reveal" style="margin-left:auto;margin-right:auto;">
      <span class="eyebrow">Before You Contact</span>
      <h2>分野別のご相談窓口</h2>
      <p>詳しい支援内容は、それぞれの事業内容ページでご紹介しています。</p>
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
  </div>
</section>
"""
