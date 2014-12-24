"""Package for peg game simulation code"""

import peggy.solver
from peggy.constants import LABELS

def getUserChoice():
    fmt_str = "\n".join([
        "        {0}",
        "      {1}  {2}",
        "    {3}  {4}  {5}",
        "  {6}  {7}  {8}  {9}",
        "{10}  {11}  {12}  {13}  {14}"
        ])
    print(fmt_str.format(*LABELS))
    resp = input("Enter choice or 'q' to exit: ")

    if resp != 'q' and resp not in set(LABELS):
        print("Invalid input")
        return getUserChoice()
    else:
        return resp


def main():
    choice = getUserChoice()
    while choice != 'q':
        solver.solveOne(choice)
        choice = getUserChoice()
