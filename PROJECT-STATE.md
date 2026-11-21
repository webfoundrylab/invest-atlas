

## 2026-11-19 実質金利の解説記事をPrivate stockに作成

- 新規記事「実質金利とは？名目金利・インフレ率との関係と投資への影響」を `real-interest-rate` として作成。
- 既存のインフレ記事・政策金利記事と役割を分け、事前/事後実質金利、近似式と複利式、期待インフレ率、BEI、資産価格への影響を整理。
- 日本銀行の2025年・2026年講演、財務省のBEI・物価連動国債解説、国際通貨研究所の期待インフレ率解説を参照。BEIの解釈上の注意点も記載。
- 記事HTML `d6d59b97`、図解SVG `c74b9a0a`、サムネイルSVG `147030a8`、manifest・逆リンク設定 `6300f222`、プレビュー順 `49ac703b`、バックログ `5912db57`。
- 公開済み「インフレとは？」「政策金利とは？」からの本文逆リンク更新ファイルを新パッケージ内に作成し、manifestのupdates/registry_updatesへ登録。
- 状態：`audit_pending`。公開キュー未登録。HTML構造・リンク先・SVG XML/実レンダリング・最終編集監査・本番同等プレビューは未完了。


## 2026-11-19 デュレーション解説記事をPrivate stockに作成

- 新規記事「デュレーションとは？金利変動による債券価格の動きと見方」を `duration-basics` としてPrivate stockへ作成。
- 既存の「債券投資とは？」が債券の基本構造・利率・利回り・価格変動を扱うのに対し、本記事はデュレーションの平均回収期間、修正デュレーションによる金利感応度の計算、債券ファンドの平均値、コンベクシティ・信用リスク等の限界に役割を限定。
- GPIFの用語集、財務省「ファイナンス」、東京海上アセットマネジメント、PIMCOの公式資料を確認。修正デュレーション2・5・8年について、金利0.5％・1％変化時の価格変化を一次近似で計算し、実際の価格変化と一致する保証がないことを明記。
- 記事HTML、金利感応度の比較図SVG、サムネイルSVG、manifestを作成。カテゴリ階層は `basics/bond-investing/bond-basics`。本文から既存公開記事3件（債券投資・資産配分・投資対象）への文脈リンクを配置。公開済み「債券投資とは？」のデュレーション節にも逆リンクを追加し、manifestのupdates/registry_updatesへ反映。リンク先の存在を確認。
- 主なコミット：記事HTML 初稿 `6a31f55e`・リンク追加 `33dd739d`、本文図解 `d924fb2a`、サムネイル 初稿 `0d8ababf`・正式副題反映 `6cb97d2c`、manifest 初稿 `95374d39`・リンク監査反映 `4309a62b`・監査記録更新 `${mu.result.commit_sha.slice(0,8)}`、プレビュー順 `ccfdfe23`、バックログ `3194308b`。
- 状態：`audit_pending`。公開キュー未登録。HTMLの最終編集監査、内部リンク・逆リンクの確定、SVG XML/実レンダリング、本番同等プレビュー（preview.bat）、PC/スマートフォン表示は未完了。ユーザーのプレビュー確認後に最終監査・必要な修正を行う。


## 2026-11-19 時価総額の基礎記事をストック作成

- 新規記事「時価総額とは？計算方法・株価との違いと企業規模の見方」を `market-capitalization-guide` として作成。
- 既存のPER・PBR・BPS・EPSは個別の企業分析指標を扱うため、本記事は時価総額の計算、株価と株式数の関係、株式分割・株式数変化、企業価値・純資産・売上高との違い、TOPIXの浮動株調整に限定。
- JPXの時価総額用語集、株価検索の表示仕様、株価指数FAQを一次資料として確認。株価と株式数を掛ける一般式、データ提供元による算定条件の違い、TOPIXでは浮動株調整がある点を反映。
- 記事HTML、比較図SVG、サムネイルSVG、manifestを作成。カテゴリ階層は `companies/company-analysis`。既存公開記事6件への本文リンクと、PER・PBR・個別株比較記事への関連記事台帳追加を設定。
- HTMLのnoindex、main内h1、目次アンカー、内部リンク先6件、カテゴリ、プレビュー順、公開キュー未登録を確認。SVGのXMLパーサー・実レンダリング、PC/スマートフォン本番同等プレビュー、最終編集監査は未完了。
- 状態：`audit_pending`。公開キュー未登録。ユーザーのプレビュー確認後に最終監査・必要な修正を行う。


## 2026-11-19 投資信託の純資産総額の記事をストック作成

- 新規記事「投資信託の純資産総額とは？ファンド規模・資金流出入・繰上償還の見方」を `fund-net-assets-guide` としてPrivate stockへ作成。
- 既存の「基準価額」記事は価格の意味・値動きを扱うため、本記事はファンド全体の規模、運用損益と資金流出入の分解、投資対象に対する規模の適切性、ファミリーファンド方式、繰上償還条項に役割を限定。
- 資産運用業協会、投資信託協会、大和アセットマネジメント、金融庁の公式資料を確認。純資産総額の大小に一律の適正基準はないこと、口数条件による繰上償還もあることを反映。
- 記事HTML、専用フロー図SVG、サムネイルSVG、manifestを作成。カテゴリ階層は `funds/investment-trust-basics`。既存公開記事4件へ本文リンク。公開済み「基準価額」記事の説明直後にも、本記事への文脈付き逆リンクを追加する更新ファイルと関連記事台帳更新を設定。
- HTMLのnoindex、main/article構造、h1が1つ、目次アンカー、内部リンク、パッケージ内ファイル参照、カテゴリ、プレビュー順、公開キュー未登録を再取得して確認。SVGはルート要素とファイル参照を確認したが、XMLパーサー・実レンダリングは未実施。
- 状態：`audit_pending`。公開キュー未登録。PC/スマートフォンの本番同等プレビュー、SVG/XMLパーサー検証、最終編集監査は未完了。ユーザー確認後に必要な修正・監査を行う。
## 2026-11-19 為替ヘッジ解説記事をPrivate stockに初稿作成

- 新規記事「投資信託の為替ヘッジとは？仕組み・コスト・ありなしの違い」を `currency-hedging-guide` としてPrivate stockへ作成。
- 直前に公開した「為替リスクとは？」の概要説明と重複しないよう、為替予約の仕組み、金利差・通貨ベーシス等によるヘッジコスト、ヘッジプレミアム、信託報酬との区別、円高・円安の計算例、フル/部分ヘッジ、目論見書・月報での確認方法に特化。
- 野村アセットマネジメント、三菱UFJアセットマネジメント、PIMCOの公式解説・FAQを確認。金利差の計算例は仮定値と明記し、現行の実コストを断定しない。
- 記事HTML、本文フロー図SVG、サムネイルSVG、manifestを作成。公開済み「為替リスク」記事からの関連記事追加を `registry_updates` に設定。recommendation-order.json に登録。
- stock全16パッケージのmanifestを横断し、slug・公開先destinationの重複なしを確認。記事HTMLの `noindex,nofollow`、`<main class="wrap"><article class="article">`、h1 1つ、本文内部リンク4件、目次アンカーの参照切れなしを確認。
- 主なコミット：記事HTML `8018fb58`、本文図解 `42e9004f`、サムネイル `4cb40dbb`、manifest/逆リンク設定 `3b73d00f`、プレビュー順 `e83fc191`。バックログ更新 `c25ba676`。
- 状態：`audit_pending`。公開キュー未登録。SVG/XMLパーサー・実レンダリングの最終検証、記事全体の編集監査、PC/スマートフォンの本番同等プレビュー、ユーザーの内容確認は未完了。確認後に必要な修正・監査を行い、プレビューOK後にready化・キュー登録へ進む。

## 2026-11-18 公開記事4本を追加監査・修正

- 公開記事4本を、公式資料・一次資料を使って再監査。
  - `ai-semiconductor-investing.html`：WSTSの2026年上期実績反映試算（2026年市場規模1兆6,550億ドル）と、NVIDIAの2027年度第3四半期決算（2026年11月17日発表）を照合。NVIDIAの売上高1,158億ドル、データセンター売上高1,076億ドル、次四半期の会社予想1,300億ドル±3%を、実績と予想を区別して追記。
  - `global-equity-indexes.html`：MSCI ACWIの約85%は世界の投資可能株式市場、FTSE Global All Capの約98%はFTSE Global Total Capを分母とすることを確認。異なる母集団の数値を直接比較できるように見せていた表現を修正。MSCIの構成銘柄数2,413（2026年10月30日時点）とFTSE側データの基準日も明記。
  - `investment-trust-distributions.html`：普通分配金・元本払戻金、NISAでの非課税扱い、再投資時の課税を再確認。NISAで再投資した分も年間投資枠を使用し、枠不足時の課税口座扱いや金融機関ごとの違いがある点を追記。日本証券業協会のQ&Aを参考資料に追加。
  - `investment-trust-investment-targets.html`：資産運用業協会の投資対象資産・地域の公式分類を照合。コモディティ型の説明に「その他資産」に含まれる場合がある旨の既存注記を確認し、重大な修正は不要と判断。
- 4記事の情報確認日を2026年11月18日に更新。公開日は維持。記事台帳 `article-index.json` の `updatedAt` も4記事とも2026-11-18へ同期。
- 主な一次資料：WSTS 2026年第2四半期リリース、NVIDIA 2027年度第3四半期決算、MSCI ACWI公式ページ・ファクトシート、FTSE Russell公式指数情報、資産運用業協会の商品分類・分配金解説、日本証券業協会NISA FAQ。
- 記事HTMLコミット：AI・半導体 `4dba922a`、投資対象 `23827eb2`、分配金 `d225bb95`（日付統一 `690b6d88`）、全世界株式指数 `4ccbc98a`（日付統一 `27ca9e12`）。記事台帳 `b8912935`。PROJECT-STATE記録 `9e172f84`。
- 未確認：GitHub Actions、Pagesデプロイ、公開URLでの実表示。次工程は公開リポジトリの検証・デプロイ状況と表示確認。
 
