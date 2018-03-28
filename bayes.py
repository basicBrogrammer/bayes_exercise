class Bayes(object):
    '''
    INPUT:
        prior (dict): key is the value (e.g. 4-sided die),
                      value is the probability

        likelihood_func (function): takes a new piece of data and the value and
                                    outputs the likelihood of getting that data
    '''
    def __init__(self, prior, likelihood_func):
        self.prior = prior
        self.likelihood_func = likelihood_func


    def normalize(self):
        '''
        INPUT: None
        OUTPUT: None

        Makes the sum of the probabilities equal 1.
        '''
        total = sum(self.prior.values())

        for k, v in self.prior.items():
            self.prior[k] = self.prior[k] / total

    def update(self, data):
        '''
        INPUT:
            data (int or str): A single observation (data point)

        OUTPUT: None

        Conduct a bayesian update. Multiply the prior by the likelihood and
        make this the new prior.
        '''
        for die, prior in self.prior.items():
            self.prior[die] = self.prior[die] * self.likelihood_func(data, die)
            # fair_posterior = (p_fair_prior * p_head_fair)

        self.normalize()


    def print_distribution(self):
        '''
        Print the current posterior probability.
        '''
        for die, prior in self.prior.items():
            print('For die {} the posterior prob is {}'.format(die, prior))
