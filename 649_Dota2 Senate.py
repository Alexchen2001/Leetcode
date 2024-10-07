from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        RQ = deque([])
        DQ = deque([])
        n = len(senate)
        turns = deque([])
        for i in range(n):
            turns.append(i)
            if senate[i] == 'R':
                RQ.append(i)
            else:
                DQ.append(i)
        while len(DQ) > 0 and len(RQ) > 0:
            person = turns.popleft()
            if senate[person] == 'R':
                personRQ = RQ.popleft()
                if person == personRQ:
                    RQ.append(personRQ)
                    DQ.popleft()
                    turns.append(person)
                else:
                    RQ.appendleft(personRQ)

            else:
                if senate[person] == 'D':
                    personDQ = DQ.popleft()
                if person == personDQ:
                    DQ.append(personDQ)
                    RQ.popleft()
                    turns.append(person)
                else:
                    DQ.appendleft(personDQ)
        if len(DQ) > 0:
            return "Dire"
        else:
            return "Radiant"



        

