import math


class Estimator:

    def __init__(self, num_gates, capacity, avg, std):
        assert (num_gates > 0)
        self.num_gates = num_gates
        self.capacity = capacity
        self.avg = avg
        self.std = std

    def get_giveaway(self, gates):
        # Estimate the future giveaway for the partially filled boxes at the gates.
        return 0


class InformedEstimator(Estimator):

    def __init__(self, num_gates, capacity, avg, std):
        Estimator.__init__(self, num_gates, capacity, avg, std)
        self.compute()
        return

    def compute(self):
        def float_range(start: float, stop: float, step: float):
            while start < stop:
                yield start
                start += step
        self.precomputed_values = {}
        for i in float_range(0, self.capacity, 0.001):
            self.precomputed_values[i] = self.get_giveaway([i])

    def __compute_giveaway(self, gate: float):
        space_left = self.capacity - gate
        estimated_avg = 0
        if space_left > 0:
            estimated_avg = -(space_left - (((space_left // self.avg) + 1) * self.avg))
        return estimated_avg - self.std, estimated_avg, estimated_avg + self.std

    def get_giveaway(self, gates):
        for gate in gates:
            if gate not in self.precomputed_values:
                self.precomputed_values[gate] = self.__compute_giveaway(gate)[0]
        return sum([self.precomputed_values.get(gate) for gate in gates])
