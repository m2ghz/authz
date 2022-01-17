from os import environ
import os

class Config(object):
        ENV = os.environ.get("SKOB_AUTHZ_ENV", "PRODUCTION")
        DEBUG = int(os.environ.get("SKOB_AUTHZ_DEBUG", "0"))
        TESTING = int(os.environ.get("SKOB_AUTHZ_TESTING", "0"))
