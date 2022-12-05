from dataclasses import dataclass

print(ord('a'))
print(ord('b'))
print(ord('A'))
print(ord('B') - ord('A'))



@dataclass
class RuckSack:
    compartment_1: str
    compartment_2: str

    def priority(self):
        compartment_1_chars = set(self.compartment_1)
        compartment_2_chars = set(self.compartment_2)

        common_chars = compartment_1_chars & compartment_2_chars

        if not common_chars:
            return 0
        
        common_char = list(common_chars)[0]
    
        offset = 38 if common_char.isupper() else 96 
        return ord(common_char) - offset