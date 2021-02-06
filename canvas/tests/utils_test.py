import unittest
import sys
from datetime import timedelta
from pathlib import Path

if __name__ == '__main__' and __package__ is None:
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[3]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    __package__ = 'CanvasPython.canvas'

from canvas.utils.jwt import create_access_token
from canvas.utils.jwt import ACCESS_TOKEN_EXPIRES_MINUTES

class TestJwt(unittest.TestCase):
    def test_counting(self):
        self.assertEqual(2, 2)

    # def test_token_creating(self):
    #     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    #     access_token = create_access_token(data={"sub": username},
    #                                        expires_delta=access_token_expires)
    #     print(access_token)


if __name__ == "__main__":
    unittest.main()
