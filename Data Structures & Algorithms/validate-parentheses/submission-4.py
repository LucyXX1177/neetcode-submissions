class Solution:
    def isValid(self, s: str) -> bool:
        record = []

        opening = {"(", "[", "{"}

        closing = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for i in s:

            if i in opening:
                record.append(i)

            elif not record or i != closing[record[-1]]:
                return False

            else:
                record.pop()

        return len(record) == 0

