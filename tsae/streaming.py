import tweepy
import time
import typing
import schedule


def id2date(id: int)->int:
    return (id >> 22)+1288834974657


T = typing.TypeVar('T')


def list_split(n: int, list: typing.List[T])->typing.List[typing.List[T]]:
    return [list[i:i+n] for i in range(0, len(list), n)]


def default_error_handling(e: tweepy.TweepError):
    print(e.reason)


class StreamingEmulate:
    def __init__(self, api: tweepy.API, list_name: str, callback: typing.Callable[[tweepy.Status], None], check_list_error: typing.Callable[[tweepy.TweepError], None]=default_error_handling, sync_list_error: typing.Callable[[tweepy.TweepError], None]=default_error_handling):
        self.api = api
        self.list_name = list_name
        self.list_id = self.find_list()
        self.last = int(time.time()*1000)
        self.callback = callback
        self.check_list_error = check_list_error
        self.sync_list_error = sync_list_error

        self.sync_list()

    def find_list(self)->int:
        for x in self.api.lists_all():
            if x.name == self.list_name:
                return x.id
        return self.api.create_list(name=self.list_name, mode="private").id

    def check_list(self):
        ts = self.api.list_timeline(count=100, list_id=self.list_id)
        for status in ts:
            if self.last < id2date(status.id):
                self.callback(status)
        if len(ts) != 0:
            self.last = id2date(ts[0].id)

    def find_friends(self)->typing.Set[int]:
        return set(list(tweepy.Cursor(self.api.friends_ids, user_id=self.api.me().id).items()))

    def find_members(self)->typing.Set[int]:
        return set([x.id for x in tweepy.Cursor(self.api.list_members, list_id=self.list_id).items()])

    def sync_list(self):
        friends = self.find_friends() | {self.api.me().id}
        members = self.find_members()

        for ids in list_split(100, list(friends-members)):
            self.api.add_list_members(list_id=self.list_id, user_id=ids)

        for ids in list_split(100, list(members-friends)):
            self.api.remove_list_members(list_id=self.list_id, user_id=ids)

    def check_list_task(self):
        try:
            self.check_list()
        except tweepy.TweepError as e:
            self.check_list_error(e)

    def sync_list_task(self):
        try:
            self.sync_list()
        except tweepy.TweepError as e:
            self.sync_list_error(e)

    def run(self, sync_list_minutes: int=30, check_list_seconds: int=2):
        schedule.every(sync_list_minutes).minutes.do(self.sync_list_task)
        schedule.every(check_list_seconds).seconds.do(self.check_list_task)

        while True:
            schedule.run_pending()
            time.sleep(1)
