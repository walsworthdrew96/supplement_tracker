class SleepPeriod:
    def __init__(self):
        pass

    def __str__(self):
        rv = f"{self.__class__.__name__}:"
        for k, v in self.__dict__.items():
            rv += f"\t{k}: {v}"
        return rv
