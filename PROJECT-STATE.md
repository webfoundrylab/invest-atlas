## 2026-11-04 相関係数2記事を公開キューへ登録
- ユーザーによる記事内容確認は完了。対象は `correlation-coefficient.html` と `asset-correlation-comparison.html`。再度の内容確認は不要。
- `correlation-coefficient.html`：GPIFの2025年4月適用・基本ポートフォリオ前提資料に合わせ、相関係数と標準偏差を同一資料の値に統一。国内債券2.60%、国内株式19.19%、相関−0.254による50:50試算を9.35%へ修正（相関0は9.68%、相関+1は10.90%）。公式PDFを参考資料へ追加。
- `asset-correlation-comparison.html`：22 ETF・全231ペアの行列を点検し、負相関13ペア、最低値はTLT×DBCの−0.31と確認。本文の誤記（BIL×TLT）を訂正。EWJ行は個別相関データと照合。米国債5満期区分はSafe Rateの指数仕様・2009〜2025年の年次トータルリターンを確認。
- 記事間リンクを整備。比較記事から相関係数解説へリンクし、既存の `diversification-basics.html` と `asset-allocation-guide.html` に文脈付きリンクを追加する更新ファイル・台帳更新を比較記事パッケージへ同梱。
- ユーザーから `preview.bat` のプレビュー表示を確認できたとの報告あり。これを受け、両記事の `visuals_complete` / `thumbnail_svg` を true、`draft_status` を `ready` に更新。
- Private stock の `queue.json` 末尾へ、`correlation-coefficient.html` → `asset-correlation-comparison.html` の順で `scheduled` 登録。queue commit：`18b8e1d8ac169b8bcd16e4f6a25c1a39c24a5d2d`。
- 残作業：GitHub Actions の手動 `dry-run` を実行し、公開側ビルド・台帳・リンク検証を確認する。現時点でdry-runは未実施・未合格。手動実行は公開ではなく検証のみを選択する。
- 運用上の不整合：`ARTICLE-WORKFLOW.md` / `README.md` はJST 05:00・17:00の2回を記載するが、現行 `.github/workflows/publish.yml` はJST 05:00相当のcronしか持たない。17:00トリガーの追加が未対応。

