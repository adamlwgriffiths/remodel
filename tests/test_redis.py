import unittest
import string
from secrets import choice
from modelus import *
from modelus.backends.redis import RedisDatabase
from redis_mock import Redis
from backend import TestBackend

class TestRedisDatabase(TestBackend):
    def setUp(self):
        self.redis = Redis()
        self.db = RedisDatabase(self.redis)

    def tearDown(self):
        self.redis.flushall()

    def test_not_found(self):
        self.not_found()

    def test_model_and_fields(self):
        self.model_and_fields()

    def test_foreign_keys(self):
        self.foreign_keys()

    @unittest.skip('Reverse foreign keys not implemented')
    def test_reverse_foreign_keys(self):
        self.reverse_foreign_keys()
