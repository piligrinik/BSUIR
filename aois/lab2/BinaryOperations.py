class BinaryOperations:
    def __init__(self):
        pass

    @classmethod
    def conjunction(cls, a: bool, b: bool):
        if a and b:
            return True
        else:
            return False

    @classmethod
    def disjunction(cls, a: bool, b: bool):
        if a or b:
            return True
        else:
            return False

    @classmethod
    def implication(cls, a: bool, b: bool):
        if a and not b:
            return False
        else:
            return True

    @classmethod
    def equivalence(cls, a: bool, b: bool):
        if a == b:
            return True
        else:
            return False

    @classmethod
    def negation(cls, a: bool):
        if a:
            return False
        else:
            return True
