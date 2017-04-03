import json

import util


class Headers:
   

    def __init__(self, ai5, debug, random, sdkv):
        self.ai5 = ai5
        self.debug = debug
        self.random = random
        self.sdkv = sdkv

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def get_headers(json_string):
        json_ = json.loads(json_string)
        return Headers(**json_)


class Post:
   

    def __init__(self, event, ts):
        self.event = event
        self.ts = ts

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def get_post(json_string):
        json_ = json.loads(json_string)
        return Post(**json_) 

class Bottle:
   

    def __init__(self, timestamp, game_id):
        self.timestamp = timestamp
        self.game_id = game_id
        self.timestamp_in_seconds = util.datetime_to_seconds(timestamp)

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def get_bottle(json_string):
        json_ = json.loads(json_string)
        return Bottle(**json_)


class Instance:
  
    def __init__(self, headers, post, bottle):
        self.headers = headers
        self.post = post
        self.bottle = bottle

    def to_json(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def get_instance(json_string):
        json_ = json.loads(json_string)
        headers = Headers.get_headers(json.dumps(json_["headers"]))
        post = Post.get_post(json.dumps(json_["post"]))
        bottle = Bottle.get_bottle(json.dumps(json_["bottle"]))
        return Instance(headers, post, bottle)


class Session:
  
    def __init__(self, ai5, valid_sessions, total_sessions, avg_session_time):
        self.ai5 = ai5
        self.valid_sessions = valid_sessions
        self.total_sessions = total_sessions
        self.avg_session_time = avg_session_time

    def to_json(self):
        return json.dumps(self.__dict__)
