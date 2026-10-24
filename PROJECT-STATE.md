# Invest Atlas — Project State

最終更新: 2026-10-24

## プロジェクト概要
- サイト名: Invest Atlas（仮）
- リポジトリ: https://github.com/webfoundrylab/invest-atlas
- 公開URL（予定）: https://webfoundrylab.github.io/invest-atlas/
- 目的: 投資全般の解説・比較情報を提供し、検索流入を育て、将来的に透明性のある広告・アフィリエイト収益につなげる
- 予算方針: 無料で開始。有料サービスや支出は事前承認なしに導入しない
- 主要領域: 投資の基礎、投資信託・ETF、NISA・税金、個別株・企業分析、市場・経済、資産形成

## ステータス
- [x] GitHub リポジトリ作成（Public / main）
- [x] 初期サイトファイル作成
- [x] トップページ・初回解説記事の下書き公開準備
- [x] sitemap.xml / robots.txt の作成
- [x] GitHub Actions Pages デプロイ workflow の作成
- [x] GitHub Pages の設定（Settings > Pages > Build and deployment > Source を GitHub Actions にする設定が反映されたことを、後続の workflow 成功で確認）
- [x] GitHub Actions の build / deploy 成功を確認（run `40097453363` の最新試行）
- [x] 公開URLが表示されることをユーザーのブラウザで確認（2026-10-24。助手側での独立したHTTP検証は未実施）
- [x] トップページの新記事導線、既存記事からの内部リンク、sitemap の記事URL追加を反映
- [ ] 公開URL、内部リンク、sitemap、canonical の公開後動作を確認
- [x] 信託報酬の解説記事を作成し、トップページと sitemap に追加
- [x] 積立投資の基礎記事を作成し、トップページと sitemap に追加
- [ ] Google Search Console の所有権確認（meta tag を追加済み。Search Console 側の「確認」は未実施）と sitemap 送信
- [x] 新NISAの基本記事を公式情報に基づき作成し、トップページと sitemap に追加
- [x] NISAで投資信託を選ぶ際のチェックポイント記事を作成し、公式資料・内部リンク・canonical・sitemapを整備

## 初期コンテンツ
- `index.html`: トップページ
- `investment-trust-vs-etf.html`: 投資信託とETFの違いを解説する初回記事
- `before-you-invest.html`: 投資初心者向け「投資を始める前に確認したい7つのこと」
- `nisa-basics.html`: 新NISAの2つの投資枠、非課税保有限度額、売却後の枠の再利用を解説
- `choose-investment-trust-nisa.html`: NISAで投資信託を選ぶ際の投資対象・運用方針・分散・費用・リスク・目論見書の確認点を解説
- `investment-trust-fees.html`: 信託報酬の仕組み、年率の計算例、その他費用と実質コストの確認方法を解説
- `regular-investing.html`: 積立投資の仕組み、定額購入の計算例、メリット・リスク、積立額の決め方を解説

## 運営・編集ルール
1. 公的機関、取引所、運用会社、企業の公式資料を優先する。
2. 金額、利回り、信託報酬、税制など変わり得る情報は確認日を記載する。
3. 過去のパフォーマンスは将来のリターンを保証しないと明記する。
4. リスク、為替、税金、売買コスト、分配金の扱いを必要に応じて説明する。
5. アフィリエイト申請の審査状況と専用リンク発行状況を分けて管理する。
6. 新規記事は既存記事との重複、内部リンク、title、description、canonical、sitemap を確認する。
7. 個別株の記事は企業の決算資料・適時開示等を根拠にし、予測を事実のように書かない。
8. 公開リポジトリに個人情報、APIキー、ログイン情報、非公開申請情報を保存しない。
9. 証券会社や金融商品の推奨に関して、法令・規制上の問題が疑われる場合は断定を避け、必要に応じて専門家確認を行う。

