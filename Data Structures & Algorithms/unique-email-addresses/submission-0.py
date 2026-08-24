class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()
        res = 0
        for e in emails:
            localName, domain = e.split("@")
            if "+" in localName:
                newList = localName.split("+")
                localName = newList[0]
            localName = localName.replace(".", "")
            fullEmail = localName+domain
            print(fullEmail)
            if fullEmail not in emails_set:
                res += 1
                emails_set.add(fullEmail)
        return res