import unittest
from env import Env

class TestEnv(unittest.TestCase):
    def test_dummy(self):
        env = Env()
        self.assertIsInstance(env, Env)