## 確認結果
- 2026-10-24: リポジトリは存在し、Public、default branch は main。初期ファイルは GitHub 上で取得できることを確認。
- Workflow run `40097453363` は失敗。job `build` の `Configure Pages` ステップで `Get Pages site failed` / HTTP 404。後続の artifact upload と deploy はスキップされた。
- 2026-10-24: run `40097453363` の最新試行で `build` と `deploy` がともに成功。`Configure Pages` と `Upload site artifact`、`Deploy to GitHub Pages` はすべて成功。Pages 設定が有効になり、デプロイ処理が完了したことを確認。
- 初回試行では Node.js 20 の警告も出ていたが、最新試行の成功を妨げてはいない。
- 公開URLはユーザー報告によりブラウザで表示されることを確認（2026-10-24）。助手側の独立したHTTP検証は未実施。
- 2026-10-24: SEO・内部リンク点検を実施。トップページと初回記事に canonical があり、sitemap にトップページと初回記事のURLが登録済み。robots.txt に sitemap URL が記載されていることを確認。
- 2026-10-24: `before-you-invest.html` を新規作成。生活資金、目的、期間、リスク許容度、分散、費用、公式情報の確認を解説し、金融庁・J-FLEC・日本取引所グループの公式資料へリンク。
- 2026-10-24: トップページの「公開予定」カードを新記事へのリンクに変更。既存記事からも新記事への内部リンクを追加し、sitemap に新記事URLを追加。
- 上記変更後の公開URL反映、記事・sitemap の実際のHTTP応答、外部リンクの全件到達性は未確認。GitHub上のファイル更新は完了。

- 2026-10-24: Search Console の sitemap 読み込みエラーは、公開URLでXMLが表示されることをユーザーが確認。`creator-terms-db` と同様の症状のため、サイトマップ内容は変更せず、数日様子見する方針。
- 2026-10-24: `nisa-basics.html` を新規作成。金融庁・国税庁の公式資料を参照し、確認日・リスク・非課税枠のルールを明記。トップページと sitemap に追加。

- 2026-10-24: `choose-investment-trust-nisa.html` を新規作成。金融庁、J-FLEC、資産運用業協会の公式情報を参照し、トップページと sitemap に追加。公開URLの表示・デプロイ結果は未確認。

- 2026-10-24: `investment-trust-fees.html` を新規作成。資産運用業協会、J-FLEC、投資信託協会の公式情報を参照し、計算例・注意点・内部リンクを整備。トップページと sitemap に追加。公開表示・デプロイは未確認。

## 次の作業
- 2026-10-24: Google Search Console の URL プレフィックスプロパティ用 verification meta tag を `index.html` の `<head>` に追加し、GitHub にコミット。Search Console 側の所有権確認と sitemap 送信はユーザー操作待ち。
1. 変更後のGitHub Pagesデプロイ結果を確認し、公開URLで新記事・内部リンク・sitemap が反映されたか検証する。
2. 外部出典リンクの到達性と canonical の整合性を点検する。
3. 必要なら Node.js 24 対応版の Actions へ更新し、警告を解消する。
4. ユーザーが Google Search Console で「確認」を実行し、所有権確認後に sitemap.xml を送信する。
5. 次の記事を一次資料に基づいて追加する。


## 2026-10-24 作業記録
- `regular-investing.html` を新規作成。積立投資、定額購入の例、ドル・コスト平均法の限界、リスク、NISA利用時の注意点を説明。
- トップページに関連記事カードを追加し、`sitemap.xml` に記事URLを登録。
- 参照先として金融庁、J-FLEC、投資信託協会の公式サイトを掲載。
- GitHubへのコミットは完了。公開URLの表示と今回のActionsデプロイ結果は未確認。


## 2026-10-24 内部リンク点検
- 既存の `before-you-invest.html`、`investment-trust-vs-etf.html`、`nisa-basics.html`、`choose-investment-trust-nisa.html` を確認し、新規記事との関連リンクを追加。
- 対象：積立投資、信託報酬、NISAでの投資信託選びへの導線を整備。
- 各記事の title / meta description / canonical を確認。4記事で canonical と description の設定を確認。
- GitHub上のファイル内容を再取得して反映確認予定。公開URLのHTTP応答と今回のActions実行結果は未確認。


## 2026-10-24 技術SEO・内部リンク点検
- GitHub main の全7 HTMLページを再取得して確認。各ページに title と meta description があり、canonical はサイトURLの形式と一致。
- 相対内部リンクのリンク先はすべて既存HTMLファイルを参照しており、未解決の相対リンクは検出されなかった。
- sitemap.xml の7 URLはリポジトリ内のHTMLページと一致し、すべて想定の GitHub Pages ホストを使用。robots.txt に sitemap URL が記載されている。
- これらはGitHub上のファイル内容に対する静的チェックであり、公開URLのHTTP応答や外部リンク先の到達性を保証するものではない。

