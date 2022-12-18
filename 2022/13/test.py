import unittest

from module import Pair

class Test(unittest.TestCase):

    def test_part1(self):
        self.assertTrue(Pair().is_in_order_with(Pair()))

        self.assertTrue(Pair([1]).is_in_order_with(Pair([2])))
        self.assertFalse(Pair([2]).is_in_order_with(Pair([1])))
        self.assertTrue(Pair([1,1]).is_in_order_with(Pair([1,2])))
        self.assertTrue(Pair([]).is_in_order_with(Pair([3])))
        self.assertFalse(Pair([3]).is_in_order_with(Pair([])))

        self.assertTrue(Pair([1,[1]]).is_in_order_with(Pair([1,[2]])))
        self.assertFalse(Pair([1,[2]]).is_in_order_with(Pair([1,[1]])))
        self.assertFalse(Pair([[],2]).is_in_order_with(Pair([[],1])))
        self.assertTrue(Pair([[],1]).is_in_order_with(Pair([[],2])))
        self.assertTrue(Pair([1,[1,1]]).is_in_order_with(Pair([1,[1,2]])))
        self.assertFalse(Pair([1,[1,2]]).is_in_order_with(Pair([1,[1,1]])))

        self.assertTrue(Pair([1]).is_in_order_with(Pair([[2]])))
        self.assertFalse(Pair([2]).is_in_order_with(Pair([[1]])))

        self.assertTrue(Pair([[1]]).is_in_order_with(Pair([2])))
        self.assertFalse(Pair([[2]]).is_in_order_with(Pair([1])))
        

        self.assertTrue(Pair(([[4],3])).is_in_order_with(Pair([[5],2])))
        self.assertFalse(Pair(([[5],2])).is_in_order_with(Pair([[4],3])))

        self.assertTrue(Pair([1,1,3,1,1]).is_in_order_with(Pair([1,1,5,1,1])))
        self.assertTrue(Pair([[1],[2,3,4]]).is_in_order_with(Pair([[1],4])))
        self.assertFalse(Pair([9]).is_in_order_with(Pair([[8,7,6]])))
        self.assertTrue(Pair([[4,4],4,4]).is_in_order_with(Pair([[4,4],4,4,4])))
        self.assertFalse(Pair([7,7,7,7]).is_in_order_with(Pair([7,7,7])))
        self.assertTrue(Pair([]).is_in_order_with(Pair([3])))
        self.assertFalse(Pair([[[]]]).is_in_order_with(Pair([[]])))
        self.assertFalse(Pair([1,[2,[3,[4,[5,6,7]]]],8,9]).is_in_order_with(Pair([1,[2,[3,[4,[5,6,0]]]],8,9])))
        self.assertTrue(Pair([[], [], [[2, [2, 0, 8, 6], 4, [6, 1, 7]], 7, [[4, 7, 10, 7, 8], [3, 7, 1, 4, 0]]]])
            .is_in_order_with(Pair([[[[], 6, 6, []]], [[[], [4, 7, 8, 4], 10, [8, 2, 3], 10], [[2], [10, 0], 6, 8, [2, 5, 3, 0]], 5, [[10, 5], [3, 4, 0], [0], [10, 0, 2, 4], 7]]])))

    def test_part2(self):
        self.assertEqual([Pair([]), Pair([[]])],sorted([Pair([[]]),Pair([])]))        


if __name__ == '__main__':
    unittest.main()