## 2026-11-18 単元株・単元未満株の記事をストック作成

- 新規テーマ「単元株とは？100株単位の売買と単元未満株の違い」を `unit-shares-guide` としてPrivate stockへ作成。既存の株式売買手数料・個別株投資・配当金記事と役割を分け、100株単位の仕組み、投資単位の計算、1株からの単元未満株、配当・議決権・株主優待、注文方式・約定価格・スプレッドを扱う。
- JPXの内国株売買単位・単元未満株の権利・単元制度の公式説明、SBI証券S株、楽天証券かぶミニの現行公式条件を確認。サービス条件は2026-11-18確認として本文に明記。
- 記事HTML、本文比較図SVG、サムネイルSVG、manifestを作成。カテゴリ階層 `companies/company-analysis`、本文リンク4件、公開済み記事3件への関連記事台帳追加（`registry_updates`）を設定。
- stock全パッケージの `files` / `updates` destination横断確認で衝突なし。stock原稿の `noindex,nofollow`、main内h1 1つ、本文CSS、関連記事リンク先、画像参照、サムネイルタイトル帯・透かしを確認。manifestは `sources_verified`・`internal_links_reviewed`・`backlinks_reviewed` のみtrue、残りは未確認のまま `audit_pending`。公開キュー未登録。
- 主なコミット：記事HTML `7601adb5270033814c0afd781fb8adcaf52f3aa0`、本文図解 `3377161ccc2e2f0bb6010f0660083da6544f78b6`、サムネイル `0898721164abcbda7c2d0cf3946f7815cc938dc8`、manifest `fd59555e1fbf4f109f5a67bbbd63271f7e1338d7`。
- 未実施：SVG/XMLパーサー検証、`preview.bat` による本番同等ビルド・プレビュー、PC/スマートフォンの表示確認、最終編集監査、ユーザーの内容確認。次工程はローカルプレビューを開き、完成稿の内容確認を1回行う。確認後に残りの監査・ready化・公開キュー登録へ進む。

## 2026-11-18 呼値の単位記事を監査・公開キュー登録

- Private stock の `tick-size-guide` を内容監査。JPX公式「呼値の単位」ページ、2027年3月1日施行の運用通知、STR参考資料を照合し、現行呼値表・新A/B/C/Oテーブル・STRの時間加重平均・日次中央値・1.5/5.0の判定・年次見直し・初回移行条件を確認。
- 監査で、現行のETF等の呼値欄は売買単位10口以上のETF等にも適用される注記が欠けていたため補正。また、全価格帯を掲載した表を「抜粋」と誤記していた箇所を修正。
- 記事内の関連記事3件が公開済みであること、本文リンク、画像参照、カテゴリ階層 `markets/market-trends`、stock原稿の `noindex,nofollow`、記事のh1、公開先destinationの重複なしを確認。既存の「株式の売買手数料」記事への関連記事台帳追加はmanifestの `registry_updates` で公開時に同時反映する。
- ユーザーから本番同等プレビュー確認OKの報告を受領。manifest必須6チェックをすべてtrue、`draft_status=ready` に更新。
- Private stock `queue.json` の末尾へ `tick-size-guide.html` を `scheduled` 登録。公開済み18件、scheduled 2件（先行は `dividend-yield-basics.html`、その次が本記事）。
- 記事HTML修正コミット：`9e03253cafd515b33db69a686e04533905c91ec4`。manifest ready：`4c5c1a7f8ea026d041e57cb7acaee24f3c4b3a17`。queue登録：`7eddba0eda3affb5ae654a3bcc51ff2bac9d75e2`。
- 公開リポジトリへの反映・GitHub Actionsの実行・公開後画面の確認は未実施。手動dry-runは任意工程のため未実施。次の自動公開はキュー順に従い、配当利回り記事の後に呼値記事を処理する。

## 2026-11-18 為替リスク記事を公開

- 公開キュー先頭の `currency-risk.html` を公開。タイトルは「為替リスクとは？円高・円安が海外投資に与える影響」。
- Private stock の manifest で必須6チェックがすべて true、`draft_status=ready`、記事HTMLは `noindex,nofollow`、関連記事4件はすべて公開済みであることを確認。カテゴリ階層 `markets/fx-rates-inflation` と公開先ファイルの新規性も確認。
- 公開リポジトリへ記事HTML、SVGサムネイル、本文図解2点、`article-index.json` を追加。公開順44、公開日2026-11-18、robotsを `index,follow` に変換。
- 公開コミット：`1fc37440956f7d19625e0b32062b6e6c51b62bf5`。
- GitHub Pages workflow run `44318658803` は success。サイトマップ・関連記事データ生成、記事台帳とサイトマップの検証、artifact upload、Pages deployまで成功。
- Private stock の queue を published に更新（commit `daa36444965437528d4c295e835d09fd6e3a3ae4`）。公開済みパッケージの原稿・manifest・サムネイル・図解2点をstockから削除し、公開側を正本とする運用へ移行。
- 公開URL：`https://webfoundrylab.github.io/invest-atlas/currency-risk.html`。Pagesデプロイ成功は確認済み。公開URLのブラウザ実表示は別途確認対象。

## 2026-11-15 AdSense用ルートサイトの準備

- `webfoundrylab/webfoundrylab.github.io` を新規作成し、ルートURL `https://webfoundrylab.github.io/` にInvest Atlas本体への案内ページを配置。自動転送は行わず、読者がリンクから既存サイトへ移動する構成。
- ルート `index.html` に既存のSearch Console所有権確認メタタグとAdSenseの `google-adsense-account` メタタグを配置。`ads.txt` にpublisher IDを登録し、`robots.txt` から既存サイトマップを案内。
- 既存の `webfoundrylab/invest-atlas` は変更していない。記事URL、canonical、サイトマップ、既存Search Consoleプロパティは維持。
- ルートリポジトリのGitHub Pagesブランチ公開を設定し、GitHub Actionsのビルド・デプロイrun `43717421137` が success。独自の重複デプロイworkflowは削除し、GitHub Pages標準のブランチ公開に一本化。
- GitHub Pagesのデプロイ成功は確認済み。ただし、この実行環境から公開URLへのHTTPアクセスは確認できず、ブラウザでの実表示・AdSense所有権確認・審査結果は未確認。次工程は `https://webfoundrylab.github.io/` と `/ads.txt` の実表示確認後、AdSenseでメタタグ方式の確認を実行する。
- Search Consoleの既存プロパティと既存サイトマップは変更しない。ルート用の新規プロパティ追加も現時点では不要。

## 2026-11-15 情報確認日の監査反映と管理ルール整備
- 追加監査した6記事の情報確認日を2026年11月15日に統一更新。公開日は維持。
  - `nisa-basics.html`：本文内2か所
  - `investment-trust-actual-cost.html`：本文内2か所
  - `global-vs-sp500.html`：本文内2か所
  - `bonds-basics.html`：本文内1か所
  - `stock-dividends.html`：「制度・税務の確認日」を更新
  - `maximum-drawdown.html`：本文内2か所
- 6記事をGitHubから再取得し、確認日表記がすべて2026年11月15日であることを確認。
- 再発防止として `EDITORIAL-GUIDELINES.md` に情報確認日の管理ルールを追加。内容を実際に一次資料等で再確認した監査時のみ更新し、公開日は維持、複数箇所の日付は統一、確認日が古い記事を監査候補として優先する。
- 関連コミット：NISA `7c18ce98`、実質コスト `c53eb6ed`、全世界株式とS&P 500 `6eb2c848`、債券 `e63cadfb`、配当 `b58753e2`、最大ドローダウン `ff6f3f6d`、編集ルール `39ce4a76`。
- Actions・デプロイ・公開画面は未確認。

## 2026-11-15 公開記事の追加監査とTOPIX見直し情報を反映
- 公開記事6本（新NISA、投資信託の実質コスト、全世界株式とS&P 500、債券投資、株式配当金、最大ドローダウン）を追加監査。今回確認した制度条件・計算例・説明の範囲では重大な誤りは確認されず。新NISAの2027年1月からの未成年者向け条件は金融庁の現行案内と一致。MSCI ACWIの最大ドローダウン58.38%もMSCIの2026年10月30日データと一致。
- 既存監査で把握していた「株価指数とは？」の記事に、2026年10月から始まったTOPIX第二段階の見直しが未反映だったため修正。全市場区分を母集団とする流動性基準の定期入替、初回2026年10月・次回2028年10月、移行措置銘柄の段階的なウェイト低減を追記。JPX公式の見直し資料を参考資料に追加し、情報確認日を2026年11月15日に更新。
- 記事コミット：`a750b086e1b734f2a21e388cee4def526c3cf8c8`。
- 公開ページ表示・GitHub Actions・デプロイ確認は未実施。次回は公開画面での表示確認と、未監査記事の継続監査。

## 2026-11-15 S&P 500の企業数・構成銘柄数の説明を修正
- 公開記事 `stock-market-index-basics.html` のS&P 500説明を修正。「500社で構成」とだけ記載していた箇所を、対象企業は500社、複数の株式クラスを別々に数えるため構成銘柄数は503（2026年9月30日時点）と区別して明記。
- S&P Dow Jones Indicesの公式ページで構成銘柄数503を確認し、SEC提出資料で500社と複数株式クラスの扱いを確認。
- 記事HTML commit：`3fe2b9589ed9168945bab926c83cd685a1b5008e`。表示確認・Actions・デプロイは未実施。

