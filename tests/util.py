import unittest

from tictactoe import util

class Util(unittest.TestCase):
    def test(self):
        hashes = []
        for i in range(10000):
            h = util.hashval(i)
            print(i, h)
            self.assertNotIn(h, hashes)
            hashes.append(h)

if __name__ == "__main__":
    unittest.main()
