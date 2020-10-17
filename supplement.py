import datetime


class Nutrient:
    def __init__(self,
                 label_name: str = "No nutrient name",
                 chemical_name: str = "No chemical name",
                 amount: float = None,
                 unit: str = None):
        self.label_name = label_name
        self.chemical_name = chemical_name
        self.amount = amount
        self.unit = unit

    def __repr__(self):
        rv = f"{self.chemical_name}"
        return rv

    def __str__(self):
        rv = f"{self.__class__.__name__}:"
        for k, v in self.__dict__.items():
            rv += f"\t{k}: {v}"
        return rv


class Supplement:
    def __init__(self, name: str = "No Supplement name", nutrients=None):
        self.name = name
        self.nutrients = nutrients

    def __repr__(self):
        rv = f"{self.name}"
        return rv

    def __str__(self):
        rv = f"{self.__class__.__name__}:"
        for k, v in self.__dict__.items():
            rv += f"\t{k}: {v}"
        return rv


class Dose:
    def __init__(self, date: datetime.datetime, supplement: Supplement, servings: int):
        self.date = date
        self.supplement = supplement
        self.servings = servings

    def __repr__(self):
        rv = f"{self.__class__.__name__}:"
        for k, v in self.__dict__.items():
            rv += f"\t{k}: {v}"
        return rv

    def __str__(self):
        rv = f"{self.__class__.__name__}:"
        for k, v in self.__dict__.items():
            rv += f"\t{k}: {v}"
        return rv
