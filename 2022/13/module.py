from dataclasses import dataclass, field
from enum import Enum

class CheckResult(Enum):
    IN_ORDER = 1,
    NOT_IN_ORDER = 2
    UNDECIDED = 3


@dataclass
class Pair:
    content: list = field(default_factory=list)
    
    def is_in_order_with(self, other_pair) -> bool:
        result = True
        for index, element in enumerate(self.content):
            other_element = Pair._other_element(other_pair.content, index)
            check_result = Pair._check_order(element, other_element)
            
            if check_result == CheckResult.IN_ORDER:
                return True
            elif check_result == CheckResult.NOT_IN_ORDER:
                return False
            else:
                continue

        return True

    @staticmethod
    def _check_order(element, other_element) -> CheckResult:
        if other_element is None:
            return CheckResult.NOT_IN_ORDER
        elif (isinstance(element, int) & isinstance(other_element, int)):
            return Pair._check_ints(element, other_element)
        elif (isinstance(element, list) & isinstance(other_element, list)):
            return Pair._check_lists(element, other_element)
        elif (isinstance(element, list) & isinstance(other_element, int)):
            return Pair._check_lists(element, [other_element])
        else:
            return Pair._check_lists([element], other_element)

    @staticmethod
    def _check_ints(element: int, other_element: int):
        if element < other_element:
            return CheckResult.IN_ORDER
        elif element > other_element:
            return CheckResult.NOT_IN_ORDER

        return CheckResult.UNDECIDED

    @staticmethod
    def _check_lists(element_list: list, other_element_list: list):
        if element_list == other_element_list:
            return CheckResult.UNDECIDED

        for index, element in enumerate(element_list):
            other_element = Pair._other_element(other_element_list, index)
            check_result = Pair._check_order(element, other_element)
            if (check_result == CheckResult.UNDECIDED):
                continue
            else:
                return check_result

        return CheckResult.IN_ORDER

    @staticmethod
    def _other_element(other_pair_content: list, index: int):
        if (index < len(other_pair_content)):
            return other_pair_content[index]

        return None

    def __str__(self) -> str:
        return f'{self.content}'