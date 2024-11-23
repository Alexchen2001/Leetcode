from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        graph = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(min(len(words[i]), len(words[j]))):
                    if words[i][k] != words[j][k]:
                        graph[words[i][k]].add(words[j][k])
                        break
                else:
                    if len(words[i]) > len(words[j]):
                        print("1")
                        return ""
        
        sumStr = ''.join(words)
        uString = set()
        for ltr in sumStr:
            uString.add(ltr)
        inDegree = defaultdict(int)
        for ltr in uString:
            for node in graph[ltr]:
                inDegree[node] += 1
        resStr = ""
        queue = deque()
        for ltr in uString:
            if inDegree[ltr] == 0:
                queue.append(ltr)
        while queue:
            node = queue.popleft()
            resStr += node
            for nextNode in graph[node]:
                inDegree[nextNode] -= 1
                if inDegree[nextNode] == 0:
                    queue.append(nextNode)
        
        if len(resStr) != len(uString):
            print("2")
            return ""
        return resStr
