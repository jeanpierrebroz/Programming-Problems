class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #x: record new score of x
        #+ record new score that is sum of old scores
        #d record new score that is double of previous
        #c: invaliate previous score, removing from record

        record = []

        for op in operations:
            if op == "+":
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(record[-1] * 2)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)