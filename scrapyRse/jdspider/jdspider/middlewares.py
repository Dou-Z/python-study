from random import choice
from jdspider.settings import USER_AGENT_LIST

class RandomAgentMiddleware(object):
    def process_request(self,request,spider):
        ua = choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = ua

