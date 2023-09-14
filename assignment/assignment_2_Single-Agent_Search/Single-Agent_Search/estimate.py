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
        # You implement this (optional) in case you want to do some onetime pre-computations.
        return

    def get_giveaway(self, gates):
        # Estimate the future giveaway for the partially filled boxes at the gates.
        space_left_in_gates = [self.capacity - gate for gate in gates]
        esitmated_giveaway_avg = [-(space_left - (((space_left // self.avg) + 1) * self.avg)) if space_left % self.avg > 0 else 0 for space_left in space_left_in_gates]
        estimated_giveaway_range = [(estimated_avg - self.std, estimated_avg + self.std)
                                    for estimated_avg in esitmated_giveaway_avg]
        total_giveaway = (sum([estimated_range[0] for estimated_range in estimated_giveaway_range]),
                          sum([estimated_avg for estimated_avg in esitmated_giveaway_avg]),
                          sum([estimated_range[1] for estimated_range in estimated_giveaway_range]))
        return total_giveaway[0]
