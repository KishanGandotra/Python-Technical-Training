class Report:
    def __init__(self, report_id, incident_id, reporting_officer, report_date, report_details, status):
        self.__report_id = report_id
        self.__incident_id = incident_id
        self.__reporting_officer = reporting_officer
        self.__report_date = report_date
        self.__report_details = report_details
        self.__status = status

    # Getters and setters
    def get_report_id(self):
        return self.__report_id

    def set_report_id(self, report_id):
        self.__report_id = report_id

    def get_incident_id(self):
        return self.__incident_id

    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id

    def get_reporting_officer(self):
        return self.__reporting_officer

    def set_reporting_officer(self, reporting_officer):
        self.__reporting_officer = reporting_officer

    def get_report_date(self):
        return self.__report_date

    def set_report_date(self, report_date):
        self.__report_date = report_date

    def get_report_details(self):
        return self.__report_details

    def set_report_details(self, report_details):
        self.__report_details = report_details

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"Report ID: {self.__report_id}, Incident ID: {self.__incident_id}, Reporting Officer: {self.__reporting_officer}, Report Date: {self.__report_date}, Report Details: {self.__report_details}, Status: {self.__status}"
