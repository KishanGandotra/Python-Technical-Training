class Incident:
    def __init__(self, incident_id, incident_type, incident_date, location, description, status, victim_id, suspect_id):
        self.__incident_id = incident_id
        self.__incident_type = incident_type
        self.__incident_date = incident_date
        self.__location = location
        self.__description = description
        self.__status = status
        self.__victim_id = victim_id
        self.__suspect_id = suspect_id

    # Getters

    def get_incident_id(self) -> int:
        return self.__incident_id

    def get_incident_type(self) -> str:
        return self.__incident_type

    def get_incident_date(self) -> str:
        return self.__incident_date

    def get_location(self) -> str:
        return self.__location

    def get_description(self) -> str:
        return self.__description

    def get_status(self) -> str:
        return self.__status

    def get_victim_id(self) -> int:
        return self.__victim_id

    def get_suspect_id(self) -> int:
        return self.__suspect_id

    # Setters

    def set_incident_id(self, incident_id: int) -> None:
        self.__incident_id = incident_id

    def set_incident_type(self, incident_type: str) -> None:
        self.__incident_type = incident_type

    def set_incident_date(self, incident_date: str) -> None:
        self.__incident_date = incident_date

    def set_location(self, location: str) -> None:
        self.__location = location

    def set_description(self, description: str) -> None:
        self.__description = description

    def set_status(self, status: str) -> None:
        self.__status = status

    def set_victim_id(self, victim_id: int) -> None:
        self.__victim_id = victim_id

    def set_suspect_id(self, suspect_id: int) -> None:
        self.__suspect_id = suspect_id

    def __str__(self):
        return f"Incident ID: {self.__incident_id}, Type: {self.__incident_type}, Date: {self.__incident_date}, Location: {self.__location}, Description: {self.__description}, Status: {self.__status}, Victim ID: {self.__victim_id}, Suspect ID: {self.__suspect_id}"