## 2026-11-15 投資の利益にかかる税金記事を確認済み・公開キュー登録
- Private stock の `investment-tax-basics` を再監査。国内上場株式等の譲渡益・配当の税率、特定口座・一般口座、NISA、損益通算・3年間の繰越控除、分配金の扱いを確認。
- 2026-11-15時点の国税庁資料（令和8年4月1日現在法令等）で、令和9年以後の復興特別所得税率引下げと防衛特別所得税導入後も、上場株式等の合計税率20.315%が維持されることを確認。
- 記事内の数値例・参考資料・内部リンク・カテゴリ階層・公開予定の関連記事との順序を確認。stock原稿の `noindex,nofollow`、記事HTML 1つのh1、図解・サムネイルの実ファイルとmanifest参照を確認。
- ユーザーから本番同等プレビューの表示・検証がすべてOKとの報告を受領。manifestの必須6チェックをすべてtrue、`draft_status=ready` に更新。
- Private stock `queue.json` の末尾へ `investment-tax-basics.html` を `scheduled` 登録。先行する `stock-trading-costs.html` の後に公開される。queue全体17件、published 15件、scheduled 2件。
- manifest commit：`2b768aa54beca8e50e8c28e5434519d7709cbc59`。queue commit：`5cbbf4288ae6bb029ab805db8a2dc49f80d94977`。
- 公開リポジトリの記事HTML・article-indexは未変更。手動dry-runは任意の追加検証であり、記事完成・プレビュー確認・キュー登録の条件ではないため実施不要。実際の公開実行時は公開ワークフロー自身が反映前にビルド・検証する。公開と公開後表示確認は未実施。次の公開対象は既存の `stock-trading-costs.html`。税金記事はその次の順番。

## 2026-11-15 株式売買手数料記事のdry-run準備確認
- Private stock の `ARTICLE-WORKFLOW.md`、`.github/workflows/publish.yml`、`scripts/publish.py` を再確認。
- `publish.py check` の選択ロジック上、現在の唯一の `scheduled` 記事 `stock-trading-costs.html` が次の対象になる。
- GitHub上の静的事前確認：stock原稿の `noindex,nofollow` 保持、manifest必須6チェック、記事・サムネイル・図解の存在、関連記事2件の公開状態、カテゴリ階層、逆リンク更新ファイルと公開先ファイルの存在、公開先の新規ファイル衝突なし、公開側article-index未登録を確認。
- ただしGitHub Actionsの `workflow_dispatch` を実行する操作は現在の接続ツールに提供されておらず、GitHub Actionsのdry-runそのもの（公開側へのprepare、build-site.py、validate-content.py）は未実行。従ってdry-run合格とは扱わない。
- `publish.yml` は毎日05:00 JSTのscheduleで自動的にpublishまで進む構成。dry-run未実施のまま次回scheduleに進む可能性があるため、公開前dry-runを確実に通すまではユーザー側でActionsの手動実行を行う必要がある。Actions → Scheduled publication → Run workflow → mode=dry-run。

## 2026-11-15 株式売買手数料記事を確認済み・公開キュー登録
- ユーザーが記事内容を確認し、主題「株式の売買手数料とは？」を承認。初心者向け表記として「成行（なりゆき）」「指値（さしね）」「呼値（よびね）」を初出時に読み方併記。
- 2026-11-15にSBI証券のゼロ革命適用条件、楽天証券のゼロコース・SOR同意条件、JPXの現行呼値と2027-03-01の制度変更を公式資料で再確認。無料条件の一般化しすぎを避け、NISA・現物/信用・単元未満株など取引区分の確認を促す記述に修正。
- 記事から公開済みの「個別株投資とインデックス投資」へ売買手数料・スプレッドの詳細解説リンクを追加。stock package の `updates` と `registry_updates` で本文・関連記事台帳を新記事公開と同時に反映する。
- stock manifest の必須6チェックを true、`draft_status=ready` に更新。カテゴリ階層、関連記事の公開状態、全11 stock packageのdestination重複（0件）、新規ファイルと既存更新先を確認。サムネイル・図解SVGはXML構文検証とレンダリング確認を実施。ユーザーによるプレビュー確認も受領。
- Private stock `queue.json` の末尾へ `stock-trading-costs.html` を `scheduled` で1件登録。キュー全体16件、scheduled 1件。公開リポジトリの `article-index.json` と記事HTMLはまだ変更していない。公開実行は未実施。
- 主なstockコミット：記事・条件更新 `cce086fdd9d6f6eae18b336f4e63054839bdb5a9`、逆リンク更新ファイル `40cc2bf5f9b77eb65f5c718fa4296b0a1cc1c160`、manifest ready `fc69ae5e43a94599220e12ca1de349be9274efc4`、queue登録 `d0088fd6f165d8122396442582a67cf20fdc8e8f`（その後のGitHub上の再取得でmanifest/queueの最新blob SHAも確認）。
- GitHub Actionsの手動dry-runは未実施。キュー登録は完了したが、公開側ビルド・validatorのdry-run合格、公開、公開後表示は未確認。次の定期公開トリガーで処理される前にdry-runを実施する。

## 2026-11-15 呼値の読み方と後続記事候補を記録
- 売買手数料記事の見出しを「呼値（よびね）の単位にも注意」に変更。読みが直感的でない証券用語は初出時に読み方を併記する。
- 呼値は独立記事候補「呼値の単位とは？株価の刻みと注文価格の決まり方」として整理。定義、銘柄・価格帯別の刻み、指値・スプレッドとの関係、JPXの制度変更を扱う想定。
- 単元株も独立記事候補「単元株とは？100株単位の売買と単元未満株の違い」として整理。売買単位、必要資金、単元未満株サービスとの注文・約定・費用・議決権等の違いを扱う想定。
- 2テーマは企画メモのみ。stock記事パッケージ・公開キュー・recommendation-orderには未登録。既存記事との重複調査後に制作判断する。
- stock commit：記事HTML `2aa02531012a5b832e45ce2c3d968a2a40383b53`、USER-FEEDBACK `e1ad56da955ae323b8ede11683e087442d294e09`。

## 2026-11-15 株式売買手数料記事に用語の読み方を追加
- ユーザー確認を受け、初心者向け記事では読みが直感的でない証券用語を初出時に読み仮名併記する編集方針を適用。
- Private stock の `articles/stock-trading-costs/article.html` を更新し、導入部を「成行（なりゆき）注文」、注文方法の見出しを「指値（さしね）注文」とした。2回目以降は読み仮名を繰り返さない。
- stock commit：記事HTML `5da5e24d802d9a12b93bce9213755fa371861d9b`、編集方針記録 `a0245fd8ec3a7e1019e0d395ee3abf92e4820431`。
- manifestはdraft/audit_pendingのまま。公開キュー・公開側記事には未反映。今回の読み方修正に伴うサムネイル変更は不要。

## 2026-11-15 株式の売買手数料記事の主題を整理
- ユーザー指摘を反映し、記事の中心を「証券会社に支払う売買手数料」と無料条件に変更。タイトル・導入・先に結論・図解・まとめ・サムネイルを同じ主題に統一し、スプレッドは手数料無料でも成行注文の約定価格に影響する補足として整理。
- 成行買いは通常売り気配、成行売りは通常買い気配で約定することを説明。指値注文でも反対側の気配と重なる価格ならスプレッドをまたいで約定し得る点を追記し、「指値なら必ずスプレッドの影響がない」という誤解を防止。
- 100株の例では最良気配に各100株以上の注文がある前提を明記。中間値を比較用の目安とし、片道の差は100円、往復の価格差は200円となる説明へ修正。
- Private stock記事HTML・サムネイルSVG・本文図解SVG・manifestを更新。manifestはdraft/audit_pendingのまま、公開キュー・公開側記事には未反映。
- コミット：記事HTML `e0a6a4f374165b5c1241c3dc028c77d84eee1d12`、サムネイル `d33ca9a4a145fa7da96e3d3b8c805e8935ab1098`、本文図解 `fb09f3fd75768c9f65d4847ed6727cfcab6f9d43`、manifest `ae85f574c58ada972ab3bf9874d26c0aed3226a3`。
- 追加修正：100株例の板数量前提と図解altを明記（記事HTML `e0a6a4f374165b5c1241c3dc028c77d84eee1d12`）。記事タイトルの主題・副題とmanifestの表示情報を完全一致させた（manifest `174e3f467ea1d870d1cf41e8e5062bce9ef7dafa`）。
- 未実施：本番同等プレビュー、生成後build/validate、PC/スマートフォン表示確認、編集監査とサムネイル縮小表示確認。ユーザー内容確認も未完了。

## 2026-11-04 VIX解説記事をストック制作
- 公開おすすめ順の先頭にあった既存の未完成パッケージ `articles/vix-index/` を仕上げる作業を開始。新規記事の主題は「VIXとは？恐怖指数の仕組みと見方」。
- Cboe公式FAQ・VIX Methodology・Volatility Trading資料を確認。SPXオプションの複数権利行使価格、23日超37日未満の金曜満期、近月・次限月を使った30日満期への調整、年率換算標準偏差、VIX現物指数と先物・連動商品の違いを整理。
- 30日換算例は `VIX × √(30/365)` に統一。VIX=20の1標準偏差相当を約±5.7%とし、指数5,000ポイントなら約±285ポイントの仮定例を追加。正規分布を前提とした確率の読み違いを避ける注意も追加。
- サムネイルSVGを、SPXオプション価格→VIX→約30日間の上下の変動幅という中心メッセージに沿って再設計。本文の算出フロー図は既存SVGを維持。
- VIX記事からボラティリティ・リスクとリターン・最大ドローダウン・シャープレシオへの内部リンクを整備。ボラティリティ記事からの逆リンクは、VIX公開時に同時反映する更新HTMLと記事台帳更新としてVIXパッケージへ同梱。未公開記事へのリンクを先行公開しないよう、ボラティリティ記事の現行パッケージからVIXリンクを一時的に外した。
- 公開キューの公開順は変更していない。VIX記事は未キュー・未承認。manifestは出典・内部リンク・逆リンク確認を true、ユーザー内容確認とプレビュー表示確認を false のまま維持し、`audit_pending`。
- 公開処理の確認で、stock原稿の `noindex,nofollow` が公開時に `index,follow` へ変換されず、そのまま公開される実装上の問題を発見。Private stock内の原稿はnoindexのまま保護し、公開側へコピーする際にrobotsメタをindex,followへ切り替える処理を `scripts/publish.py` に追加。ARTICLE-WORKFLOW.md にも明記。ローカルの変換関数テストは成功。GitHub Actionsでのpy_compile・dry-runは未実施。
- 次工程：ユーザーによるVIX記事の内容確認後、`preview.bat` の本番同等表示・XML/HTML検証を確認し、全項目完了後に公開キューへ追加する。公開操作は行わない。

