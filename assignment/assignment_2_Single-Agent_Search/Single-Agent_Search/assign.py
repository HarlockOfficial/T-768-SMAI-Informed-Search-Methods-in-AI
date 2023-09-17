from timeit import default_timer as timer


class Assign:

    def __init__(self, debug, estimator):
        self.debug = debug
        self.estimator = estimator
        return

    def get_estimator(self):
        return self.estimator

    def assign(self, cars, gates, capacity, time):
        """
        Determines the gate number to dispatch the item in car[0].
        :param cars: List with weight of items
        :param gates: List with weight of boxes at gates
        :param capacity: Box capacity
        :param time: Maximum time (in seconds) allowed for allocation; if 0, then there are no time-limits.
        :return: The gate number to assign item in car[0]
        """

        def time_is_up(start, time):
            if time == 0:
                return False
            return timer() - start >= time

        def do_assign(w, g):
            filled = False
            giveaway = 0
            gates[g] += w
            if gates[g] >= capacity:
                giveaway = gates[g] - capacity
                gates[g] = 0
                filled = True
            return (filled, giveaway)

        def undo_assign(w, g, info):
            filled, giveaway = info
            if filled:
                gates[g] = (capacity + giveaway) - w
            else:
                gates[g] -= w
            return

        # IMPLEMENT THIS ROUTINE
        # Suggestion: Use an iterative-deepening version of DFBnB.
        # Call 'self.estimator.get_giveaway(gates)' for the heuristic estimate of future giveaway

        def sort_gates(gates):
            sorted_gates = []
            for i, gate_weight in enumerate(gates):
                sorted_gates.append((i, gate_weight))
            sorted_gates.sort(key=lambda x: x[1])

            return sorted_gates

        def iddfbnb_rec(current_depth, last_giveaway_update_depth, best_current_car_fit):

            ordered_gates = sort_gates(gates)

            for gate in range(len(gates)):
                current_gate = ordered_gates[gate][0]
                gate_state[current_depth] = do_assign(cars[current_depth], current_gate)
                total_established_giveaway = sum([gate_state[_][1] for _ in range(current_depth + 1)])
                current_solution[current_depth] = current_gate

                if current_depth == 0:
                    if gate_state[0] == (True, 0):
                        best_current_car_fit[0] = current_gate
                        best_giveaway[0] = current_gate
                        return True

                if total_established_giveaway > best_giveaway[current_depth]:
                    undo_assign(cars[current_depth], current_gate, gate_state[current_depth])
                    continue

                if current_depth < global_depth_boundary:
                    iddfbnb_rec(current_depth + 1, last_giveaway_update_depth, best_current_car_fit)

                else:
                    giveaway_estimate = self.estimator.get_giveaway(gates)
                    if total_established_giveaway + giveaway_estimate < best_giveaway[current_depth]:
                        best_giveaway[current_depth] = total_established_giveaway + giveaway_estimate
                        last_giveaway_update_depth = current_depth
                        best_current_car_fit[:] = current_solution[:]
                undo_assign(cars[current_depth], current_gate, gate_state[current_depth])
                if time_is_up(begin_time, time):
                    return False

        max_depth = len(cars)
        max_giveaway = float('inf')

        current_solution, best_solution, gate_state, best_giveaway = [], [], [], []

        for i in range(max_depth):
            current_solution.append(-1)
            best_solution.append(-1)
            gate_state.append((False, 0))
            best_giveaway.append(max_giveaway)

        global_depth_boundary = 0
        begin_time = timer()

        # iterative deepening through the cars
        while global_depth_boundary < max_depth:
            exit_search = iddfbnb_rec(0, -1, best_solution)
            if time_is_up(begin_time, time) or exit_search:
                break
            else:
                global_depth_boundary += 1
        return best_solution[0]

