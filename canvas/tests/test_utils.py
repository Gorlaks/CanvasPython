import unittest

from canvas.utils.hashing import hash_password


class TestUtils(unittest.TestCase):

  def test_hash_password(self):
    self.assertEqual(2, 2)


if __name__ == "__main__":
  unittest.main()