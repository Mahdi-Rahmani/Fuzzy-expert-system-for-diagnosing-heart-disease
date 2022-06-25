from fuzzification import Fuzzification
from inference import Inference
from defuzzification import Defuzzification

class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        fuzzification = Fuzzification()
        fuzzy_value = fuzzification.fuzzify_user_input(input_dict)
        inference = Inference()
        health_memberships = inference.result_membership(fuzzy_value)
        defuzzification = Defuzzification(fuzzification)
        health_status = defuzzification.get_health_status(health_memberships)
        return health_status