## 2026-11-04 相関係数2記事を公開キューへ登録
- ユーザーによる記事内容確認は完了。対象は `correlation-coefficient.html` と `asset-correlation-comparison.html`。再度の内容確認は不要。
- `correlation-coefficient.html`：GPIFの2025年4月適用・基本ポートフォリオ前提資料に合わせ、相関係数と標準偏差を同一資料の値に統一。国内債券2.60%、国内株式19.19%、相関−0.254による50:50試算を9.35%へ修正（相関0は9.68%、相関+1は10.90%）。公式PDFを参考資料へ追加。
- `asset-correlation-comparison.html`：22 ETF・全231ペアの行列を点検し、負相関13ペア、最低値はTLT×DBCの−0.31と確認。本文の誤記（BIL×TLT）を訂正。EWJ行は個別相関データと照合。米国債5満期区分はSafe Rateの指数仕様・2009〜2025年の年次トータルリターンを確認。
- 記事間リンクを整備。比較記事から相関係数解説へリンクし、既存の `diversification-basics.html` と `asset-allocation-guide.html` に文脈付きリンクを追加する更新ファイル・台帳更新を比較記事パッケージへ同梱。
- ユーザーから `preview.bat` のプレビュー表示を確認できたとの報告あり。これを受け、両記事の `visuals_complete` / `thumbnail_svg` を true、`draft_status` を `ready` に更新。
- Private stock の `queue.json` 末尾へ、`correlation-coefficient.html` → `asset-correlation-comparison.html` の順で `scheduled` 登録。queue commit：`18b8e1d8ac169b8bcd16e4f6a25c1a39c24a5d2d`。
- 残作業：GitHub Actions の手動 `dry-run` を実行し、公開側ビルド・台帳・リンク検証を確認する。現時点でdry-runは未実施・未合格。手動実行は公開ではなく検証のみを選択する。
- 運用上の不整合：`ARTICLE-WORKFLOW.md` / `README.md` はJST 05:00・17:00の2回を記載するが、現行 `.github/workflows/publish.yml` はJST 05:00相当のcronしか持たない。17:00トリガーの追加が未対応。


## 2026-11-04 VIX記事のプレビュー修正・承認・キュー登録
- プレビューで発生した「files/updates間のdestination衝突」は、VIXパッケージの `updates/volatility-basics.html` が既存記事の公開先と重複していたことが原因。VIX manifestから `updates` / `registry_updates` を削除し、衝突ファイルを削除。VIX本文から既存記事へのリンクは維持し、逆リンクの上書き反映は行わない方針に変更。
- 同じ失敗を防ぐため、全stockパッケージ横断で `files` と `updates` のdestination重複を検査するルールを `ARTICLE-WORKFLOW.md` と `USER-FEEDBACK.md` に記録。
- ユーザーから継続・問題なしの確認を受け、本番同等プレビューの確認工程を完了扱いとした。VIX manifestの必須チェック6項目をすべて true、`draft_status` を `ready` に更新。
- VIXを `queue.json` の末尾（公開順9番目、scheduled記事の5番目）へ追加。先行する4本のscheduled記事の後に公開される。manifest commit：`cc2fa3858d9de12f587e11f415c5f1b4dcd49be3`、queue commit：`3ea973f5e44e92ab4b29b0aa4966a29ffecd7352`。
- VIXは公開キュー登録済みだが、GitHub Actionsの手動dry-runは未実施。公開側の最終ビルド・検証は未確認。手動publishや公開操作は行っていない。


## 2026-11-08 公開記事の共通ヘッダー欠落を修正
- 公開順上位15記事を調査し、6記事（asset-correlation-comparison.html、correlation-coefficient.html、volatility-basics.html、portfolio-rebalancing.html、asset-allocation-guide.html、lump-sum-vs-dca.html）で共通ヘッダーが欠落していることを確認。
- 原因は `scripts/build-site.py` の `inject_article_category_nav()` が、元HTMLに既存の `<header>` がある場合だけ共通ヘッダーへ置換し、ヘッダーのない記事では挿入処理を行っていなかったこと。
- 既存ヘッダーがない場合は `<body>` 直後へ共通ヘッダーを挿入する処理を追加。記事ごとのHTMLを個別修正するのではなく、共通ビルド処理を修正。
- 修正コミット：`860a52bab9bb09cafad3f0ffaf454ad98f0e56fc`。
- GitHub Actions Pages workflow run #1134 は起動済み（確認時点 queued）。ビルド・検証・デプロイ・公開画面の反映は未確認。完了後、上記6記事を含む対象ページのヘッダー表示を確認する。

## 2026-11-08 stockプレビューの構造検査と旧記事レイアウトを根本修正
- stockのプレビュー失敗を全15パッケージで確認。記事HTMLは `main.wrap + article.article`、裸の `main/article`、main直下本文など複数世代が混在。公開publisherはHTMLをそのまま配置するため、プレビュー側だけが単一class・タグ入れ子を強制していたのが誤り。Python regexの二重エスケープも併発。
- stock `preview-select.py` の構造ゲートを、main要素・main内h1 1個・noindex確認に変更。既存15記事はこの条件をすべて満たすことを横断確認。stock commit：`907e067` / regex修正 `211a86b`。
- `ARTICLE-WORKFLOW.md` の「全記事に共通shellを強制する」誤った記述を撤回し、複数世代のソース形式と公開処理の仕様を一致させた。原因・再発防止・旧対策の撤回を `USER-FEEDBACK.md` に記録。stock commits：`0e12692` / `d79e5c1`。
- 公開側 `scripts/build-site.py` も見直し。既存記事に `article.article` がない場合、main内の既存articleへ共通classを付与し、article要素自体がない場合はmain本文を共通articleカードで包む正規化を追加。旧記事（ETF・政策金利等）も本文カードと共通CSSの適用対象になる。公開側 commits：`2d2c653` → `9ab4941` → `2a20fb7` → `f722051` → `6432e54` → `413d558`（正規表現・引用符を修正し最新ソース再取得済み）。
- stock push Actions #443 はsuccess（push時のqueue checkのみ。プレビュー・記事buildテストではない）。公開側Pages workflow #1134相当の最新runはqueued。build/validate・デプロイ・ブラウザ表示はまだ未確認。次工程はstockをpullして `preview.bat` を実行し、本番build/validate結果と生成後の全記事プレビューを確認する。


## 2026-11-08 投資の羅針盤を「Invest Atlasとしての結論」中心に再設計
- ユーザー方針：読者の最終判断は読者に委ねるが、サイトとして比較・検証した結論（基本選択）を明確に出す。「人それぞれ」「条件による」で終わらせない。
- `investment-compass.html` を全面再構成。冒頭に長期資産形成の基本結論（低コスト・広く分散された株式インデックスを軸）を明示し、全世界株式 vs S&P 500、一括 vs 積立、株式100% vs 債券併用、リバランス、投資信託費用について基本回答・理由・例外を提示。生活資金・投資期間・下落耐性などの前提確認、既存解説への導線、結論の更新原則を配置。
- 記事リンク13件を `article-index.json` と照合し、全件既存記事に一致。
- コミット：`05265dd08ca3ed50acd64c80c3ba3ffeb0f65394`（investment-compass.html）。
- 未実施：HTML構文・リンク・ビルド検証、公開ページのPC/スマホ表示確認。結論の個別根拠については各比較記事の内容監査と整合確認が次の品質工程。

## 2026-11-08 投資の羅針盤：株式100% vs 債券併用の結論を明確化
- ユーザー方針：「このページだけは逃げ無し」「最強を目指す」。一般論や「リスク許容度で決める」だけで終わらせず、Invest Atlasの標準案を明言する。
- `investment-compass.html` の株式100% vs 債券併用を改稿。標準案を「長期成長資金は株式100%を出発点とし、下落幅の抑制が必要な場合に限り債券を組み合わせる。債券は必須ではない」と明示。生活資金・近い支出の分離、下落時に売却せず保有できるか、債券を加える目的とコストの判断順を追加。
- 根拠としてVanguardの英国市場1901〜2022年の株式・債券リターン比較（年率平均8.7%対5.3%、最悪暦年−52.62%対−23.15%、ポンド建て等の前提を明記）と、ECBの2022年金融安定レビュー（インフレ・金利上昇局面で株式・債券が同時下落し得る点）を一次資料リンク付きで掲載。日本円ベースの将来予測ではないことも明記。
- コミット：`5418d66416789ebc9ce3221e19a177e221b83985`（investment-compass.html）。
- 未実施：HTML構文・全リンク・ビルド検証、公開ページのPC/スマホ表示確認。今後は同ページの他の結論も同じ基準（基本選択・根拠・例外・条件・確認可能な出典）で厳しく監査する。

- 追記：根拠セクションの見出しID重複を検査で発見し、`evidence-basis` / `evidence-title` に分離して修正。追加コミット：`07ec48d391bd1aa9b303222aeb888c0b077ea964`。
- GitHub上の保存後ソースを再取得して簡易構造検査：ID重複なし、内部HTMLリンク22件を抽出し、article-index外の `editorial-policy.html` も実ファイル存在を確認。根拠セクションと株式100%の基本結論の保存を確認。
- ただし、HTMLパーサーによる構文検証、サイトビルド、GitHub Actions、公開後のPC/スマホ表示は未確認。

