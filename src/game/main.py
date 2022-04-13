from typing import List, Tuple, Union


RULES: List[Tuple[str, str]] = [
    ("Paper", "Rock"),
    ("Rock", "Scissor"),
    ("Scissor", "Paper")
]


def get_winner(entity1: str, entity2: str) -> Union[str, None]:
    if entity1 == entity2:
        return None
    if (entity1, entity2) in RULES:
        return entity1
    elif (entity2, entity1) in RULES:
        return entity2
    raise KeyError("Invalid entities")


def main() -> str:
    print("Jo!\nKen!\nPo!\n")
    p1 = input("Input player 1:")
    p2 = input("Input player 2:")
    winner = get_winner(p1, p2)
    return (f"{winner} wins!")


if __name__ == "__main__":
    main()
