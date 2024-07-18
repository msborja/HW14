import dataclasses


@dataclasses.dataclass
class Address:
    firstName: str
    lastName: str
    postalCode: int