## 2026-11-08 投資の羅針盤：結論の説明量を整理
- ユーザー指摘：羅針盤は結論と簡潔な根拠だけを示し、数値・詳細な検証・例外の説明は個別記事に任せる。ページ内で説明を重複させない。
- `investment-compass.html` の「株式100% vs 債券併用」を、基本結論＋短い理由＋詳細記事リンクの構成に短縮。前回追加したVanguard/ECBの詳細な数値・資料解説セクションは削除し、詳細は `asset-allocation-guide.html` に委ねる。
- コミット：`9c3ab149ba2123c3fa84f41d2af77be72644b255`。
- 今後の羅針盤全体の編集基準：各テーマは「Invest Atlasの基本結論」「その理由を1〜2文」「詳しい個別記事へのリンク」を基本形とし、長い説明・データ表・細かな例外列挙は置かない。

## 2026-11-08 Invest Atlasの編集方針を「理解・比較・検証・結論」に統一
- ユーザー方針：読者の理解を重視し、解説だけ・比較だけに偏らず、投資をわかりやすく説明したうえで、複数の根拠を比較・検証し、Invest Atlasとしての最適解を導く。
- `EDITORIAL-GUIDELINES.md` に「解説・比較・結論をつなぐ編集方針」を追加。基礎解説、複数対象の比較、複数根拠による検証、サイトとしての基本結論、根拠に応じた結論更新、記事間の導線を一体で設計する。
- 根拠が不足している場合は結論を曖昧にするのではなく、不足する比較・検証を補う記事を企画する。読者が中心テーマを理解できる説明は各記事に残し、詳細な根拠は関連記事群に蓄積する。
- 羅針盤は簡潔な結論・短い理由・詳細記事への導線を維持し、個別記事群の蓄積を反映して更新する。

## 2026-11-08 読者の疑問から記事群を補強する方針を追加
- ユーザー方針：PERなどの用語解説を孤立させず、「インデックス投資と個別株投資のどちらがよいか」等の読者の疑問から逆算し、必要な基礎解説・比較・検証記事を揃える。読者が理解してから比較・判断へ進める順序を重視する。
- 「投資に終わりはあるのか」という既存記事を起点に、積立終了・保有継続・取り崩し・資産を使い切る段階を区別し、現金・預金、株式、債券、ゴールド、REIT、コモディティ等の資産の置き場所・役割・リスクを比較する記事群を検討する。
- 現状確認：公開記事には investment-period-guide.html（投資の出口）、investment-trust-investment-targets.html（株式・債券・REIT・コモディティ等の概要）、asset-correlation-comparison.html（株式・債券・金・コモディティの相関比較）が存在する。ゴールドやREITの仕組みを単独で深く理解する解説、および現金・預金も含めた資産の置き場所の包括比較は、今後の不足候補。
- Private stockにはEPS・PER・PBR・BPS・ROEの記事パッケージがある。EPS/PER/PBR/BPSは自己監査済み・ready、ROEは監査待ちとして記録されている。PERはEPSへの導線を持つ。個別株とインデックスの比較、PER等の指標をどう組み合わせて投資判断するかは、記事群の次の比較テーマ候補。
- EDITORIAL-GUIDELINES.md に「読者の疑問から記事群を設計する」基準を追加。既存記事の再利用・改稿も含め、理解→比較→検証→判断の不足を補う。

## 2026-11-08 読者の疑問に答える記事群の制作を開始
- 最新の `article-index.json`、公開記事本文、stock の `queue.json`・`recommendation-order.json`・記事マニフェストを照合。個別株とインデックス投資の比較、財務指標を組み合わせた企業分析、資産の置き場所に関する記事群を優先候補として確認。
- ゴールド投資（`articles/gold-investing/`）とREIT（`articles/reit-basics/`）はstockに既存原稿があることを確認。いずれも概要レベルで `audit_pending` のため、新規重複制作はせず既存原稿を深掘りする対象とする。
- 新規記事 `individual-stock-vs-index.html` と `financial-metrics-analysis.html` の初稿、manifest、SVGサムネイル、本文内SVG図解をPrivate stockへ作成。前者は個別株とインデックス投資の仕組み・分散・リスク・費用・手間を比較。後者はEPS・PER・BPS・PBR・ROEを仮定企業2社の数値例と分析手順で接続。
- 2記事を `recommendation-order.json` の末尾へ追加。公開キューには未登録。manifestの必須監査項目は false、`draft_status` は `audit_pending` のまま。GitHub保存後の静的検査では、各記事のh1/main/article/noindex、manifest登録ファイル数、本文画像参照、manifest関連記事と本文リンクの一致、SVG viewBoxを確認し、すべて整合。SPIVA 2026年中期版の10年・15年アンダーパフォーム率を比較記事へ追加し、個人の個別株成績を示すものではないと明記。未実施：SVG/XMLパーサー検証、本番同等プレビュー、公開側build/validate、PC/スマートフォン実表示確認、ユーザー内容確認。
- SPIVA 2026年中期版はアクティブ運用投資信託とベンチマークの比較であり、個人の個別株投資成績を直接示す資料ではないことを本文で明記。JPXの財務指標定義・業種別PER/PBR資料を企業分析記事の基礎資料として採用。
- 要確認の既存不整合：`queue.json` では `roe-basics.html` が `scheduled` だが、同記事manifestは `audit_pending` かつ「公開キュー未登録」と記載。公開状態・準備状態の矛盾を解消するまで公開対象として扱わない。
- 次工程：新規2記事の数値・比較範囲・説明・出典・内部リンクを監査し、既存ゴールド・REIT原稿を深掘りする。全記事を本番同等プレビューと検証に通し、内容確認が完了したものだけ公開準備へ進める。公開・キュー登録は別途指示なしに行わない。



## 2026-11-08 個別記事と投資の羅針盤の役割を分離
- ユーザー方針：個別記事では客観的事実を記載し、投資の羅針盤で事実・比較・検証結果からInvest Atlasとしての最適解を導く。
- `EDITORIAL-GUIDELINES.md` 第15章に役割分担を明記。個別記事では仕組み・定義・制度・費用・実績・リスク・比較結果・根拠の限界を扱い、サイト独自の推奨判断は羅針盤へ集約する。事実・推論・サイト判断を区別する。
- `articles/individual-stock-vs-index/article.html` の「6. Invest Atlasの基本的な考え方」を「6. 比較から確認できる事実」へ変更。投資方法の推奨表現を外し、投資対象・リスク構造・運用作業・SPIVAデータの適用範囲を客観的に整理。目次アンカーも更新。
- 記事コミット：`995bf02901124c30b6287402a4ec2c7056cbf13c`。編集ガイド最終整形コミット：`7b7203a0c1dc78f3d5f1d62fbcaf26d90bc91966`。
- manifestは監査待ちのまま。公開キューへの追加なし。未実施：記事全体の再読、HTML構文検証、本番同等プレビュー、公開側ビルド、PC/スマホ実表示。

## 2026-11-08 個別株・インデックス投資の読者疑問を記事群へ反映
- ユーザーが比較記事「個別株投資とインデックス投資」の確認後に挙げた疑問を、今後の記事企画へ反映する方針を記録。
  - 分散はどの程度必要か（銘柄数だけでなく、業種・地域・構成比・集中度・相関など）
  - インデックスの具体例と、それぞれの対象・構成銘柄・連動商品との違い
  - 業種分類と各業種の特徴
  - 個別株の売買手数料
  - 売値・買値の差であるスプレッドと実質的な取引コスト
  - 証券会社・取引所・注文方法を含む株式の購入手順
- stock の `USER-FEEDBACK.md` に編集上の好みとして追記（commit `8bcce88445c9154fb4bc96e0b9e0a0bc0e4d66dd`）。
- 次工程では公開記事・stock記事・記事台帳を照合し、既存記事の拡充で対応できるテーマと新規記事が必要なテーマを分ける。料金・制度・取引仕様は日本の公式資料・証券会社公式情報を基に確認日を付ける。個別記事は客観的事実に徹し、サイトとしての基本選択は投資の羅針盤で扱う。


## 2026-11-14 株式の売買コスト記事をストック制作
- 読者の疑問「個別株の売買手数料・スプレッドはどれくらいか」に対応し、新規記事「株式の売買コストとは？手数料・スプレッドの仕組みと確認方法」を作成。国内株式の現物取引を中心に、取引手数料・スプレッド・板の数量・成行/指値注文・呼値を説明。
- 100株・株価2,500円・最良買気配2,499円/最良売気配2,501円という仮定例で、即時買い/売りの差額200円を計算。手数料無料でもスプレッドや約定価格差が残ることを図表で説明。
- JPXの売買成立・呼値・買い/売り気配の説明、SBI証券のゼロ革命、楽天証券のゼロコース公式案内を確認日付きで参照。無料化の条件を併記し、特定証券会社の推奨は行わない。
- 記事HTML、SVGサムネイル、本文SVG図解、manifestをPrivate stockの `articles/stock-trading-costs/` に作成。recommendation-order.json末尾へ追加。作成コミット：article `5bc1381`、thumbnail `840dce4`、diagram `b0b820f`、manifest `0948e61`、おすすめ順 `b0cd2ea`。監査時の修正コミットは各ファイルに追加。
- 保存後の静的確認：main/h1各1件、stock noindexあり、重複IDなし、本文画像パスとmanifest files一致、本文関連記事リンクとmanifest relatedを照合。サムネイルの副題未満の日本語ラベルを修正。
- 状態：`audit_pending`。出典確認・本文内部リンク確認は完了。編集全体監査、SVG/XMLパーサー検証、本番同等プレビュー、縮小表示・PC/スマホ実画面確認、ユーザー内容確認は未完了。公開キュー未登録・公開操作なし。


