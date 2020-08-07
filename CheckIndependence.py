import pandas as pd
from math import sqrt


# you can use this table as an example
distr_table_sample = pd.DataFrame({
    'X': [0, 0, 1, 1],
    'Y': [1, 2, 1, 2],
    'pr': [0.3, 0.25, 0.15, 0.3]
})


def mass(values,probabilities):
    """Dict of value with marginal probability"""
    var_pr = {}
    for i, pr in enumerate(probabilities):
        var_pr[values[i]] = var_pr.get(values[i], .0) + pr
    return var_pr


def mean(mass_dict):
    mu = .0
    for val, pr in mass_dict.items():
        mu += pr * val
    return mu


def std_dev(mass_dict, mu):
    sigma = .0
    for val, pr in mass_dict.items():
        sigma += pr * pow(val - mu, 2)
    return sqrt(sigma)

class CheckIndependence:

    def __init__(self):
        self.version = 1


    def check_independence(self, distr_table: pd.DataFrame):

        pr_list = distr_table['pr'].tolist()
        x_list = distr_table['X'].tolist()
        y_list = distr_table['Y'].tolist()

        x_mass = mass(x_list, pr_list)
        y_mass = mass(y_list, pr_list)

        x_mean = mean(x_mass)
        y_mean = mean(y_mass)

        independent = True
        cov = .0

        for i, pr in enumerate(pr_list):
            x, y = x_list[i], y_list[i]

            #  independence
            if x != y:
                if pr != (x_mass[x] * y_mass[y]):
                    independent = False

            # covariance
            cov += pr * (x - x_mean) * (y - y_mean)

        corr = cov / (std_dev(x_mass, x_mean) * std_dev(y_mass, y_mean))

        return {'are_independent': independent, 'cov': cov, 'corr': corr}


