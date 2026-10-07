from logic import *

# Symbols
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

symbols = [AKnight, AKnave, BKnight, BKnave]

# Everyone is either a knight or a knave, but not both
basic_rules = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave))
)


def solve(name, knowledge):
    print(name)
    for symbol in symbols:
        if model_check(knowledge, symbol):
            print(symbol)
    print()


# ---------------- PUZZLE 0 ----------------
# A says: "I am both a knight and a knave."

statement0 = And(AKnight, AKnave)

knowledge0 = And(
    basic_rules,
    Implication(AKnight, statement0),
    Implication(AKnave, Not(statement0))
)

solve("Puzzle 0", knowledge0)


# ---------------- PUZZLE 1 ----------------
# A says: "We are both knaves."
# B says nothing.

statement1 = And(AKnave, BKnave)

knowledge1 = And(
    basic_rules,
    Implication(AKnight, statement1),
    Implication(AKnave, Not(statement1))
)

solve("Puzzle 1", knowledge1)


# ---------------- PUZZLE 2 ----------------
# A says: "We are the same kind."
# B says: "We are of different kinds."

same_kind = Or(
    And(AKnight, BKnight),
    And(AKnave, BKnave)
)

different_kinds = Or(
    And(AKnight, BKnave),
    And(AKnave, BKnight)
)

knowledge2 = And(
    basic_rules,

    # A's statement
    Implication(AKnight, same_kind),
    Implication(AKnave, Not(same_kind)),

    # B's statement
    Implication(BKnight, different_kinds),
    Implication(BKnave, Not(different_kinds))
)

solve("Puzzle 2", knowledge2)
