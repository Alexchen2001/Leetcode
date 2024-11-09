class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uEmail = set()

        for email in emails:
            domainArr = []
            eNameArr = []

            for ltr in email:

                if ltr == "@" or ltr == "+":
                    break
                if ltr != ".":
                    eNameArr.append(ltr)
            
            for ltr in email[::-1]:
                print(ltr)

                if ltr == "@":
                    break
                domainArr.append(ltr)
            name = ''.join(eNameArr)
            dom = ''.join(domainArr[::-1])
            uEmail.add(name + "@" + dom)
        return len(uEmail)


                
        
