import unittest

from module import CommandRunner

class Day7Test(unittest.TestCase):
    
    def test_part1(self):
        self.assertEqual(CommandRunner().run_for_directories(["$ ls","1 b.txt"]).sum_of_big_directory_sizes(), 1)
        self.assertEqual(CommandRunner().run_for_directories(["$ ls","14848514 b.txt"]).sum_of_big_directory_sizes(), 0)
        self.assertEqual(CommandRunner().run_for_directories(["$ ls","1 b.txt","1 a.txt"]).sum_of_big_directory_sizes(), 1+1)
        self.assertEqual(CommandRunner().run_for_directories(["$ ls","dir a","1 b.txt","1 a.txt"]).sum_of_big_directory_sizes(), 1+1)

        self.assertEqual(CommandRunner().run_for_directories(["$ ls","dir a","100001 b.txt","100001 a.txt","$ cd a", "$ ls", "1 c.txt"]).sum_of_big_directory_sizes(), 1)

if __name__ == '__main__':
    unittest.main()