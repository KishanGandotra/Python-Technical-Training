from DAO.ICrimeAnalysisService import ICrimeAnalysisService
from UTIL.db_connection import DBConnection
from MYEXCEPTIONS import IncidentNumberNotFoundException
import mysql.connector

from typing import Collection
from DAO.ICrimeAnalysisService import ICrimeAnalysisService
from ENTITY.INCIDENT import Incident
from ENTITY.REPORT import Report
from ENTITY.CASE import Case
from ENTITY.INCIDENTTYPE import IncidentType
from UTIL.db_connection import DBConnection

class CrimeAnalysisServiceImpl(ICrimeAnalysisService):
    connection = None

    def __init__(self):
        self.connection = DBConnection.getConnection()

    def create_incident(self, incident: Incident) -> bool:
        # Implement logic to create incident
        # Example: SQL query to insert incident into database
        cursor = self.connection.cursor()
        query = "INSERT INTO Incidents (IncidentType, IncidentDate, Location, Description, Status, VictimID, SuspectId) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (incident.incident_type, incident.incident_date, incident.location, incident.description, incident.status, incident.victim_id, incident.suspect_id)
        cursor.execute(query, values)
        self.connection.commit()
        return True

    def update_incident_status(self, status: str, incident_id: int) -> bool:
        # Implement logic to update incident status
        # Example: SQL query to update incident status in database
        cursor = self.connection.cursor()
        query = "UPDATE Incidents SET Status = %s WHERE IncidentID = %s"
        values = (status, incident_id)
        cursor.execute(query, values)
        self.connection.commit()
        return True

    def get_incidents_in_date_range(self, start_date: str, end_date: str) -> Collection[Incident]:
        # Implement logic to get incidents in date range
        # Example: SQL query to fetch incidents from database within date range
        cursor = self.connection.cursor()
        query = "SELECT * FROM Incidents WHERE IncidentDate BETWEEN %s AND %s"
        values = (start_date, end_date)
        cursor.execute(query, values)
        incidents = []
        for row in cursor.fetchall():
            incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

            incidents.append(incident)
        return incidents

    def search_incidents(self, criteria: IncidentType) -> Collection[Incident]:
        cursor = self.connection.cursor()
        query = "SELECT * FROM Incidents WHERE IncidentType = %s"
        cursor.execute(query, (criteria,))
        incidents = []
        for row in cursor.fetchall():
            # Here you are trying to initialize an Incident object with 8 arguments
            incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8])
            incidents.append(incident)
        return incidents

    def generate_incident_report(self, incident: Incident) -> Report:
        # Implement logic to generate incident report
        # Example: Generate report object based on incident details
        report = Report(incident.incident_id, incident.description, incident.location, incident.incident_date)
        return report

    def create_case(self, case_description: str, incidents: Collection[Incident]) -> Case:
        # Implement logic to create case and associate it with incidents
        # Example: SQL query to insert case into database and associate with incidents
        cursor = self.connection.cursor()
        query = "INSERT INTO Cases (CaseDescription) VALUES (%s)"
        values = (case_description,)
        cursor.execute(query, values)
        case_id = cursor.lastrowid
        for incident in incidents:
            query = "UPDATE Incidents SET CaseID = %s WHERE IncidentID = %s"
            values = (case_id, incident.incident_id)
            cursor.execute(query, values)
        self.connection.commit()
        case = Case(case_id, case_description, incidents)
        return case

    def get_case_details(self, case_id: int) -> Case:
        # Implement logic to get case details by case ID
        # Example: SQL query to fetch case details from database by case ID
        cursor = self.connection.cursor()
        query = "SELECT * FROM Cases WHERE case_id = %s"
        cursor.execute(query, (case_id,))
        row = cursor.fetchone()
        if row:
            case = Case(row[0], row[1], [])
            return case
        else:
            return None

    def update_case_details(self, case: Case) -> bool:
        # Implement logic to update case details
        # Example: SQL query to update case details in database
        cursor = self.connection.cursor()
        query = "UPDATE Cases SET CaseDescription = %s WHERE CaseID = %s"
        values = (case.case_description, case.case_id)
        cursor.execute(query, values)
        self.connection.commit()
        return True

    def get_all_cases(self) -> Collection[Case]:
        # Implement logic to get all cases
        # Example: SQL query to fetch all cases from database
        cursor = self.connection.cursor()
        query = "SELECT * FROM Cases"
        cursor.execute(query)
        cases = []
        for row in cursor.fetchall():
            case = Case(row[0], row[1], [])
            cases.append(case)
        return cases


    def get_incident_details(self, incident_id: int) -> Incident:
        """
        Retrieves incident details based on the incident ID.
        """
        cursor = self.connection.cursor()
        query = "SELECT * FROM Incidents WHERE IncidentID = %s"
        cursor.execute(query, (incident_id,))
        row = cursor.fetchone()
        if row:
            incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            return incident
        else:
            return None