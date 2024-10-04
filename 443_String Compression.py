class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        temp = None
        count = 0
        res = []
        if n < 2:
            return n
        for i in range(n):
            if count == 0:
                temp = chars[i]
                count += 1
            elif temp == chars[i] and i == n - 1:
                res.append(chars[i])
                count += 1
                if count > 9:
                    for item in list(str(count)):
                        res.append(item)
                else:
                    res.append(str(count))
            elif temp != chars[i] and i == n - 1:
                res.append(temp)
                if count > 9:
                    for item in list(str(count)):
                        res.append(item)
                else:
                    if count > 1:
                        res.append(str(count))
                res.append(chars[i])
            elif temp != chars[i] and count == 1:
                res.append(temp)
                temp = chars[i]
                count = 1
            elif temp != chars[i] and count > 1:
                res.append(temp)
                temp = chars[i]
                if count > 9:
                    for item in list(str(count)):
                        res.append(item)
                else:
                    res.append(str(count))
                count = 1

            else:
                count += 1
        m = len(res)
        print(res)
        for j in range(m):
            chars[j] = res[j]
        return m