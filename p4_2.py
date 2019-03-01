import random
import unittest


class TestSequenceFunctions():
    def test_shuffel(self):
        seq = list(range(10))
        print("Seq before is {}".format(seq))
        random.shuffle(seq)
        print("Seq after is {}".format(seq))
        seq.sort()
        print("Seq sorted is {}".format(seq))


if __name__ == '__main__':
    TestSequenceFunctions().test_shuffel()


print("UNITEST")

class TestSequenceFunstions(unittest.TestCase):
    def test_shuffle(self):
        seq = list(range(10))
        random.shuffle(seq)
        seq.sort()
        self.assertEqual(seq,list(range(10)))



if __name__ == '__main__':
    unittest.main()














