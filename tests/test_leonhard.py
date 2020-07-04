import unittest
from leonhard import leonhard


class TestLeonhard(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(1, leonhard.foo())


if __name__ == '__main__':
    unittest.main()