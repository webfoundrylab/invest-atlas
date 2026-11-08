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
