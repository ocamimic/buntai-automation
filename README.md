# buntai-automation
文体の集計を自動化する。
自分で使う用なので、ファイルのパスなどはローカルのまま。
コピペして使用する場合は適宜変更してください。

# 使用するとき用のメモなど
## 作成時点でのファイル構成
```
vscode code
└python
 └gss
  ├main.py
  └gss_credential.json
```

## スプレッドシート側の権限設定
共有設定より、リンクを知っている全員が閲覧可能に。
もっと良いやり方があるかもしれない。

## 参考にしたページなど
gss_credential.jsonの作成や使用はこちらを参考にしました↓
[[python]Googleスプレッドシートの連携（読み込み、書き込み）する方法](https://mashimashi.net/skill/821/)

gspreadのドキュメントです↓
[Examples of gspread Usage](https://docs.gspread.org/en/v6.1.3/user-guide.html#getting-a-cell-value)

作品をシャッフルする部分で参考にしました↓
[Python リストを参照してリストをソート](https://qiita.com/ossyaritoori/items/c567d63596401d0d9590)
