# ボタンワンポチで管理下のリポジトリをターゲットのリポジトリにマージする
* 開発時に何個もあるリポジトリを毎日手動でテスト環境用のブランチにマージしてくのめんどくさよね ってのを解決するプロダクト
* 事故怖いからとりあえず今は手動で叩いてる

Lambdaにないけど使いたいモジュールを丸ごとzip化してアップロードするので以下のようにモジュールをインストールする
```
pip install requests .
```

# 使い方
AWS Lambdaにあげてからオブジェクトを渡してテスト実行

サクッと改造してできそうなこと
* CloudWatchからSchedule Eventを作成して定期実行
* ブランチ名等定数化されている部分を引数で渡せるようにして動的にbaseブランチとheadブランチを指定できるようにする
* ApiGatewayを使って外から叩けるようにする(slackコマンドと連携とか)
