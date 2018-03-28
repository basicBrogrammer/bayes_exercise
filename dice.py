from bayes import Bayes


def die_likelihood(roll, die):
    """
    Args:
        roll (int): result of a single die roll
        die  (int): number of sides of the die that produced the roll

    Returns:
        likelihood (float): the probability of the roll given the die.
    """




if __name__ == '__main__':
    uniform_prior = #fill in here
    unbalanced_prior = #fill in here
    die_bayes_1 = Bayes(prior, die_likelihood)
    experiment = [8,2,1,2,5,8,2,4,3,7,6,5,1,6,2,5,8,8,5,3,4,2,4,3,8,8,7,8,8,8,5,5,1,3,8,7,8,5,2,5,1,4,1,2,1,3,1,3,1,5]

    for roll in experiment:
        die_bayes_1.update(roll)
        die_bayes_1.print_distribution()
    # ... you take it from here ...
