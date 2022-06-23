class fuzzification:
    def __init__(self):
        fuzzy_sets = {
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
            }
        }

    def get_line(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        slope = float(y2 - y1) / float(x2 - x1)
        bias = y1 - slope * x1
        return slope, bias

    def get_y