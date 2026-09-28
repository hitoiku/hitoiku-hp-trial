from icons import icon

def case(tag, title, body, result, org, img=None, alt="", body_font_size=None):
    photo = f'<img class="case-photo" src="{img}" alt="{alt}" loading="lazy">' if img else ""
    body_style = f"margin-top:14px;font-size:{body_font_size}px;" if body_font_size else "margin-top:14px;"
    return f"""
    <div class="case-card reveal">
      {photo}
      <div class="case-body" style="padding:32px;">
        <span class="badge">{tag}</span>
        <h3 style="font-size:15px;">{title}</h3>
        <p style="{body_style}">{body}</p>
        <div class="result-line"><span class="result-label">成果</span>{result}</div>
        <div class="org">{org}</div>
      </div>
    </div>
    """

CONTENT = f"""
<section class="page-hero">
  <div class="container">
    <h1>支援実績</h1>
  </div>
</section>

<section>
  <div class="container">
    <div class="case-grid case-grid-2x2">
      {case(
        "医療・介護法人",
        "見えない課題を教えてくれる唯一のフィードバック",
        "現場だけでは気づけない課題や、面接官ごとの評価のばらつきが課題でした。研修と面接官トレーニングを通じ、社内では出てこない本音の声を可視化しました。",
        "見過ごしていた部分を具体的に指摘してもらえたことで、安心して導入を決められ、実際に業務の質の向上を実感。",
        "株式会社ナーシング 様",
        img="images/case-nursing.jpg", alt="株式会社ナーシング様 研修風景"
      )}
      {case(
        "運送・物流業",
        "心理学のエッセンスで、自分・メンバーと真剣に向き合えた研修",
        "管理職・メンバーそれぞれが、自分自身の考え方や在り方を見つめ直す機会が不足していました。心理学的アプローチを取り入れた研修を実施し、無意識の判断や『自分のクセ』への気づきを促しました。",
        "チームメンバーへの接し方や受け止め方に変化が生まれ、組織内コミュニケーションが改善しました。",
        "カリツー株式会社 様",
        img="images/case-karitsu.jpg", alt="カリツー株式会社様 研修風景", body_font_size=14
      )}
      {case(
        "福祉・教育法人",
        "超参加型だからこそ気づけた、本当の自分と仲間の想い",
        "研修が座学中心になりがちで、チームの一体感やお互いの価値観の共有が課題でした。超参加型の体験学習型研修を設計し、メンバー同士が想いを共有できる場をつくりました。",
        "お互いの想いや価値観を共有する中で、チームの一体感が確実に高まったとの声をいただきました。",
        "中日青葉学園 様",
        img="images/case-aoba.jpg", alt="中日青葉学園様 研修風景"
      )}
      {case(
        "専門サービス業",
        "毎日が輝いている講師から、リアルな学びをもらった",
        "知識のインプット型研修では、現場での行動変容につながりにくいという課題がありました。講師自身の実体験を交えた研修プログラムを提供し、姿勢や生き方から学べる機会を設計しました。",
        "一つひとつの言葉に説得力があり、日々の充実度が伝わる研修として高い評価をいただきました。",
        "株式会社セキュア 様",
        img="images/case-secure.jpg", alt="株式会社セキュア様 研修風景"
      )}
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
