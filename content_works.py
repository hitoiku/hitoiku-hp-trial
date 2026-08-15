from icons import icon

def case(tag, title, issue, support, result, org, img=None, alt=""):
    photo = f'<img class="case-photo" src="{img}" alt="{alt}" loading="lazy">' if img else ""
    return f"""
    <div class="case-card reveal">
      {photo}
      <div class="case-body" style="padding:32px;">
        <span class="badge">{tag}</span>
        <h3 style="font-size:19px;">{title}</h3>
        <div style="display:flex;flex-direction:column;gap:14px;margin-top:16px;">
          <div><div class="tag" style="font-family:var(--ff-en);font-size:11.5px;color:var(--accent);font-weight:800;letter-spacing:.08em;">課題</div><p style="margin:4px 0 0;font-size:14px;">{issue}</p></div>
          <div><div class="tag" style="font-family:var(--ff-en);font-size:11.5px;color:var(--brand);font-weight:800;letter-spacing:.08em;">支援</div><p style="margin:4px 0 0;font-size:14px;">{support}</p></div>
          <div><div class="tag" style="font-family:var(--ff-en);font-size:11.5px;color:var(--gold);font-weight:800;letter-spacing:.08em;">成果</div><p style="margin:4px 0 0;font-size:14px;">{result}</p></div>
        </div>
        <div class="org">{org}</div>
      </div>
    </div>
    """

CONTENT = f"""
<section class="page-hero">
  <div class="container">
    <div class="breadcrumb"><a href="index.html">ホーム</a> / 支援事例</div>
    <span class="eyebrow">Case Studies</span>
    <h1>支援事例</h1>
    <p class="lead">「課題 → 支援 → 成果」の3段構成でご紹介します。数値実績は今後の蓄積とともに順次公開してまいります。</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="case-grid">
      {case(
        "医療・介護法人",
        "見えない課題を教えてくれる唯一のフィードバック",
        "現場だけでは気づけない課題や、面接官ごとの評価のばらつきが課題でした。",
        "研修と面接官トレーニングを通じ、社内では出てこない本音の声を可視化しました。",
        "見過ごしていた部分を具体的に指摘してもらえたことで、安心して導入を決められ、実際に業務の質の向上を実感。",
        "株式会社ナーシング 様",
        img="images/case-nursing.jpg", alt="株式会社ナーシング様 研修風景"
      )}
      {case(
        "運送・物流業",
        "心理学のエッセンスで、自分・メンバーと真剣に向き合えた研修",
        "管理職・メンバーそれぞれが、自分自身の考え方や在り方を見つめ直す機会が不足していました。",
        "心理学的アプローチを取り入れた研修を実施し、無意識の判断や『自分のクセ』への気づきを促しました。",
        "チームメンバーへの接し方や受け止め方に変化が生まれ、組織内コミュニケーションが改善しました。",
        "カリツー株式会社 様",
        img="images/case-karitsu.jpg", alt="カリツー株式会社様 研修風景"
      )}
      {case(
        "福祉・教育法人",
        "超参加型だからこそ気づけた、本当の自分と仲間の想い",
        "研修が座学中心になりがちで、チームの一体感やお互いの価値観の共有が課題でした。",
        "超参加型の体験学習型研修を設計し、メンバー同士が想いを共有できる場をつくりました。",
        "お互いの想いや価値観を共有する中で、チームの一体感が確実に高まったとの声をいただきました。",
        "中日青葉学園 様",
        img="images/case-aoba.jpg", alt="中日青葉学園様 研修風景"
      )}
      {case(
        "専門サービス業",
        "毎日が輝いている講師から、リアルな学びをもらった",
        "知識のインプット型研修では、現場での行動変容につながりにくいという課題がありました。",
        "講師自身の実体験を交えた研修プログラムを提供し、姿勢や生き方から学べる機会を設計しました。",
        "一つひとつの言葉に説得力があり、日々の充実度が伝わる研修として高い評価をいただきました。",
        "株式会社セキュア 様",
        img="images/case-secure.jpg", alt="株式会社セキュア様 研修風景"
      )}
    </div>
    <p class="price-note text-center mt-lg">※ 掲載している事例は各社様の許諾を得て公開しています。採用コンサルティング・人事制度構築の数値実績は、今後の支援実績の蓄積とともに順次公開してまいります。</p>
  </div>
</section>

<section class="pain-band">
  <div class="container">
    <div class="cta-band reveal" style="background:linear-gradient(120deg, var(--brand) 0%, #0A5F55 100%);">
      <div>
        <h2>貴社の課題も、まずはお聞かせください。</h2>
        <p>業種・規模を問わず、無料相談を承っております。</p>
      </div>
      <div class="actions">
        <a href="contact.html" class="btn btn-ghost-light">無料相談を予約する {icon('arrow-right')}</a>
      </div>
    </div>
  </div>
</section>
"""