## 2026-11-14 未公開記事プレビュー検証の状態不整合を修正
- **発生事象**：stock の `preview-select.py` が未公開記事を隔離プレビュー用 `article-index.json` に `status=draft` のまま登録し、本番と同じ `validate-content.py` が「unpublished stock must not be stored in the public repository」で停止した。
- **原因**：公開側validatorは公開リポジトリ内の全登録記事が `published` であることを必須とする一方、プレビュー側が公開後の状態を再現していなかった。
- **修正**：stock の `preview-select.py` で、隔離プレビューサイト内のindexへ登録するコピーだけ `status=published` に変換。保存先がプレビューサイト直下であることも実行時にガード。stock manifest の status は draft のまま、公開リポジトリは変更しない。stock原稿・プレビューHTMLの noindex は維持する。commit `fa3c30c7d791f8d768e4e40c13079a941afc6864`。
- **関連修正**：stock記事 manifest に `registry_entry.thumbnail` が未登録だったため `thumbnails/stock-trading-costs.svg` を追加（commit `ec053821de4c8a8e6c6019d3ff3c5df4e976dd70`）。ARTICLE-WORKFLOW.mdへ隔離プレビューの公開状態シミュレーションを明文化（commit `4a508c9e9ebc00f9fa0f9f96a72ff2e5157303c8`）。USER-FEEDBACK.mdに原因と再発防止策を記録（commit `e501dad806230c136be36489fe1172611e28b414`）。
- **検証**：GitHubから修正後ファイルを再取得し、status変換がプレビューindexのコピーに限定され、manifest側は draft のままであること、保存先ガード、thumbnail登録を確認。変更Pythonブロックの構文コンパイルと状態変換・保存先ガードの単体シミュレーションは成功。
- **未確認**：ユーザーのWindows環境での `py_compile`、`preview.bat`再実行、本番同等 build/validate の通過、ブラウザ表示は未実施。ローカル実行で最終確認する。

## 2026-11-14 AdSense審査前のサイト情報・プライバシー整備
- 審査前の不足として、プライバシーポリシー、サイト概要・編集体制の説明、お問い合わせ窓口が独立ページとして存在しないことを確認。
- `article-index.json` の `pages` に `about.html`、`privacy-policy.html`、`contact.html` を登録。各ページにcanonical・description・共通ヘッダーを設定。
- `privacy-policy.html` を新設。現時点で広告配信を開始していないことを明示したうえで、将来Google AdSense等を導入する場合のCookie・第三者配信事業者・Google広告設定によるパーソナライズ停止・aboutads.info、GitHub Pagesのホスティングに伴う技術情報、表示モード保存用localStorage（`ia-display-mode`）、外部リンクの取り扱いを説明。
- `about.html` を新設し、サイト目的、一次情報を優先する編集方針、事実・推論・サイト判断の区別、リスク・費用の説明方針を記載。個人名・住所などの未確認情報は創作せず、サイト名を運営主体の表示として使用。
- `contact.html` を新設。現時点で専用メール・フォームがないため、実在するGitHub Issuesを問い合わせ窓口として案内。投稿が公開されること、個人情報・口座情報等を投稿しないことを明記。
- `scripts/build-site.py` に全公開HTML共通のサイト情報フッター生成を追加。トップ、記事、カテゴリ、静的ページのすべてから「Invest Atlasについて」「編集方針・免責事項」「プライバシーポリシー」「お問い合わせ」へ移動できる構成に統一。
- `scripts/validate-content.py` に、必須情報ページの台帳登録、プライバシー開示の主要項目、問い合わせ案内、全HTMLページの共通フッターリンクを検査する条件を追加。
- 主なコミット：台帳 `b8a2403`、ページ `89368be` / `7074ad8` / `3a60363`、共通フッター生成 `98c248d`、検証処理 `5047758`。
- GitHub Actions Pages run #43550695631：build・サイトマップ生成・validate-content・artifact upload・deploy がすべて success。プライバシー等の3ページを含む5件の静的ページがサイトマップ対象になる構成。
- 未確認：この実行環境から公開URLへのHTTPアクセスがDNS解決エラーとなり、ブラウザでの公開画面・リンク遷移確認は未実施。GitHub Actionsのデプロイ成功と実画面確認は区別する。
- AdSense申請は未実施。今後広告配信を開始する前に、実際のAdSense設定・配信事業者・必要な同意管理を確認し、プライバシーポリシーを実運用に合わせて更新する。運営者の個人名・住所・電話番号・個人メールアドレス等の直接連絡先は公開しない。問い合わせ窓口は、個人情報を公開せずに利用できるサイト名義の窓口に限定する。


## 2026-11-14 共通フッターを一元化
- 前回のサイト情報リンク追加は、既存フッターの閉じタグ直前へリンクだけを挿入する方式だったため、ページごとの既存構造・幅・余白に依存し、ホーム・カテゴリ・記事・案内ページ間で表示が不揃いになる問題があった。
- scripts/build-site.py を修正し、各ページ固有のフッターを共通HTMLへ置換する方式に変更。既存フッターがないページにも同じフッターを生成し、全ページで assets/site-footer.css を読み込む。
- assets/site-footer.css を新設。PCではサイト名とサイト情報リンクを横並び、狭い画面では縦並びにするレスポンシブ設計。フッター内のインラインスタイルを廃止。
- scripts/validate-content.py を強化し、全HTMLで共通フッターが1つだけ存在すること、共通CSSが読み込まれること、4つの案内リンクがフッター内にあること、インラインスタイルがないことを検査。
- 変更コミット：build 566450850204c0eda6215aa533fe72147b8d9ece、CSS db23378dfed88fef9d5b487f2533841f1b08616b、validator 8cb95e3fa76ae52359b1081cc7e02fbf0aa43466。
- 未確認：GitHub Actionsのビルド・検証・デプロイ結果、および公開サイトでのPC/スマートフォン表示。検証成功後に実画面を確認する。


## 2026-11-14 運営者の個人情報を非公開とする方針
- ユーザーの明確な決定：運営者の個人名・住所・電話番号・個人メールアドレスなど、個人を特定・直接連絡できる情報は絶対に公開しない。
- AdSense審査対応やサイトの信頼性向上を理由に、この方針を変更・例外化しない。個人名・自宅住所・電話番号・個人メールアドレスをサイト本文、フッター、メタデータ、構造化データ、公開リポジトリへ追加しない。
- 問い合わせはInvest Atlas名義の公開窓口に限定する。GitHub Issuesを案内する場合は公開投稿であることと個人情報を書かない注意を明示する。個人用アカウントのプロフィール等から個人情報が露出しないかも別途確認する。
- AdSenseの審査要件と個人情報非公開方針が衝突する場合、個人情報を公開せず、要件の公式根拠を確認して対応可否を判断する。審査通過のために個人情報公開を勧めない。


## 2026-11-15 公開前ドライランの自動実行経路を修正
- 株式売買コスト記事の公開前確認で、従来の publish.yml は push イベントでも起動する一方、記事準備・公開サイトbuild・validateを github.event_name != 'push' で除外していたため、stockリポジトリへの通常pushでは実質的なドライランが実行されないことを確認。
- 根本対応として、stockリポジトリの .github/workflows/publish.yml を変更。due記事がある場合はpushでも公開サイトをcheckoutし、prepare・build・validateまで実行する。push時は結果報告のみとし、公開サイトへのpushおよびqueueのpublished更新はscheduleまたは明示的なworkflow_dispatch publishの場合に限定。
- 変更コミット：stock 758e7797370fb9e68e4e8e4a1cd734d243b8c489。
- GitHub上のワークフロー定義は再取得して変更内容を確認。push時の公開処理ガードが維持されていることを静的確認。
- 未確認：この接続からActions run一覧を取得できず、今回のpushによる実行開始・ドライラン結果は未確認。実行成功とは扱わない。実行結果を取得できる接続経路を継続調査する。


## 2026-11-15 公開ワークフローの不要なpush時ドライランを撤回
- 直前の変更では、stockリポジトリへの通常pushでも公開サイトのprepare・build・validateを実行するようにしていたが、通常pushのたびに重い公開前検証を重複実行する必要はないと判断。
- 公開ワークフロー本来の経路へ戻し、通常pushでは構文・キュー形式確認と公開キュー確認までを実行。公開予定記事がある場合のprepare・本番サイトbuild・validateは、定期scheduleまたは明示的なworkflow_dispatch（dry-run / publish）で実行する。
- 公開直前のbuild・validateはscheduleによる自動公開処理に含まれ、検証成功後にのみ公開・キュー更新へ進む。明示的なdry-runは任意の事前確認として残す。
- stock の `.github/workflows/publish.yml` を修正。コミット：`5e630cacb3999526190de953a45a87a4c2de8556`。実行条件を再取得して静的確認済み。
- Actionsの実行結果および次回の自動公開結果は未確認。今回の変更はワークフロー定義の修正であり、実行成功・記事公開を意味しない。


## 2026-11-15 投資の利益にかかる税金の記事を初稿作成
- 記事企画バックログの優先候補から、国内居住者の一般的な国内上場株式等を対象とする「投資の利益にかかる税金」記事を制作。
- Private stock に `articles/investment-tax-basics/` を作成し、`article.html`、SVGサムネイル、本文フロー図、`manifest.json` を保存。記事は売却益・配当・分配金、税率20.315%の内訳、特定口座・一般口座、NISA、損益通算・3年間の繰越控除、確定申告の確認手順を扱う。
- 国税庁の譲渡益課税・配当課税・NISA・損益通算資料、日本証券業協会のNISA FAQ、投資信託分配金の公式解説を確認。2027年以降の復興特別所得税関連の変更は、合計税率が20.315%から変わらない旨を注記。外国源泉税は記事対象外と明記。
- 具体例の税額計算を再点検し、取得・売却手数料を考慮する説明へ整理。記事HTMLのmain/h1/noindexと内部リンク先の公開・予約状態を静的確認。
- stockコミット：記事HTML `83ded59` → 数値・対象範囲修正 `e0daf6d`、サムネイル `21f8cccd`、本文図解 `6dec5f6c`、manifest `0889e5aa` → 監査範囲記録 `63f1c924`。企画バックログ状態更新 `b162dc16`。
- **未完了**：ユーザーによる記事内容確認、本番同等プレビュー（preview.bat）、PC/スマートフォン表示、SVG XML・レンダリング確認、build-site.py / validate-content.py、manifestの必須監査項目。したがってdraftのまま維持し、公開キューには登録していない。GitHub Actions・公開・デプロイは未実施。

