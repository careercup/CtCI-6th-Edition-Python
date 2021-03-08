import enum
import random


class Gender(enum.Enum):
    BOY = enum.auto()
    GIRL = enum.auto()


def simulate_child() -> Gender:
    return random.choice([Gender.BOY, Gender.GIRL])


class Family:
    def __init__(self, num_boys: int, num_girls: int) -> None:
        self.num_boys = num_boys
        self.num_girls = num_girls


def simulate_family() -> Family:
    num_boys = sum(1 for _ in iter(simulate_child, Gender.GIRL))
    return Family(num_boys=num_boys, num_girls=1)


def simulate_apocalypse(num_families: int) -> float:
    total_boys = total_girls = 0
    for _ in range(num_families):
        family = simulate_family()
        total_boys += family.num_boys
        total_girls += family.num_girls
    return total_boys / (total_boys + total_girls)


def test_apocalypse():
    # ratio should be really close to 0.5
    ratio = simulate_apocalypse(30000)
    assert abs(0.5 - ratio) < 0.01


if __name__ == "__main__":
    n = int(input("How many families should we simulate? "))
    print("Proportion of children that are boys:", simulate_apocalypse(n))
