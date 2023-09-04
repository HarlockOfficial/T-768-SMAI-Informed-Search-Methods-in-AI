#
# Informed Search Methods
#
# Implementation of various backtracking-based solvers.
#
from enum import Enum

import constraintnetwork
import sudoku


class SolverType(Enum):
    GTBT = 1  # Generate-and-test Backtracking
    BT = 2  # Cronological Backtracking
    BJ = 3  # Backjumping
    CBJ = 4  # Conflict-Directed Backjumping


def make_arc_consistent(cn: constraintnetwork.ConstraintNetwork):
    """
    Makes the cn constraint network arc-consistent (use the AC-3 algorithm).
    (there are no unary-constraints, so you can omit making it first node-consistent).
    """

    # ===> Your task is to implement this routine. Feel free to add sub-routines as needed.

    # Generate queue of all constraints
    q = sudoku.generate_constraints()
    r = []
    for i in q:
        r.append((i[1],i[0]))
    q = sorted(q + r)

    # Assigns domain of variables at start of queue
    while len(q) > 0:
        dom = cn.get_domain(q[0][0])
        dom2 = cn.get_domain(q[0][1])
        revise = False

        # Checks if a value can be removed from the domain
        for i in cn.get_domain(q[0][0]):
            if i in cn.get_domain(q[0][1]) and len(cn.get_domain(q[0][1])) == 1:
                revise = True
                point = i
                cn.get_domain(q[0][0]).remove(point)
                break
            else:
                pass

        # If not, remove from queue
        if revise == False:
            q.pop(0)
        
        # If yes, remove from queue and add applicable pairs to queue
        else:
            temp = q.pop(0)
            const = sudoku.generate_constraints()
            for k in const:
                if k[0] == i:
                    q.append((k[1],k[0]))
                elif k[1] == i:
                    q.append(k)

    return cn


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

    def GTB(cn, current_index, assigned_values):
        # print(A)
        nonlocal num_nodes
        num_nodes += 1
        if current_index >= cn.num_variables():
            return cn.consistent_all(assigned_values)
        for v in cn.get_sorted_domain(current_index):
            assigned_values.append(v)
            solved = GTB(cn, current_index + 1, assigned_values)
            if solved:
                return True
            assigned_values.pop()
        return False

    def BT(constraint_network, current_index, assigned_values):
        """
        Backtracking algorithm.
        """
        nonlocal num_nodes
        num_nodes += 1

        if current_index >= constraint_network.num_variables():
            return constraint_network.consistent_all(assigned_values)

        for value in constraint_network.get_sorted_domain(current_index):
            assigned_values.append(value)
            if consistent_upto_level(constraint_network, current_index, assigned_values) == current_index:
                solved = BT(constraint_network, current_index + 1, assigned_values)
                if solved:
                    return True
            assigned_values.pop()
        return False

    def BJ(constraint_network, current_index, assigned_values):
        """
        Backjumping algorithm.
        """
        # TODO check: does not lower the number of visited nodes
        nonlocal num_nodes
        num_nodes += 1

        if current_index >= constraint_network.num_variables():
            if constraint_network.consistent_all(assigned_values):
                return True, -1
            inconsistency_index = consistent_upto_level(constraint_network, current_index-1, assigned_values)
            return False, inconsistency_index

        inconsistency_index_list = []
        for value in constraint_network.get_sorted_domain(current_index):
            inconsistency_index = consistent_upto_level(constraint_network, current_index, assigned_values + [value])
            if inconsistency_index < current_index:
                inconsistency_index_list.append(inconsistency_index)
                continue
            assigned_values.append(value)
            result, inconsistency_index = BJ(constraint_network, current_index + 1, assigned_values)
            if result:
                return True, -1
            assigned_values.pop()
            inconsistency_index_list.append(inconsistency_index)
            if inconsistency_index < current_index:
                return False, max(inconsistency_index_list)
        return False, max(inconsistency_index_list)


    def CBJ(cn, i, A, CS):
        # ===> Your task is to implement this routine.
        ...
        return False, 0

    num_nodes = 0
    assignment = []
    conflict_set = [set() for _ in range(0, cnet.num_variables())]

    print('Solving ...', st)
    if st == SolverType.GTBT:
        is_solved = GTB(cnet, 0, assignment)
    elif st == SolverType.BT:
        is_solved = BT(cnet, 0, assignment)
    elif st == SolverType.BJ:
        is_solved, _ = BJ(cnet, 0, assignment)
    elif st == SolverType.CBJ:
        is_solved, _ = CBJ(cnet, 0, assignment, conflict_set)

    return assignment, num_nodes
