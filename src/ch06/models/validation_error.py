class ValidationError(Exception):
    def __init__(self, error_message: str, status_code: int) -> None:
        super().__init__(error_message)

        self.status_code = status_code
        self.error_message = error_message
