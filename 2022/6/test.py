import unittest

from module import Datastream

class Day6Test(unittest.TestCase):
    
    def test_part1(self):
        self.assertEqual(Datastream('mjqjpqmgbljsphdztnvjfqwrcgsmlb').start_of_packet_marker(), 7)
        self.assertEqual(Datastream('bvwbjplbgvbhsrlpgdmjqwftvncz').start_of_packet_marker(), 5)
        self.assertEqual(Datastream('nppdvjthqldpwncqszvftbrmjlhg').start_of_packet_marker(), 6)
        self.assertEqual(Datastream('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg').start_of_packet_marker(), 10)
        self.assertEqual(Datastream('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw').start_of_packet_marker(), 11)

    def test_part2(self):
        self.assertEqual(Datastream('mjqjpqmgbljsphdztnvjfqwrcgsmlb').start_of_message_marker(), 19)
        self.assertEqual(Datastream('bvwbjplbgvbhsrlpgdmjqwftvncz').start_of_message_marker(), 23)
        self.assertEqual(Datastream('nppdvjthqldpwncqszvftbrmjlhg').start_of_message_marker(), 23)
        self.assertEqual(Datastream('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg').start_of_message_marker(), 29)
        self.assertEqual(Datastream('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw').start_of_message_marker(), 26)

if __name__ == '__main__':
    unittest.main()