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
        leakage = 14*(3 ** self.num_gates)
        self.precomputed_values = dict()
        for weight in range(self.capacity):
            w1 = weight//leakage
            self.precomputed_values[weight] = w1 + max(0, weight - self.capacity + self.avg - w1)

    def get_giveaway(self, gates):
        return sum(self.precomputed_values[weight] for weight in gates)