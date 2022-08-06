class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        rules = {"type": 0, "color": 1, "name": 2}
        count = 0
        
        for item in items:
            if item[rules[ruleKey]] == ruleValue:
                count += 1
        return count