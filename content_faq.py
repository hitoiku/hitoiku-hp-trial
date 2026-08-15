from icons import icon

def faq(cat, q, a):
    return f"""
    <div class="faq-item" data-cat="{cat}">
      <div class="faq-q"><span><span class="qmark">Q.</span>{q}</span>{icon('chevron').replace('<svg', '<svg class="chev"')}</div>
      <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
    </div>
    """

CONTENT = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">ホーム</a> / よくある質問</div>
    <span class="eyebrow">FAQ</span>
    <h1>よくある質問</h1>
    <p class="lead">お問い合わせの多いご質問をまとめました。ご不明点はお気軽にお問い合わせください。</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="tab-bar reveal">
      <button class="tab-btn active" data-cat="all">すべて</button>
      <button class="tab-btn" data-cat="recruiting">採用コンサルティング</button>
      <button class="tab-btn" data-cat="training">研修</button>
      <button class="tab-btn" data-cat="hrsystem">人事制度</button>
      <button class="tab-btn" data-cat="general">契約・お支払い</button>
    </div>
    <div class="faq-list reveal">
      {faq("recruiting", "採用代行との違いは何ですか？", "採用代行は業務の一部を代わりに実行することが中心ですが、ヒトイクは戦略設計から実務、面接、定着まで一気通貫で『仕組み』そのものをつくることを重視しています。単発の作業ではなく、貴社に採用のノウハウが残る形で支援します。")}
      {faq("recruiting", "どのくらいの規模の会社でも依頼できますか？", "従業員数十名規模のスタートアップから、複数拠点を持つ企業様まで幅広く対応しております。特に「採用後の早期離職」にお悩みの企業様からのご相談が多くなっています。")}
      {faq("recruiting", "採用媒体の選定から依頼できますか？", "はい。求人媒体・エージェント・スカウトサービスなど、貴社の採用要件に合ったチャネル選定からご支援可能です。")}
      {faq("training", "研修はオンライン・対面どちらに対応していますか？", "対面・オンラインどちらにも対応しております。貴社の拠点数や参加人数に応じて最適な形式をご提案します。")}
      {faq("training", "少人数や単発の研修でも依頼できますか？", "はい。管理職1名向けのスポット研修から、全社的な研修プログラムまで、規模に応じて柔軟に対応いたします。")}
      {faq("training", "研修の効果はどのように測定していますか？", "研修後のアンケートや行動チェックリストに加え、必要に応じて一定期間後のフォローアップ面談を実施し、行動変容の定着度を確認します。")}
      {faq("hrsystem", "小規模企業でも人事制度の構築は必要ですか？", "組織が10名を超えるあたりから、評価や処遇の基準が曖昧なことによる不公平感が離職要因になりやすくなります。企業規模に応じたシンプルな制度からご提案可能です。")}
      {faq("hrsystem", "既存の制度の見直しだけでも依頼できますか？", "はい。ゼロから制度を作るケースだけでなく、既存制度の課題診断・部分的な見直しのご相談も承っております。")}
      {faq("general", "相談は本当に無料ですか？", "はい、初回のご相談は無料です。貴社の課題をヒアリングした上で、最適なプランをご提案いたします。")}
      {faq("general", "契約期間の縛りはありますか？", "スポット相談から長期の顧問契約まで、貴社のご要望に応じた契約形態をご用意しています。まずはお気軽にご相談ください。")}
      {faq("general", "対応エリアを教えてください。", "愛知県名古屋市（名駅エリア）を拠点に、全国オンライン対応が可能です。対面でのご支援についてもご相談ください。")}
      {faq("general", "請求書・インボイス制度に対応していますか？", "はい、インボイス制度に対応した請求書の発行が可能です。")}
    </div>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="cta-band reveal" style="background:linear-gradient(120deg, var(--brand) 0%, #0A5F55 100%);">
      <div>
        <h2>知りたいことが見つかりませんでしたか？</h2>
        <p>どんな些細なご質問でも、お気軽にお問い合わせください。</p>
      </div>
      <div class="actions">
        <a href="contact.html" class="btn btn-ghost-light">お問い合わせする {icon('arrow-right')}</a>
      </div>
    </div>
  </div>
</section>
"""
