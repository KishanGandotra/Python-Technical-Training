class Report:
    def __init__(self, report_id: int, incident_id: int, reporting_officer: int, report_date: str, report_details: str, status: str):
        self.__report_id = report_id
        self.__incident_id = incident_id
        self.__reporting_officer = reporting_officer
        self.__report_date = report_date
        self.__report_details = report_details
        self.__status = status

    # Getter methods
    def get_report_id(self) -> int:
        return self.__report_id

    def get_incident_id(self) -> int:
        return self.__incident_id

    def get_reporting_officer(self) -> int:
        return self.__reporting_officer

    def get_report_date(self) -> str:
        return self.__report_date

    def get_report_details(self) -> str:
        return self.__report_details

    def get_status(self) -> str:
        return self.__status

    # Setter methods
    def set_report_id(self, report_id: int):
        self.__report_id = report_id

    def set_incident_id(self, incident_id: int):
        self.__incident_id = incident_id

    def set_reporting_officer(self, reporting_officer: int):
        self.__reporting_officer = reporting_officer

    def set_report_date(self, report_date: str):
        self.__report_date = report_date

    def set_report_details(self, report_details: str):
        self.__report_details = report_details

    def set_status(self, status: str):
        self.__status = status