## 2026-10-24 積立投資記事の図解追加
- `images/regular-investing-diagram.svg` を新規作成。毎回3,000円を積み立てる仮定例（価格1,000円・750円・600円で購入数量が3口・4口・5口、合計9,000円・12口、平均購入価格750円/口）を図示。
- `regular-investing.html` にレスポンシブ表示の図解と日本語の代替テキスト・キャプションを追加。
- 数値は記事本文にある説明用の仮定例と一致。図は利益や損失回避を保証するものではない旨を明記。
- GitHub main へのファイル追加・記事更新コミットは完了。今回の変更後のGitHub Actionsと公開URLでの表示確認はこれから確認する。

## 2026-10-24 トップページのデザイン改善
- `images/home-investing-illustration.svg` を新規追加。外部の有料画像サービスを使わず、投資学習をテーマにしたオリジナルSVGを作成。
- `index.html` のヒーロー領域を2カラム構成にし、画像・主要CTA（解説記事を読む／テーマから探す）を追加。
- 編集方針の特徴（公式情報を優先、リスクも説明、初心者向け）を短いカードで見せ、記事カードの余白・ホバー状態・2列レイアウトを改善。スマートフォン向けの1列表示も設定。
- title、description、canonical、Google Search Console verification meta、記事リンク、サイトマップは変更していない。
- 変更ファイル：`index.html`、`images/home-investing-illustration.svg`、本ファイル。
- GitHubへのコミットは完了。デプロイ結果と公開URLでの実表示は次に確認する。


## 2026-10-24 トップページのヒーロー高さ調整
- ユーザーの指摘を受け、トップページ上部の余白とイラストを縮小。
- ヒーロー上下の余白を縮め、見出しサイズ・CTA上部余白・画像最大幅を調整。スマートフォン表示でも画像を小さくし、本文に早く到達できる構成に変更。
- 変更ファイル：`index.html`、本ファイル。
- `index.html` の変更コミット：`b942ab51b70fa63d9bbb6f05cab60c80bc61c9f4`。
- この変更後のデプロイ結果と公開URLでの実表示は未確認。


## 2026-10-24 トップページのヒーロー領域を追加縮小
- ユーザー希望に合わせ、ファーストビューの高さをさらに縮小。
- デスクトップは上下余白・見出し・イラスト・CTAをさらにコンパクトに調整。モバイルではヒーロー内のイラストを非表示にして、記事への到達を早める。
- 変更ファイル：`index.html`、本ファイル。
- `index.html` の変更コミット：`c7c3a0016899f41534e89c91d8b9826ec8282eff`。
- デプロイと公開URLでの実表示は未確認。


## 2026-10-24 ヒーロー高さの原因修正
- ユーザーから公開画面でもヒーローが大きいままと報告あり。原因を調査し、`index.html` のヒーロー画像に HTML の `height="560"` 属性がある一方、CSSで `height:auto` を指定していなかったため、画像の高さが固定されてセクションを押し広げていたことを特定。
- `.hero-art` に `height:auto` を追加し、幅に応じて画像の高さが比例して縮むよう修正。
- 変更ファイル：`index.html`。
- GitHubへのコミットは完了。今回のデプロイ結果と公開URLでの実表示は確認待ち。


## 2026-10-24 分散投資の解説図を追加
- `images/diversification-basics.svg` を新規作成。集中投資と、資産・地域・業種などに分ける分散投資の考え方を比較するオリジナル図解。
- `before-you-invest.html` の「分散・積立・長期」節に図解、代替テキスト、キャプションを追加。モバイル画面でも幅に合わせて縮小するレスポンシブ表示。
- 図中に、分散しても市場全体の下落などによる損失を防ぐ保証ではない旨を明記。
- 変更ファイル：`images/diversification-basics.svg`、`before-you-invest.html`、本ファイル。
- GitHubへの反映は完了。デプロイ結果と公開URLでの実表示は次に確認する。


## 2026-10-24 記事の図解を追加
- 既存の図解がある記事（`before-you-invest.html`、`nisa-basics.html`、`regular-investing.html`）に加え、以下の記事に内容に合わせたオリジナルSVG図解を追加。
- `investment-trust-vs-etf.html`：投資信託とETFの売買方法・価格の違い（`images/fund-vs-etf-diagram.svg`）。
- `choose-investment-trust-nisa.html`：投資信託を選ぶ7つの確認項目（`images/fund-selection-checklist.svg`）。
- `investment-trust-fees.html`：信託報酬とその他費用の構造、単純計算例（`images/investment-trust-fees-diagram.svg`）。
- 画像に代替テキストとキャプションを付け、記事側でレスポンシブ表示するCSSを追加。費用図は仮定例であること、図解が利益を保証しないことを明記。
- 変更ファイル：上記3記事、上記3 SVG、本ファイル。
- GitHub main への反映は完了。GitHub Actions の最新結果と公開URLでの表示確認は未確認。


