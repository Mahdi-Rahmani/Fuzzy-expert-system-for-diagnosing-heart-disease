class fuzzification:
    def __init__(self):
        self.fuzzy_sets = {
            'age': {
                'age_young': [(0,1), (29,1), (38,0)],
                'age_mild' : [(33,0), (38,1), (45,0)],
                'age_old' : [(40,0), (48,1), (58,0)],
                'age_veryold': [(52,0), (60,1),(80,1)]
            },
            'bloodPressure': {
                'bloodPressure_low': [(100,1),(111,1),(134,0)],
                'bloodPressure_medium': [(127,0), (139,1), (153,0)],
                'bloodPressure_high': [(153,0), (157,1), (172,0)],
                'bloodPressure_veryhigh': [(154,0), (171,1), (300,0)]
            },
            'bloodSugar': {
                'bloodSugar_veryhigh': [(105,0), (120,1), (160,1)]
            },
            'cholesterol': {
                'cholesterol_low': [(100,1), (151,1), (177,0)],
                'cholesterol_medium': [(188,0), (215,1), (250,0)],
                'cholesterol_high': [(217,0), (263,1), (307,0)],
                'cholesterol_veryhigh': [(281,0), (347,1), (400,1)]
            },
            'HeartRate': {
                'HeartRate_low': [(0,1), (100,1), (141,0)],
                'HeartRate_medium': [(111,0), (152,1), (194,0)],
                'HeartRate_high': [(152,0), (210,1), (500,1)]
            },
            'ECG': {
                'ECG_normal': [(-0.5,1), (0,1), (0.4,0)],
                'ECG_abnormal': [(0.2,0), (1,1), (1.8,0)],
                'ECG_hypertrophy': [(1.4,0), (1,9,1), (2,5,1)]
            },
            'oldPeak': {
                'oldPeak_low': [(0,1), (1,1), (2,0)],
                'oldPeak_risk': [(1.5,0), (2.8,1), (4.2,0)],
                'oldPeak_terrible': [(2.5,0), (4,1), (6,1)]
            },
            'output': {
                'output_healthy': [(0,1), (0.25,1), (1,0)],
                'output_sick1': [(0,0), (1,1), (2,0)],
                'output_sick2': [(1,0), (2,1), (3,0)],
                'output_sick3': [(2,0), (3,1), (4,0)],
                'output_sick4': [(3,0), (3.75,1), (5,1)]
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

    def get_fuzzy_value(self, parameter, x, points, value):
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