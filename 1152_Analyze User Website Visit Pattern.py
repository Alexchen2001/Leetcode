from collections import defaultdict
from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = sorted(zip(timestamp,username,website))

        # building user access history
        userVisitHistory = defaultdict(list)
        for accessTime, user, site in data:
            userVisitHistory[user].append(site)
        
        # We do not want count multiple access from the same users
        patternsUsers = defaultdict(set)
        for user,sites in userVisitHistory.items():
            # since its combination, the order doesn't matter so we use set
            patterns = set(combinations(sites, 3))
            for pattern in patterns:
                patternsUsers[pattern].add(user)
        
        maxVisit = 0
        result = tuple()

        for pattern, users in patternsUsers.items():
            visitCount = len(users)
            if visitCount > maxVisit or (visitCount == maxVisit and pattern < result):
                maxVisit = visitCount
                result = pattern
        
        return result
        
        