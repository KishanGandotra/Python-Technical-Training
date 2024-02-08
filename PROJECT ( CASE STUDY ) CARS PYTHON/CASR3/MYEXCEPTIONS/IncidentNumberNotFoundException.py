# myexceptions/IncidentNumberNotFoundException.py

class IncidentNumberNotFoundException(Exception):
    """Exception raised when an invalid incident number is provided."""

    def __init__(self, message="Incident number not found"):
        self.message = message
        super().__init__(self.message)
