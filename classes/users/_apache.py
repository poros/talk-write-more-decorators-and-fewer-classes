from statmonster import Log
from utils import decode_apache


class ApacheBaseLog(Log):
    codec = decode_apache