- 追加：売却益の計算例を再計算し、99,000円×20.315%=20,111.85円（約20,112円）へ修正。既存の株式売買手数料記事への本文リンクを追加（stock commit `9d03bc2e`）。内部リンクの遷移先は公開済み3記事と予約公開1記事であることを再確認。


## 2026-11-15 AdSenseコードの共通ビルド挿入
- AdSenseで登録済みサイト `webfoundrylab.github.io` の所有権確認用コード（publisher `ca-pub-2286144432351332`）を、`scripts/build-site.py` の共通HTML正規化処理に追加。
- 全HTMLの `</head>` 直前にコードを一度だけ挿入する設計とし、既にコードがあるページへの重複挿入を防ぐ。フッター正規化と同じ全HTML走査で適用。
- build script commit：`74a12020`（初回変更 `9c510e7c`、エスケープ修正 `e93842a4` を含む）。
- GitHub Actionsの実行・ビルド検証・公開サイトへの反映・AdSense所有権確認は未確認。次はActionsの結果と公開ページのheadを確認後、AdSense画面の「コードを配置しました」→「確認」→審査リクエストへ進む。


## 2026-11-17 投資の利益にかかる税金記事を公開
- Private stock の公開キュー先頭にあった「投資の利益にかかる税金とは？株式・投資信託の税率と口座の違い」を、GitHub連携によるGitデータAPIの直接コミットで公開リポジトリへ反映。GitHub Actions の stock 公開workflow・追加課金は使用していない。
- 公開ファイル：`investment-tax-basics.html`、`thumbnails/investment-tax-basics.svg`、`images/investment-tax-basics-flow.svg`、`article-index.json`。記事台帳 status=published、publishOrder=43、publishedAt=2026-11-17。
- 公開コミット：`8241c10304fdd5e26035e853112deee3f5c08b84`。stock queue 更新・記事パッケージのアーカイブコミット：`cb3948ed905d77c79b4a27d622b8b5940ea3e740`。
- 公開側 GitHub Pages workflow run `44058256019` は build・サイトマップ生成・validate-content・artifact upload・deploy がすべて success。
- 公開URLへの外部アクセス確認はこの接続からできず、ブラウザ実表示は未確認。GitHub Pages デプロイ成功と実画面確認は区別する。


