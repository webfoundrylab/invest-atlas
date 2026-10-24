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
- [ ] 公開URL、内部リンク、sitemap、canonical を公開後に検証
- [ ] Google Search Console 登録と sitemap 送信
- [ ] 追加記事の検索意図・一次情報・重複確認

## 初期コンテンツ
- `index.html`: トップページ
- `investment-trust-vs-etf.html`: 投資信託とETFの違いを解説する初回記事

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
- 公開URLはユーザー報告によりブラウザで表示されることを確認（2026-10-24）。助手側の独立したHTTP検証は未実施。記事ページと sitemap の表示・応答、および内部リンク／canonical の整合性は未確認。

## 次の作業
1. 初回記事と sitemap の表示・応答、内部リンク、canonical の整合性を検証する。
2. 必要なら Node.js 24 対応版の Actions へ更新し、警告を解消する。
3. 次の記事を一次資料に基づいて追加する。
