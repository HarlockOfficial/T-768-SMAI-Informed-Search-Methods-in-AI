PRECISION = 0.05
NUMBERS_AFTER_DECIMAL = 2


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


def _trim_gate(gate: float) -> float:
    return round(PRECISION * round(gate / PRECISION), NUMBERS_AFTER_DECIMAL)


class InformedEstimator(Estimator):

    def __init__(self, num_gates, capacity, avg, std):
        Estimator.__init__(self, num_gates, capacity, avg, std)
        self.compute()
        return

    def compute(self):
        """
        def float_range(start: float, stop: float, step: float):
            while start < stop:
                yield start
                start += step
        self.precomputed_values = dict()
        for i in float_range(0, self.capacity+PRECISION, PRECISION):
            trimmed_gate = _trim_gate(i)
            self.precomputed_values[trimmed_gate] = self.__compute_giveaway(trimmed_gate)[0]
        """
        leakage_constant = 16
        self.precomputed_values = dict()
        for weight in range(self.capacity):
            self.precomputed_values[weight] = weight // leakage_constant + max(0, (-weight // leakage_constant) +
                                                                               weight - (self.capacity - self.avg))

    def __compute_giveaway(self, gate: float):
        space_left = self.capacity - gate
        estimated_avg = 0
        if space_left > 0:
            estimated_avg = -(space_left - (((space_left // self.avg) + 1) * self.avg))
        return estimated_avg - self.std, estimated_avg, estimated_avg + self.std

    def get_giveaway(self, gates):
        #return sum([self.precomputed_values[_trim_gate(gate)] for gate in gates])
        return sum(self.precomputed_values[weight] for weight in gates)