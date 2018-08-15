# ボタンワンポチでマージコミットする
* 開発時に何個もあるリポジトリを毎日手動でテスト環境用のブランチにマージしてくのめんどくさよね ってのを解決したソースコード
* 事故怖いからとりあえず今は手動で叩いてる

Lambdaにないモジュールは、lambda_function.pyと一緒にzip化してアップロードする必要があるので、以下のようにプロジェクト直下にモジュールをインストールする
```
pip install requests .
```
残りは何もせずにimportさえしておけばLambdaで使えるモジュールだったはず...

# 使い方
AWS Lambdaにあげて空オブジェクトを渡してテスト実行

サクッと改造してできそうなこと
* CloudWatchからSchedule Eventを作成して定期実行
* ブランチ名等定数化されている部分を引数で渡せるようにして動的にbaseブランチとheadブランチを指定できるようにする
* ApiGatewayを使って外から叩けるようにする(slackコマンドと連携とか)
