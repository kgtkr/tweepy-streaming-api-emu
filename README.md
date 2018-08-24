# tweepy-streaming-api-emu

ストリーミングAPIが廃止されたので、フォローしている人をリストに入れてなるべくリアルタイムでTLを取得するライブラリ

# インストール

```
$ pip3 install tweepy-streaming-api-emu
```

# サンプル

```python
from tsae import StreamingEmulate
import tweepy
import os


def callback(s: tweepy.Status):
    print(s.text)


ck = os.environ["CK"]
cs = os.environ["CS"]
tk = os.environ["TK"]
ts = os.environ["TS"]
list_name = os.environ["LIST_NAME"]

auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(tk, ts)
api = tweepy.API(auth)

StreamingEmulate(api, list_name, callback).run()
```

# オプション

## StreamingEmulate
* list_name:フォローしてる人を入れるリストの名前
* callback:TLが更新されたときのコールバック
* check_list_error:リストTL取得に失敗したときのエラーハンドリングコールバック
* sync_list_error:リスト同期に失敗したときのエラーハンドリングコールバック

## StreamingEmulate#run

* sync_list_minutes:リスト同期間隔。単位分。デフォルト30
* check_list_seconds:リストTL取得間隔。単位秒。デフォルト2