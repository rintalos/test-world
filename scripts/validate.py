class Height:

    def __init__(self, value: float):
        if not (1.00 <= value <= 2.00):
            raise ValueError
        self.value = value


class Weight:
    def __init__(self, value: float):
        if not (30 <= value <= 150):
            raise ValueError
        self.value = value
