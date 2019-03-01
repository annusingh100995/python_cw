
import random
import unittest


print("UNIT TEST SECOND")

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq,5):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()

