from dataclasses import dataclass


@dataclass
class Datastream:
    stream: str

    def start_of_packet_marker(self):
        return Datastream.__find_marker(self.stream, 4)

    def start_of_message_marker(self):
        return Datastream.__find_marker(self.stream, 14)

    @staticmethod
    def __find_marker(stream, unique_characters_needed):
        start_index = unique_characters_needed-1
        for i in range(start_index, len(stream)):
            if len(set(stream[i-start_index:i+1])) == unique_characters_needed:
                return i + 1

    