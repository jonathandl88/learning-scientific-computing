import copy
import random


class Hat:
    def __init__(self, **kwargs):
        if not kwargs:
            raise ValueError("A hat must have at least one ball.")
        self.contents = [key for key, value in kwargs.items() for _ in range(value)]

    def draw(self, n):
        sample = []
        if n > len(self.contents):
            return [self.contents.pop() for _ in range(len(self.contents))]
        else:
            for _ in range(n):
                random_index = random.randrange(len(self.contents))
                sample.append(self.contents.pop(random_index))
        return sample


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = num_experiments
    for _ in range(N):
        trial_hat = copy.deepcopy(hat)
        sample = trial_hat.draw(num_balls_drawn)
        bools = []

        for key, value in expected_balls.items():
            bools.append(sample.count(key) >= value)
        if all(bools):
            M += 1
    return M / N


if '__name__' == '__main__':
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                            expected_balls={'red': 2, 'green': 1},
                            num_balls_drawn=5,
                            num_experiments=2000)