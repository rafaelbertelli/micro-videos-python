class InvalidUuidException(Exception):
    def __init__(self, error="ID must be a valid UUID") -> None:
        super().__init__(error)


class ValidationException(Exception):
    def __init__(self, error="Validation error") -> None:
        super().__init__(error)
