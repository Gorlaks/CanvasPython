import unittest
import sys
from pathlib import Path

if __name__ == '__main__' and __package__ is None:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[3]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    __package__ = 'CanvasPython.canvas.utils'

from ..utils.hashing import hash_password


class TestUtils(unittest.TestCase):

    def test_hash_password(self):
        self.assertEqual(2, 2)


if __name__ == "__main__":
    unittest.main()
