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


def _beta_function(x1, x2):
    return math.gamma(x1) * math.gamma(x2) / math.gamma(x1 + x2)


class InformedEstimator(Estimator):

    def __init__(self, num_gates, capacity, avg, std, cars):
        Estimator.__init__(self, num_gates, capacity, avg, std)
        self.__cars = cars
        self.compute()
        return

    def compute(self):
        # You implement this (optional) in case you want to do some onetime pre-computations.
        return

    def get_giveaway(self, gates):
        # Estimate the future giveaway for the partially filled boxes at the gates.
        selected_heuristic = self.__initial_heuristic

        space_left_in_gates = [self.capacity - gate for gate in gates]
        estimated_giveaway_avg = [selected_heuristic(space_left) for space_left in space_left_in_gates]
        estimated_giveaway_range = [(estimated_avg - self.std, estimated_avg + self.std)
                                    for estimated_avg in estimated_giveaway_avg]
        total_giveaway = (sum([estimated_range[0] for estimated_range in estimated_giveaway_range]),
                          sum([estimated_avg for estimated_avg in estimated_giveaway_avg]),
                          sum([estimated_range[1] for estimated_range in estimated_giveaway_range]))
        return total_giveaway[1]

    def __initial_heuristic(self, space_left):
        return -(space_left - (((space_left // self.avg) + 1) * self.avg)) if space_left % self.avg > 0 else 0

    def __gaussian(self, x):
        # NOTE: mu = avg, sigma = std
        return (1 / (self.std * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - self.avg) / self.std) ** 2)

    def __t_distribution(self, x):
        # NOTE: df = num_gates - 1
        df = self.num_gates - 1
        return math.gamma((df + 1) / 2) / (math.sqrt(df * math.pi) * math.gamma(df / 2) * (1 + x**2 / df)**((df + 1) / 2))

    def __uniform_distribution(self, x):
        # NOTE: a = avg - std, b = avg + std
        a = self.avg - self.std
        b = self.avg + self.std
        if a < x < b:
            return 1 / b - a
        return 0

    def __exponential_distribution(self, x):
        # NOTE: lambda is assumed 1/avg
        if x > 0:
            lambda_ = 1 / self.avg
            return lambda_ * math.exp(-x * lambda_)
        return 0

    def __chi_square_distribution(self, x):
        # NOTE: df = num_gates - 1
        if x > 0:
            df = self.num_gates - 1
            return x**(df / 2 - 1) * math.exp(-x / 2) / (2**(df / 2) * math.gamma(df / 2))
        return 0

    def __f_distribution(self, x, num_cars):
        # NOTE: df1 = num_gates - 1, df2 = num_cars - 1
        df1 = self.num_gates - 1
        df2 = num_cars - 1
        return math.sqrt((df1 * x)**df1 * df2**df2 / (df1 * x + df2)**(df1 + df2)) / (x * _beta_function(df1/2, df2/2))