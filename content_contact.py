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
        <h3>無料相談を予約する</h3>
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
        <div class="contact-method">
          <div class="ico">{icon('calendar')}</div>
          <div><div class="lbl">設立</div><div class="val">2024年1月10日</div></div>
        </div>
        <p style="margin-top:20px;font-size:13px;color:var(--ink-faint);">お急ぎの場合は、メールにて直接ご連絡いただいても構いません。内容を確認の上、担当より折り返しご連絡いたします。</p>
      </div>
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="section-head center reveal" style="margin-left:auto;margin-right:auto;">
      <span class="eyebrow">Before You Contact</span>
      <h2>こんなご相談も承っています</h2>
    </div>
    <div class="service-grid">
      <div class="service-card reveal"><div class="icon">{icon('target')}</div><h3>採用に関するご相談</h3><p>応募が集まらない、面接品質にばらつきがある、といった採用課題のご相談。</p></div>
      <div class="service-card reveal"><div class="icon">{icon('brain')}</div><h3>研修に関するご相談</h3><p>管理職・面接官・新入社員向けなど、階層別研修のご相談。</p></div>
      <div class="service-card reveal"><div class="icon">{icon('layers')}</div><h3>人事制度に関するご相談</h3><p>評価制度・等級制度の見直しや新規構築のご相談。</p></div>
    </div>
  </div>
</section>
"""
