import numpy as np

class Defuzzification:
    def __init__(self, fuzzification):
        # we need fuzzification Object to find the fuzzy value of
        # each discrete point on x axis in health chart
        self.fuzzification = fuzzification

    """ In this function first we should discrete the x axis of health chart
    Then according to below formula we can calculate the center of mass:
    formula :   x_c = (sigma (mu(i) * x(i))) / (sigma (mu(i)))  """

    def get_center_of_mass(self, health):
        # 1- discretization
        points = np.linspace(0, 5, 1000)
        # 2- define two variables. one for the numerator in center of mass formula (sigma_mu_x)
        #    and one for denominator of that formula (sigma_mu)
        sigma_mu_x = 0.0
        sigma_mu = 0.0
        # 3- for finding the area that we should to calculate its center of mass:
        #    we should calculate minimum between inference output and fuzzy value of fuzzification part
        #    health['healthy'] has a constant fuzzy value and its like (+) line in below figure
        #    self.fuzzification.get_fuzzy_value('healthy', points[i]) get us the triangle that specified
        #    with (/\) in below figure
        #    The result that we want from calculating min is (*) part in figure
        #    (NOTE: also we know each min is calculate for 1 point but this figure help to understand)
        #                    |         /\
        #                    |        /  \
        # health['healthy']  |+ + + +* * * *+ + + +
        #                    |_____*_________*________
        #    then we should calculate maximum. because its possible to have two fuzzy value for a point but we
        #    should select maximum value. like below figure that only we want (*) part
        #                    |         /\     / \
        # health['sick_1']   |+ + + + /  \ + * * * + + + +
        # health['healthy']  |+ + + +* * * * + + +* + + +
        #                    |_____*______/________*_______
        for i in range(len(points)):
            healthy = min(health['healthy'], self.fuzzification.get_fuzzy_value('healthy', points[i]))
            sick_1 = min(health['sick_1'], self.fuzzification.get_fuzzy_value('sick_1', points[i]))
            sick_2 = min(health['sick_2'], self.fuzzification.get_fuzzy_value('sick_2', points[i]))
            sick_3 = min(health['sick_3'], self.fuzzification.get_fuzzy_value('sick_3', points[i]))
            sick_4 = min(health['sick_4'], self.fuzzification.get_fuzzy_value('sick_4', points[i]))
            overall_health = max(healthy, sick_1, sick_2, sick_3, sick_4)
            # 4- update sigma_mu_x and sigma_mu point by point
            sigma_mu_x += overall_health * points[i]
            sigma_mu += overall_health

        # 5- check if the sigma_mu is zero
        if sigma_mu == 0:
            return 0
        # 6- if sigma_mu is not zero we calculate center of mass value
        else:
            return sigma_mu_x / sigma_mu

    """ in this method first we should calculate center of mass with get_center_of_mass
    function then we should the fuzzy values at center of mass point in health chart
    then we can return the health status that has maximum membership value"""
    def get_health_status(self, inference_result):
        center_of_mass = self.get_center_of_mass(inference_result)
        COM_fuzzy_value = self.fuzzification.get_fuzzy_value('health', center_of_mass)
        # change value and key to find maximum value
        # (a trick for finding a key with maximum value in dictionary)
        inverse = [(value, key) for key, value in COM_fuzzy_value.items()]
        health_status = max(inverse)[1]
        return health_status