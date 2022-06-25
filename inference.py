import re
class Inference:
    def __init__(self):
        self.rules = self.read_rules()

    """ This function read rules from rules.fcl file
    also save parts of a rule as a list. at the end the all rules are saved in rules list.
    for example if we have below rule:
      "RULE 1: IF (age IS very_old) AND (chest_pain IS atypical_anginal) THEN health IS sick_4;"
    then we save it as below:
      [['age','very_old'],['chest_pain','atypical_anginal'],['health','sick_4']]"""
    def read_rules(self):
        rules = []
        with open('rules.fcl') as f:
            for line in f:
                rule = []
                if 'OR' in line:
                    for normal_rule in self.change_to_normal_rule(line):
                        rules.append(normal_rule)
                    continue
                for i in re.split('[()]', line):
                    if 'IS' in i:
                        rule.append(list(i.replace('IS', '').replace('THEN', '').replace(';', '').split()))
                rules.append(rule)
        return rules

    """ This function is written according to our rules
    our rules in complex format only has (AND) or (OR) but not both of them
    also our rules at most has two parts in IF section"""
    def change_to_normal_rule(self, rule):
        rules = []
        parts = []
        for i in re.split('[()]', rule):
            if 'IS' in i:
                parts.append(list(i.replace('IS', '').replace('THEN', '').replace(';', '').split()))
        for i in range(len(parts)-1):
            rule = []
            rule.append(parts[i])
            rule.append(parts[len(parts)-1])
            rules.append(rule)
        return rules

    def result_membership(self, fuzzy_value):
        result = {
            'healthy': [0],
            'sick_1': [0],
            'sick_2': [0],
            'sick_3': [0],
            'sick_4': [0]}

        for rule in self.rules:
            # the membership of each part of a rule
            memberships = []
            # calculate min if we have AND between conditions of a rule
            for i in range(len(rule)-1):
                memberships.append(fuzzy_value[rule[i][0]][rule[i][1]])
            result[rule[len(rule)][1]].append(min(memberships))
        # calculate max on results for each health subset
        for subset in result:
            result[subset] = max(result[subset])
        return result
