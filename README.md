# tweepy-streaming-api-emu

```
$ pip3 install tweepy-streaming-api-emu
```

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