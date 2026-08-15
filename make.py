from build import page
from content_index import CONTENT as C_INDEX
from content_recruiting import CONTENT as C_RECRUIT
from content_training import CONTENT as C_TRAIN
from content_hrsystem import CONTENT as C_HRSYS
from content_works import CONTENT as C_WORKS
from content_message import CONTENT as C_MSG
from content_faq import CONTENT as C_FAQ
from content_contact import CONTENT as C_CONTACT
from content_privacy import CONTENT as C_PRIVACY

page("index.html", "ヒトイク | 採用して終わらせない。人が定着し、育つ組織へ。 - UPDATE HUMAN",
     "ヒトイクは、採用を入口に定着・育成・組織づくりまで伴走する採用コンサルティング会社です。採用コンサルティング・研修・人事制度構築を通じて企業の成長を支援します。",
     "home", C_INDEX, extra_css="css/story.css")

page("recruiting.html", "採用コンサルティング | ヒトイク",
     "採用代行ではなく、採用の仕組みをつくる。採用戦略設計から実務、面接官研修、定着支援までを一気通貫で支援する採用コンサルティングサービス。",
     "service", C_RECRUIT)

page("training.html", "研修・人材育成 | ヒトイク",
     "心理学×体験学習で行動変容を生み出す研修サービス。管理職研修、評価者研修、面接官研修、コミュニケーション研修、リーダーシップ研修など。",
     "service", C_TRAIN)

page("hr-system.html", "人事制度・組織開発 | ヒトイク",
     "等級・評価・処遇制度の設計から評価者研修、制度運用支援まで。現場で機能する人事制度・組織開発を支援します。",
     "service", C_HRSYS)

page("works.html", "支援事例 | ヒトイク",
     "ヒトイクの支援事例をご紹介。課題・支援内容・成果の3段構成で、企業の人事課題解決の実例をご覧いただけます。",
     "works", C_WORKS)

page("message.html", "代表紹介 | ヒトイク",
     "Hitoiku CEO 満仲佑哉のご挨拶とプロフィール。現場歴18年、CHRO、公認心理師、社会福祉士の視点から、UPDATE HUMANの理念を語ります。",
     "message", C_MSG)

page("faq.html", "よくある質問 | ヒトイク",
     "採用コンサルティング、研修、人事制度構築に関するよくあるご質問をまとめました。",
     "faq", C_FAQ)

page("contact.html", "お問い合わせ | ヒトイク",
     "採用・研修・人事制度に関するご相談は無料です。お気軽にお問い合わせください。",
     "contact", C_CONTACT)

page("privacy.html", "プライバシーポリシー | ヒトイク",
     "ヒトイクのプライバシーポリシーです。",
     "", C_PRIVACY)

print("done")
