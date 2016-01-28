# class TempTracker with these methods:
#
# insert()—records a new temperature
# get_max()—returns the highest temp we've seen so far
# get_min()—returns the lowest temp we've seen so far
# get_mean()—returns the mean of all temps we've seen so far
# get_mode()—returns the mode of all temps we've seen so far

class TempTracker():
    def __init__(self):
        self.min_temp = None
        self.max_temp = None

        # for mean
        self.total_numbers = 0
        self.total_sum = 0.0 # mean should be float
        self.mean = None

        # for mode
        self.occurrences = [0] * (111) # list of 0s at indices 0..110
        self.max_occurrences = 0
        self.mode = None

    def insert(self, temperature):
        self.total_numbers += 1
        self.total_sum += temperature
        self.mean = self.total_sum / self.total_numbers

        # for mode
        self.occurrences[temperature] += 1
        if self.occurrences[temperature] > self.max_occurrences:
            self.mode = temperature
            self.max_occurrences = self.occurrences[temperature]

        if not self.max_temp or temperature > self.max_temp:
            self.max_temp = temperature
        if not self.min_temp or temperature < self.min_temp:
            self.min_temp = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.