import unittest

from module import CommandRunner

class Day7Test(unittest.TestCase):
    
    def test_part1(self):
        self.assertEqual(CommandRunner().run_for_directories(["$ ls","1 b.txt"]).sum_of_big_directory_sizes(), 1)
        self.assertEqual(CommandRunner().run_for_directories(["$ ls","14848514 b.txt"]).sum_of_big_directory_sizes(), 0)
        self.assertEqual(CommandRunner().run_for_directories(["$ ls","1 b.txt","1 a.txt"]).sum_of_big_directory_sizes(), 1+1)
        self.assertEqual(CommandRunner().run_for_directories(["$ ls","dir a","1 b.txt","1 a.txt"]).sum_of_big_directory_sizes(), 1+1)

        self.assertEqual(CommandRunner().run_for_directories(["$ ls","dir a","100001 b.txt","100001 a.txt","$ cd a", "$ ls", "1 c.txt"]).sum_of_big_directory_sizes(), 1)
        self.assertEqual(CommandRunner().run_for_directories(["$ ls","dir a","1 b.txt","1 a.txt","$ cd a", "$ ls", "1 c.txt"]).sum_of_big_directory_sizes(), 3+1)

        self.assertEqual(CommandRunner().run_for_directories(["$ ls","dir a","dir b","1 b.txt","1 a.txt","$ cd a", "$ ls", "1 c.txt", "$ cd ..", "$ cd b", "$ ls", "1 d.txt"]).sum_of_big_directory_sizes(), 4+1+1)

        self.assertEqual(CommandRunner().run_for_directories([
            "$ ls",
            "dir a",
            "dir b",
            "$ cd a",
            "$ ls",
            "dir c",
            "$ cd c",
            "$ ls",
            "50_001 e.txt",
            "$ cd ..",
            "$ cd ..",
            "$ cd b",
            "$ ls",
            "dir c",
            "$ cd c",
            "$ ls",
            "50_001 e.txt",
        ]).sum_of_big_directory_sizes(), 50_001 + 50_001 + 50_001 + 50_001)

    def test_part2(self):
        self.assertEqual(CommandRunner().run_for_directories([
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst", 
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d"
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k"
        ]).size_of_smallest_dir_to_delete(), 24933642)

if __name__ == '__main__':
    unittest.main()