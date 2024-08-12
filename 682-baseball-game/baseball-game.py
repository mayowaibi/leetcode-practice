class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i, op in enumerate(operations):
            # Checking if character is an integer (+ve or -ve)
            if op.isdigit() or (op.startswith('-') and op[1:].isdigit()):
                record.append(int(op))
            elif op == '+':
                record.append(record[-2] + record[-1])
            elif op == 'D':
                record.append(record[-1] * 2)
            elif op == 'C':
                record.pop()
        
        return sum(record)