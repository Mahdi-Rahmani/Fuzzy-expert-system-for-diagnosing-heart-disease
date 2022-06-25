class Fuzzification:
    def __init__(self):
        self.fuzzy_sets = {
            'age': {
                'young': [(0,1), (29,1), (38,0)],
                'mild' : [(33,0), (38,1), (45,0)],
                'old' : [(40,0), (48,1), (58,0)],
                'veryold': [(52,0), (60,1),(80,1)]
            },
            'blood_pressure': {
                'low': [(100,1),(111,1),(134,0)],
                'medium': [(127,0), (139,1), (153,0)],
                'high': [(153,0), (157,1), (172,0)],
                'veryhigh': [(154,0), (171,1), (300,0)]
            },
            'blood_sugar': {
                'veryhigh': [(105,0), (120,1), (160,1)]
            },
            'cholesterol': {
                'low': [(100,1), (151,1), (177,0)],
                'medium': [(188,0), (215,1), (250,0)],
                'high': [(217,0), (263,1), (307,0)],
                'veryhigh': [(281,0), (347,1), (400,1)]
            },
            'maximum_heart_rate': {
                'low': [(0,1), (100,1), (141,0)],
                'medium': [(111,0), (152,1), (194,0)],
                'high': [(152,0), (210,1), (500,1)]
            },
            'ECG': {
                'normal': [(-0.5,1), (0,1), (0.4,0)],
                'abnormal': [(0.2,0), (1,1), (1.8,0)],
                'hypertrophy': [(1.4,0), (1,9,1), (2,5,1)]
            },
            'old_peak': {
                'low': [(0,1), (1,1), (2,0)],
                'risk': [(1.5,0), (2.8,1), (4.2,0)],
                'terrible': [(2.5,0), (4,1), (6,1)]
            },
            'chest_pain': {
                'typical_anginal': [(0,1),(1,1),(2,0)],
                'atypical_anginal' : [(1,0),(2,1),(3,0)],
                'non_aginal_pain' : [(2,0), (3,1), (4,0)],
                'asymptomatic' : [(3,0), (4,1), (5,1)]
            },
            'exercise': {
                'not_allowable': [(-1,1), (0,1), (1,0)],
                'allowable': [(0,0),(1,1),(2,1)]
            },
            'thallium': {
                'normal': [(0,1), (3,1), (6,0)],
                'medium': [(3,0), (6,1), (7,0)],
                'high' : [(6,0), (7,1), (8,1)]
            },
            'sex': {
                'male': [(-1,1), (0,1), (1,0)],
                'female': [(0,0),(1,1),(2,1)]
            },
            'health': {
                'healthy': [(0,1), (0.25,1), (1,0)],
                'sick_1': [(0,0), (1,1), (2,0)],
                'sick_2': [(1,0), (2,1), (3,0)],
                'sick_3': [(2,0), (3,1), (4,0)],
                'sick_4': [(3,0), (3.75,1), (5,1)]
            }
        }

    def create_line(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        slope = float(y2 - y1) / float(x2 - x1)
        bias = y1 - slope * x1
        return slope, bias

    def get_y_of(self, x, point1, point2):
        # y = ax + b
        a, b = self.create_line(point1, point2)
        return a * x + b

    def get_fuzzy_value(self, parameter, x):
        result = {}
        for sub_element in self.fuzzy_sets[parameter]:
            index = 0
            for point in self.fuzzy_sets[parameter][sub_element]:
                if (index == 0 and point[1] == 1 and x < point[0]) or (index == 2 and point[1] == 1 and x > point[0]):
                    result[sub_element] = 1
                    break
                if index == 0:
                    index += 1
                    lastPoint = point
                    continue
                index += 1
                if lastPoint[0] <= x <= point[0]:
                    result[sub_element] = self.get_y_of(x, lastPoint, point)
                    break
                result[sub_element] = 0
                lastPoint = point
        return result

    """ this method find fuzzy value for each parameter of input. our input has a dict 
    format that we can see in final_result class also. finding fuzzy value is possible 
    with get_fuzzy_value function in this class"""

    def fuzzify_user_input(self, user_input):
        # save the fuzzy results of inputs in fuzzy_result dict
        fuzzy_result = {}
        for parameter in user_input:
            fuzzy_result[parameter] = self.get_fuzzy_value(parameter, user_input[parameter])
        return fuzzy_result