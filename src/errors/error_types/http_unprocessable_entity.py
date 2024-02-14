class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str = "Unprocessable Entity"):
        super().__init__(message, 422)
        self.message = message
        self.name = "Unprocessable Entity"
        self.status_code = 422
