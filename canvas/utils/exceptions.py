class ResponseException(Exception):
    def __init__(self, message, status_code = 404, error_code = 1):
        self.status_code = status_code
        self.error_code = error_code
        self.message = message