## 2026-11-17 公開記事のnoindex混入を修正・再発防止
- Search ConsoleのURL検査で \`stock-trading-costs.html\` が「robotsメタタグのnoindex」により除外されていることを確認。
- 公開リポジトリの実HTMLにも \`<meta name="robots" content="noindex,nofollow">\` が残っていた。Googleの取得・クロール許可・canonicalは正常で、直接原因は公開HTMLのrobots指定。
- 公開HTMLを \`index,follow\` に修正。Private stock側の原稿は公開前保護のため \`noindex,nofollow\` のまま維持する。
- 再発防止として \`scripts/validate-content.py\` に、公開済み記事HTMLの \`noindex\` を検出して検証失敗にするチェックを追加。
- GitHub Actions・Pages反映・公開URLの再取得・Search Console再検査は未確認。修正公開後、URL検査で再クロールをリクエストする。

## 2026-11-18 呼値の単位の記事を新規ストック制作
- 既存の「株式の売買手数料」記事では呼値に触れているものの、呼値の定義・価格帯/銘柄区分別の刻み・指値注文への影響・流動性との関係を独立して理解するには説明が不足するため、独立記事「呼値の単位とは？株価の刻みと指値注文・スプレッドの関係」を制作。
- JPX公式「呼値の単位」で2026年11月18日時点の現行表と2027年3月1日の制度変更を確認。JPX Working Paperも参照し、呼値の細分化が価格形成・流動性へ与える両面を説明。2,500円付近の1円/0.5円の具体例と指値注文の価格選択例を掲載。
- Private stock `articles/tick-size-guide/` に記事HTML、SVGサムネイル、本文図解、manifestを追加。公開記事「株式の売買手数料」から新記事への関連記事逆リンクをmanifestのregistry_updatesに設定。recommendation-order.jsonにも未公開候補として追加。
- コミット：記事HTML `05a60a756bb15eaef5797bf95e4a722d44393dd5`、サムネイル `11cd9bb33d71a7f59b8e1505b2bd3baebdec544b`、本文図解 `938a7186d6f62f16040c81c7c1c167ccdd81e984`、manifest `17a7e945564376755092ecee7bca1d05b00f9818`、おすすめ順 `47b2fefe84439abde1df23cb19fb978ffdf52249`。
- 現時点では制作初稿。manifestの監査チェックはすべてfalse、draft_statusはaudit_pending。stock原稿のnoindex,nofollowを維持。公開キューには未登録で、公開リポジトリへの変更・公開操作は行っていない。
- 未実施：記事全体の最終監査、図解・サムネイルのXML/縮小表示検証、本番同等preview.batによる生成・表示確認、ユーザー内容確認。JPXの2027年3月制度変更後の銘柄別適用呼値は、制度移行時に公表される最新情報を確認して更新する。

## 2026-11-18 隔離プレビューのrobots変換不整合を根本修正
- **発生事象**：呼値記事を含むstock全13記事を本番同等プレビューへ配置し、validate-content.pyを実行したところ、13記事すべてで「published article contains a noindex robots directive」となった。
- **根本原因**：本番のscripts/publish.py prepareは公開側へコピーしたHTMLをindex,followに変換してからbuild/validateするが、preview-select.pyは隔離用indexのstatusだけpublishedにし、HTML側の公開時robots変換を再現していなかった。公開処理とプレビュー処理で変換実装も分かれていた。
- **修正**：stockに共通関数scripts/robots_directives.pyを新設し、本番publisherと隔離プレビューが同じmake_article_indexable()を使用するよう統一。プレビューではfilesとupdatesのHTMLコピーに対して変換を適用後、本番build/validatorを実行。ブラウザ表示用__preview_article_*.htmlは生成後にnoindex,nofollowを付け直すため、プレビュー画面自体は検索登録されない。stock原稿はnoindexのまま維持し、validatorの条件は変更していない。
- **再発防止**：共通変換関数の単体テスト4件を追加。preview-select.py起動時にpreview-select.py / publish.py / 共通関数 / テストのpy_compileと単体テストを自動実行し、失敗時はプレビュー処理を開始しない。ARTICLE-WORKFLOW.mdとUSER-FEEDBACK.mdへ原因・処理仕様・再発防止策を反映。
- **stockコミット**：共通関数 9fc95a84ed497883d5f45318317ee391574a2bdb、preview変換適用 5edd5deb58b3a99ddf21f86cb1528ade26996e97、publisher共通化 c26c60f7a5d44420d49b096df360b8eae1106ba2、単体テスト d6ebd7b4ed7332b4641e9f3325983d4b804d90af、ARTICLE-WORKFLOW caee1d6affeee968bab45c52a902b613d0d74f16、USER-FEEDBACK 356e9191db6670fe7269f0bf68328bb68259a031、起動前の構文・単体テストゲート 6e32582fb8de20c532146550496257ef8e8af30d。
- **検証**：共通関数と単体テストの同一ソースを隔離環境でpy_compileし、4テストすべて成功。GitHub上でpublisher/preview双方の共通関数呼び出しと、プレビュー後段でのnoindex付与を再取得して静的確認。
- **未確認**：ユーザーWindows環境でのpreview.bat再実行、全13記事の本番同等build/validate通過、生成後ブラウザ表示。これらはローカル再実行で最終確認する。stock原稿のnoindex、公開リポジトリ、公開キューは変更していない。

## 2026-11-18 呼値制度変更記事の一次資料ベース改稿
- Private stock の `articles/tick-size-guide/article.html` を改稿。2027年3月1日の東証呼値制度変更について、概要だけだった説明を、JPX公式資料に基づく詳細説明へ拡充した。
- 追加内容：A（Active・超高流動性）/B（Basic・高流動性）/C（Calm・中流動性）/O（One Unit・売買単位1株/口）の意味と適用対象、新制度の全価格帯・4テーブルの呼値一覧、STRの時間加重平均による日次算出、評価期間の日次STR中央値、1.5未満/1.5〜5.0/5.0超の見直し基準、毎年8月の定期見直し、2027年3月初回適用に用いる2026年3月〜11月末のSTR等、2027年1月目途の銘柄別公表予定。
- 現行制度の呼値表も全価格帯へ拡充。STRの説明は瞬間的な板の差だけで判定するかのような記述を改め、立会時間中の気配差を時間加重平均して日次STRを求める実際の方法を記載。銘柄別初回テーブルは2026年11月18日時点で未公表として、確定情報と公表待ち情報を区別した。
- 主な一次資料：JPX「呼値の単位」 https://www.jpx.co.jp/equities/trading/domestic/07.html 、JPX運用資料 https://www.jpx.co.jp/equities/trading/domestic/tvdivq0000008dfl-att/t13vrt000001jblm.pdf 、JPX STR解説 https://www.jpx.co.jp/equities/trading/domestic/tvdivq0000008dfl-att/t13vrt000001jbo1.pdf 、制度見直し資料 https://www.jpx.co.jp/rules-participants/public-comment/detail/d2/t13vrt0000014ecv-att/t13vrt0000014efa.pdf 。
- stockコミット：記事本文の制度詳細追加 `99e112a2676687f4da907d4c8a57f6037d8df84d`、現行呼値表の全価格帯化 `56865ee30723e9b98af8e96e9f89250ef16a1968`、manifest概要更新 `eecef147bf7aa4fdaa21ce350ed5e9037adfd1a6`、現行表の説明調整 `f8773da7d8ce97f163b822009baf80c1f78ecc10`、編集品質ルール `bad2bfc6451afaf7192471001796796896713aed`。
- **未完了**：stock原稿はdraftのまま。Windowsの `preview.bat` 再実行、本番同等build/validator、生成後HTMLとSVGの表示検査、記事の最終監査は未実施。公開キュー・公開サイトは変更していない。
- 追加反映：現行呼値表の「代表的な価格帯」表現を全価格帯掲載に合わせて修正し、TOPIX500の説明箇所に株価指数解説、個別株と指数投資の比較箇所に各関連記事への本文リンクを追加。関連記事3件すべてのslugが本文HTML内に存在すること、目次アンカーの欠落がないこと、カテゴリ階層 `markets/market-trends` が公開側台帳に存在することを静的確認。公開済み債券記事への逆リンク更新ファイル `e1f8c47a`。最終stock記事コミット：`1c5ce6d0577437c1005f4fb3840c41adcdd2ab89`。
- **最終確認待ち**：`preview.bat` による本番同等ビルド・validator・生成後表示、SVGの縮小表示確認、編集監査。stock原稿はdraft・noindexのまま、queue.jsonと公開リポジトリの記事HTMLは変更していない。


## 2026-11-18 ROA（総資産利益率）記事を新規ストック制作
- 公開済みのEPS・PER・BPS・PBR・ROE記事群を補完する「ROAとは？総資産利益率の計算方法とROEとの違い」をPrivate stockに新規作成。
- JPXのROA定義、経済産業省のROA/ROE算定方法の例、財務省の法人企業統計からみえる企業の財務指標、金融庁資料のROA分解を確認。ROAは分子に使う利益によって総資産営業利益率・総資産経常利益率・総資産純利益率などがあるため、本文では当期純利益／期中平均総資産を基本式として明示し、定義違いの比較を避ける構成とした。
- 数値例（当期純利益6,000万円、期中平均総資産5億円、ROA12%）、利益率×総資産回転率の分解、ROEとの関係、業種差、成長投資・資産の帳簿価額・一時利益・負債リスクの注意点を掲載。
- Private stock `articles/roa-basics/` に記事HTML、SVGサムネイル、本文図解、manifestを作成。公開済みROE記事からの文脈リンク追加を `updates/roe-basics.html` と `registry_updates` に設定。recommendation-order.jsonへ追加。
- 静的確認：本文のnoindex・main/h1・目次アンカー、公開済み関連記事へのリンク、図解参照、カテゴリ階層、サムネイルのviewBox・固定タイトル帯・ブランド透かし、全13 stockパッケージのプレビュー順登録・公開先destination重複なしを確認。
- manifestは `draft_status=audit_pending`。sources_verified / internal_links_reviewed / backlinks_reviewedのみtrue。本文の最終編集監査、SVG/XML検証・縮小表示、本番同等 `preview.bat` のbuild/validator/ブラウザ表示、ユーザーの内容確認は未完了。公開キュー・公開リポジトリの公開記事は変更していない。

## 2026-11-18 ROIC解説記事をPrivate stockに作成

- 新規記事「ROICとは？投下資本利益率の計算方法とWACCとの関係」を `articles/roic-basics/` に作成。ROA・ROEの次に読む資本効率の指標として、NOPAT・投下資本・ROICの計算、利益率と投下資本回転率への分解、WACCとの比較、経済的利益（EP）、ROA・ROEとの違い、成長投資を含む注意点を整理。
- 経済産業省「成長投資ガイダンス（案）」のROIC・NOPAT・投下資本・WACC・EPの定義と、同省のROIC参考資料を確認。説明用の数値例は、営業利益1億円・税率30%・NOPAT7,000万円・投下資本5億円・ROIC14%。WACCを仮に8%とした場合のEPは3,000万円で、すべての数値を仮定例として明記。
- 記事HTML、本文分解図SVG、サムネイルSVG、manifestを作成。カテゴリ階層 `companies/financial-statements/financial-metrics`、ROA・ROEへの関連記事リンク、stock全14パッケージ横断の公開先destination重複なしを確認。`recommendation-order.json` に追加し、プレビュー一覧へ登録。
- manifestは出典確認・内部リンク確認のみtrue。最終編集監査、SVG XMLパーサー検証・実表示確認、ユーザーの本番同等プレビュー確認は未完了のため `audit_pending`。公開キューには未登録。
- 主なコミット：記事HTML `d4f9d6bc`、本文図解 `6b05a5de`、サムネイル `ac476b6b`、manifest `bce9cd27`、プレビュー順 `029d7fc4`。
- 次工程：ユーザー環境で `preview.bat` を実行し、`roic-basics.html` の本文・図解・サムネイルを確認。確認後、残りの監査と公開準備を行う。


## 2026-11-19 金投資記事を全面改稿

- Private stock の既存ストック `gold-investing` を、概要原稿から実用的な比較解説へ全面改稿。
- 金価格の変動要因（実質金利・米ドル・地政学リスク・需給）、円建て価格の換算式と為替の複合シナリオ、現物・純金積立・ETF・投資信託の仕組み・コスト比較、金地金の譲渡所得と商品別税務/NISAの注意点、分散投資での役割と限界を追加。
- World Gold Council「Gold Demand Trends Q3 2026」（2026-09-30基準）、Chicago Fed、国税庁、金融庁、日本証券業協会の公式資料を確認。円換算例は再計算して丸めを修正。
- サムネイルを濃紺＋ゴールドの配色で再設計し、本文図解をドル建て価格×為替の計算フローに変更。サムネイル・本文図解のSVG XML構文を確認。本文は共通レイアウト用 `main.wrap > article.article`、h1 1つ、stockのnoindexを確認。本文リンクは公開済みの分散投資・為替リスク記事へ接続。
- 主なコミット：本文改稿 `0cea92b7`、図解 `6a32c9bd`、サムネイル `f88ba53a`、計算例修正 `3551fc32`、サムネイル可読性修正 `312f67c0`、manifest更新 `f00301b8`。
- `recommendation-order.json` には既に登録済み。公開キューには未登録。manifestは `audit_pending`。公開済み記事からの逆リンク確認と本番同等プレビューの表示・validator検証が未完了。ユーザーのプレビュー確認後、最終監査・ready化・キュー登録へ進む。


## 2026-11-19 金投資記事の最終監査・公開キュー登録

- ユーザーからプレビューOKを受領。最終監査を実施し、stock manifest を `ready`、必須6チェックすべてtrueへ更新。
- NISAの参照先を金融庁の2026-11-16更新対象商品一覧と、成長投資枠の資産運用業協会案内へ分けて明確化。金地金の譲渡所得は国税庁No.3161、金価格要因はChicago Fed、需給統計はWorld Gold Council Q3 2026（2026-11-03公表、2026-09-30基準）と照合。
- カテゴリ階層に `markets / investment-themes / precious-metals（金・貴金属）` を追加し、manifestのtopicを一致させた。
- 内部リンク・遷移先、本文CSS、共通HTML構造、h1、stock noindex、画像参照、SVG構造、destination一意性を再確認。既存の分散投資・為替リスク記事を確認し、逆リンクは必須でないと判断。
- 公開キュー `queue.json` の末尾へ `gold-investing.html` を `scheduled` として追加。即時公開はしていない。
- 主なコミット：カテゴリ ea041535、NISA参照先 ddb05eeb、manifest ready 2bd06b2c、queue登録 035e9c71。


## 2026-11-19 サムネイル配色ルールを明確化

- 淡い単色・控えめなグラデーションを標準的な選択肢として残しつつ、必須条件や優先固定ルールではないことを明記。
- 濃い背景・中間的な明度・鮮やかな配色も通常の選択肢とし、例外扱いや採用割合の固定を禁止。直近5〜8記事の確認は色の使い回し防止に使い、配色比率の調整には使わない。
- サイト全体の統一感は、固定タイトル帯・文字階層・コントラスト・整理された図解で保つ方針に整理。
- THUMBNAIL-GUIDELINES.md を更新し、GitHubから再取得して反映内容を確認。コミット：db47a38da8b8ca3ce29a456125ac1f037c329786。

## 2026-11-20 配当利回り解説記事を公開

- 公開キュー先頭の「配当利回りとは？計算方法と高配当株の注意点」を公開。
- 予想・実績利回り、現在株価利回りと取得価格利回り、高利回りの落とし穴、利益・キャッシュフロー・財務から見る配当の持続性、配当性向・DOEを解説。
- 公開日・情報確認日は区別し、記事本文のrobotsを `index,follow` に変換。公開順45。
- 公開側の `article-index.json` に登録し、既存「株式の配当金」記事の関連記事にも追加。
- 直近のサムネイル配色と重複しないよう、緑系から暖色・紫系へ色相を変更。タイトル・図柄の構造は維持。
- 公開リポジトリへの反映後、GitHub Pages workflowで生成・検証・デプロイを確認する。

## 2026-11-21 呼値の単位の記事を公開
- Private stock のキュー先頭 `tick-size-guide.html` を公開。
- JPX公式の現行呼値表、2027年3月1日導入のA・B・C・Oテーブル、STR測定・中央値による年次見直し、初回適用の銘柄別公表予定を再確認。
- 公開記事URL：`https://webfoundrylab.github.io/invest-atlas/tick-size-guide.html`。
- 公開と同時に `stock-trading-costs.html` の本文へ呼値解説への文脈付き内部リンクを追加し、article-index.json の関連記事も相互に更新。
- 情報確認日を2026年11月21日に更新。公開順46。
- 公開リポジトリの公開コミット：`3dae9efe08f35180774ae694ee23db8e2c8f3fc1`。公開順46、情報確認日・公開日ともに2026年11月21日。
- Pages workflow run `44915757545` は success。サイトマップ・関連記事データ生成、記事台帳/サイトマップ検証、artifact upload、GitHub Pages deploy がすべて成功。
- 公開と同時に `stock-trading-costs.html` 本文へ呼値記事への内部リンクを追加し、記事台帳の関連記事も相互更新。
- 実URLへのアクセス確認はこの環境ではエラーとなり、ブラウザでの最終表示は未確認。
