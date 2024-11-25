import re

class FOPCParser:
    def __init__(self):
        self.pattern = re.compile(r'([A-Za-z]+)\((.*?)\)')

    def parse(self, expression):
        match = self.pattern.match(expression)
        if match:
            predicate = match.group(1)
            arguments = match.group(2).split(',')
            return {"predicate": predicate, "arguments": [arg.strip() for arg in arguments]}
        else:
            raise ValueError("Invalid FOPC expression")

# Example usage
parser = FOPCParser()
expression = "Loves(John, Mary)"
parsed = parser.parse(expression)
print(f"Parsed FOPC Expression: {parsed}")
