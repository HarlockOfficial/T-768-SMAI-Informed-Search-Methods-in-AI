#
# Informed Search Methods
#
# Implementation of various backtracking-based solvers.
#

from enum import Enum


class SolverType(Enum):
    GTBT = 1        # Generate-and-test Backtracking
    BT = 2          # Cronological Backtracking
    BJ = 3          # Backjumping
    CBJ = 4         # Conflict-Directed Backjumping


def make_arc_consistent(cn):
    """
    Makes the cn constraint network arc-consistent (use the AC-3 algorithm).
    (there are no unary-constraints, so you can omit making it first node-consistent).
    """

    # ===> Your task is to implement this routine. Feel free to add sub-routines as needed.
    ...

    return


def solve(st, cnet):
    """
    Use the specified backtracking algorithm (st) to solve the CSP problem (cnet).
    Returns a tuple (assignment, nodes), where the former is the solution (an empty list if not found)
    and the latter the number of nodes generated.
    """

    def consistent_upto_level(cn, i, A):
        for j in range(0, i):
            if not cn.consistent(i, j, A):
                return j
        return i

    def GTB(cn, i, A):
        # print(A)
        nonlocal num_nodes
        num_nodes += 1
        if i >= cn.num_variables():
            return cn.consistent_all(A)
        for v in cn.get_sorted_domain(i):
            A.append(v)
            solved = GTB(cn, i+1, A)
            if solved:
                return True
            A.pop()
        return False

    def BT(cn, i, A):
        # ===> Your task is to implement this routine.
        ...
        return False

    def BJ(cn, i, A):
        # ===> Your task is to implement this routine.
        ...
        return (False, 0)

    def CBJ(cn, i, A, CS):
        # ===> Your task is to implement this routine.
        ...
        return (False, 0)

    num_nodes = 0
    assignment = []
    conflict_set = [set() for _ in range(0, cnet.num_variables())]

    print('Solving ...', st)
    if st == SolverType.GTBT:
        is_solved = GTB(cnet, 0, assignment)
    elif st == SolverType.BT:
        is_solved = BT(cnet, 0, assignment)
    elif st == SolverType.BJ:
        (is_solved, _) = BJ(cnet, 0, assignment)
    elif st == SolverType.CBJ:
        (is_solved, _) = CBJ(cnet, 0, assignment, conflict_set)

    return (assignment, num_nodes)