## 2026-10-24 図解SVGのエラー修正
- ユーザー報告により `images/fund-selection-checklist.svg` を再確認し、SVGのマークアップを簡潔な構造に整理して更新。
- 修正コミット：`80c860dab18371a85acfdff248d45d55e1dd226e`。
- GitHubから更新後のファイルを再取得して内容を確認。GitHub Pagesでの表示およびActionsの結果は未確認。


## 2026-10-24 既存記事の図解を追加
- 既存の6解説記事すべてに、記事内容に沿った追加図解を1点ずつ追加。既存図解は残し、各図に日本語の代替テキストとキャプションを付与。
- 新規SVG：`images/before-investing-flow.svg`（投資前の確認フロー）、`images/nisa-allowances.svg`（新NISAの年間枠・生涯枠）、`images/fund-cost-layers.svg`（投資信託の費用タイミング）、`images/fund-vs-etf-decision.svg`（投資信託とETFの比較ポイント）、`images/nisa-selection-flow.svg`（NISAの商品選び手順）、`images/regular-investing-outcomes.svg`（積立投資でも成果は変動することを示す模式図）。
- 対象記事：`before-you-invest.html`、`nisa-basics.html`、`investment-trust-fees.html`、`investment-trust-vs-etf.html`、`choose-investment-trust-nisa.html`、`regular-investing.html`。
- 図はレスポンシブCSSで表示し、制度数値・模式図の注意書きを付記。新NISA図は年間枠・生涯枠の関係を説明するもので、制度の最新条件は公式情報での確認を促す。
- GitHub main への反映は完了。公開URLでの実表示と今回のGitHub Actions結果は未確認。


## 2026-10-24 トップページをタイル型導線に再構成
- ユーザー希望に合わせ、トップページの「テーマから探す」にあった記事未作成のカテゴリタイルを、既存6記事へ直接遷移するクリック可能なタイルに再構成。
- 6タイルは「投資前の基礎」「新NISA」「投資信託とETFの比較」「NISAの商品選び」「信託報酬・費用」「積立投資」に対応。タイル全体をリンクにし、アイコン・短い説明・遷移ラベルを配置。
- カードをデスクトップ3列・モバイル1列で表示し、フォーカス表示、ホバー、タッチしやすい余白を整備。既存のtitle、description、canonical、Search Console verification、サイトマップは維持。
- 変更ファイル：`index.html`。
- コミット：`29b387d04dac70bc0b3fa12473c70ae76125169e`。公開URLでの実表示とGitHub Actions結果は未確認。


## 2026-10-25 トップページのタイルに図解イラストを追加
- 既存6記事へのタイル導線に、記事テーマに沿ったオリジナルSVGの小さな図解イラストを追加。
- 新規画像：`images/tile-before-investing.svg`、`images/tile-nisa.svg`、`images/tile-fund-etf.svg`、`images/tile-selection.svg`、`images/tile-fees.svg`、`images/tile-regular-investing.svg`。
- `index.html` のタイルに画像と日本語の代替テキストを設定。画像はレスポンシブ表示、遅延読み込みに対応し、既存の記事リンク・SEOメタ情報を維持。
- GitHub main への反映済み。コミット：`2aecfa05135c8bd87d1625219a244c342e60a27c`。
- GitHub Actions のデプロイ結果と公開URLでの実表示は未確認。


## 2026-10-25 トップページの視認性・華やかさを改善
- ユーザー要望に合わせ、トップページを明るい配色（淡いミント・ブルー・ラベンダー、濃い青緑のCTA）へ調整し、見出し階層と余白を整理。
- 記事タイルの図解エリアを目立たせ、カード全体がクリック可能であることをホバー時の浮き上がり・画像の軽い拡大・明確なCTAボタンで示す。キーボードフォーカスも強調し、動きを減らす設定にも配慮。
- モバイルでは図解を含めて縦並びにし、ヒーロー画像も小さく表示。ヘッダーの「投資の基礎」リンク先が存在しないアンカーだったため、編集方針の特徴セクションに `id="basics"` を付けて修正。
- 変更ファイル：`index.html`、本ファイル。
- `index.html` のコミット：`0a8ee0abea29dc27a55e99ae1472f8b560df81a5`。GitHub main への反映済み。GitHub Actions と公開画面での最終表示は未確認。
