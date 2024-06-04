class LogOps:
    def __init__(self):
        pass

    def return_value(self, function_string, value1, value2) -> int:
        match function_string:
            case '4':
                return self.f4(value1, value2)
            case '6':
                return self.f6(value1, value2)
            case '9':
                return self.f9(value1, value2)
            case '11':
                return self.f11(value1, value2)
    # 0011100000010000
    # 0010000000110001
    # 1110011111111111
    @staticmethod
    def f4(value1, value2) -> int:
        return int(not bool(value1) and bool(value2))

    def f6(self, value1, value2) -> int:
        return int(bool(self.f4(value1, value2)) or
                   bool(self.f4(value2, value1)))

    @staticmethod
    def f9(value1, value2) -> int:
        return int((bool(value1) and bool(value2)) or (not bool(value1) and not bool(value2)))

    @staticmethod
    def f11(value1, value2) -> int:
        return int(bool(value1) or not bool(value2))
