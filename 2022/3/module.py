from dataclasses import dataclass

def to_ord(common_char):
    offset = 38 if common_char.isupper() else 96 
    return ord(common_char) - offset


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
    
        return to_ord(common_char)


@dataclass
class ElfGroup:
    elf_1: str
    elf_2: str
    elf_3: str

    def priority(self):
        elf_1_chars = set(self.elf_1)
        elf_2_chars = set(self.elf_2)
        elf_3_chars = set(self.elf_3)

        common_chars = elf_1_chars & elf_2_chars & elf_3_chars
        
        if not common_chars:
            return 0

        common_char = list(common_chars)[0]

        return to_ord(common_char)