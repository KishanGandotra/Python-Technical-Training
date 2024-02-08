# File: dao/CrimeAnalysisServiceImpl.py
from UTIL.db_connection import DBConnection
from typing import List
from ENTITY.INCIDENT import Incident
from ENTITY.CASE import Case
from DAO.ICrimeAnalysisService import ICrimeAnalysisService
import mysql.connector
from mysql.connector import Error


class CrimeAnalysisServiceImpl(ICrimeAnalysisService):
    connection = None  # Static variable for connection

    def __init__(self):
        # Assign the static variable `connection` by invoking the getConnection() method
        if CrimeAnalysisServiceImpl.connection is None:
            CrimeAnalysisServiceImpl.connection = DBConnection.getConnection()

    def create_incident(self, incident: Incident) -> bool:
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            sql = "INSERT INTO Incidents (IncidentID, IncidentType, IncidentDate, Location, Description, Status, VictimID, SuspectId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (
                incident.get_incident_id(), incident.get_incident_type(), incident.get_incident_date(),
                incident.get_location(), incident.get_description(), incident.get_status(),
                incident.get_victim_id(), incident.get_suspect_id()))
            CrimeAnalysisServiceImpl.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error occurred: {str(e)}")
            return False

    def update_incident_status(self, status , incident_id ) -> bool:
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            sql = "UPDATE Incidents SET Status = %s WHERE IncidentID = %s"
            cursor.execute(sql, (status, incident_id))
            CrimeAnalysisServiceImpl.connection.commit()
            cursor.close()
            return True
        except Error as e:
            print(f"Error occurred: {str(e)}")
            return False

    def get_incidents_in_date_range(self, start_date: str, end_date: str) -> List[Incident]:
        incidents = []
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            sql = "SELECT * FROM Incidents WHERE IncidentDate BETWEEN %s AND %s"
            cursor.execute(sql, (start_date, end_date))
            rows = cursor.fetchall()
            for row in rows:
                incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                incidents.append(incident)
            cursor.close()
        except Error as e:
            print(f"Error occurred: {str(e)}")
        return incidents

    def search_incidents(self, criteria: str) -> List[Incident]:
        incidents = []
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            sql = "SELECT * FROM Incidents WHERE IncidentType = %s OR Description LIKE %s"
            cursor.execute(sql, (criteria, f'%{criteria}%'))
            rows = cursor.fetchall()
            for row in rows:
                incident = Incident(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                incidents.append(incident)
            cursor.close()
        except Error as e:
            print(f"Error occurred: {str(e)}")
        return incidents

    def generate_incident_report(self, incident_id: str) -> str:
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            sql = "SELECT * FROM Incidents WHERE IncidentID = %s"
            cursor.execute(sql, (incident_id,))
            row = cursor.fetchone()
            report = ""
            if row:
                report += f"Incident ID: {row[0]}\n"
                report += f"Incident Type: {row[1]}\n"
                report += f"Incident Date: {row[2]}\n"
                report += f"Location: {row[3]}\n"
                report += f"Description: {row[4]}\n"
                report += f"Status: {row[5]}\n"
                report += f"Victim ID: {row[6]}\n"
                report += f"Suspect ID: {row[7]}\n"
                return report
            else:
                return "Incident not found."
        except Error as e:
            print(f"Error occurred: {str(e)}")
            return "Error generating report."

    def create_case(self, case_description, IncidentId):

        if self.checkIncidentId(IncidentId) is None:
            return "NoIncidentFound"
        try:
            print('hi')
            cursor = CrimeAnalysisServiceImpl.connection.cursor()
            sql_insert_case = "INSERT INTO cases(case_description, INCIDENTID) VALUES(%s, %s)"
            values= (case_description,IncidentId)
            result= cursor.execute(sql_insert_case,values)
            print('hello',result)
        except Exception as e:
            print("Exception: ", e)


    def checkIncidentId(self, incidentID):
        query = f"select * from Incidents where IncidentID={incidentID}"
        cursor = CrimeAnalysisServiceImpl.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        return result


    def get_case_details(self, case_id: int) -> Case:
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()

            # Retrieve case details from the database
            sql_get_case = "SELECT * FROM Cases WHERE case_id = %s"
            cursor.execute(sql_get_case, (case_id,))
            case_row = cursor.fetchone()

            if case_row:
                case_description = case_row[1]  # Assuming the description is stored in the second column
                incidents = []

                # Retrieve associated incidents for the case directly from the Incidents table
                sql_get_incidents = "SELECT *  FROM cases WHERE case_id = %s"
                cursor.execute(sql_get_incidents, (case_id,))
                incident_rows = cursor.fetchone()
                print(incident_rows)


        except Error as e:
            print(f"Error occurred: {str(e)}")
            return None

    def get_incident_by_id(self, incident_id: int) -> Incident:
        try:
            cursor = self.connection.cursor()
            sql = "SELECT * FROM Incidents WHERE IncidentID = %s"
            cursor.execute(sql, (incident_id,))
            row = cursor.fetchone()
            cursor.close()

            if row:
                # Construct and return an Incident object from the database row
                incident = Incident(incident_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                return incident
            else:
                return None
        except Error as e:
            print(f"Error occurred: {str(e)}")
            return None

    def update_case_details(self, case_id: int, new_description: str) -> bool:
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()

            # Update the case description in the Cases table
            sql_update_case = "UPDATE Cases SET case_description = %s WHERE case_id = %s"
            cursor.execute(sql_update_case, (new_description, case_id))

            # Commit the transaction and close the cursor
            CrimeAnalysisServiceImpl.connection.commit()
            cursor.close()

            return True

        except Error as e:
            print(f"Error occurred: {str(e)}")
            return False

    def get_all_cases(self) -> List[Case]:
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()

            # Retrieve all cases from the database
            sql_get_all_cases = "SELECT * FROM Cases"
            cursor.execute(sql_get_all_cases)
            case_rows = cursor.fetchall()

            all_cases = []


            # Iterate through case rows and construct Case objects
            for case_row in case_rows:
                print(case_row)
            #     case_id = case_row[0]  # Assuming the case ID is the first column
            #     case_description = case_row[1]  # Assuming the description is stored in the second column
            #
            #     # Fetch associated incidents for the current case
            #     incidents = self.get_incidents_for_case(case_id)
            #
            #     # Create a Case object with the retrieved details and associated incidents
            #     case_object = Case(case_id, case_description, incidents)
            #
            #     # Append the case object to the list of cases
            #     all_cases.append(case_object)
            #
            # # Close the cursor and return the list of Case objects
            # cursor.close()
            # return all_cases

        except Error as e:
            print(f"Error occurred: {str(e)}")
            return []


    def get_incidents_for_case(self, case_id: int) -> List[Incident]:
        try:
            cursor = CrimeAnalysisServiceImpl.connection.cursor()

            # Retrieve incidents associated with the given case_id from the database
            sql_get_incidents = "SELECT * FROM Incidents WHERE case_id = %s"

            cursor.execute(sql_get_incidents, (case_id,))
            incident_rows = cursor.fetchall()

            incidents = []

            # Iterate through incident rows and construct Incident objects
            for incident_row in incident_rows:
                # Assuming the structure of the incident_row matches the Incident class attributes
                incident = Incident(incident_row[0], incident_row[1], incident_row[2], incident_row[3], incident_row[4], incident_row[5], incident_row[6], incident_row[7])
                incidents.append(incident)

            # Close the cursor and return the list of Incident objects
            cursor.close()
            return incidents

        except Error as e:
            print(f"Error occurred: {str(e)}")
            return []
