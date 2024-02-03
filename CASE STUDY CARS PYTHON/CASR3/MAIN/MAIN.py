# Import necessary modules and classes
from DAO.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from ENTITY.INCIDENT import Incident

# Create an instance of your service implementation class
crime_analysis_service = CrimeAnalysisServiceImpl()

# Define the incident ID you want to retrieve
incident_id = 103

try:
    # Call the method to retrieve incident details based on the incident ID
    incident = crime_analysis_service.get_incident_details(incident_id)

    # Check if the incident details are retrieved successfully
    if incident:
        # Print the incident details
        print("Incident Details:")
        print(f"Incident ID: {incident.get_incident_id()}")
        print(f"Description: {incident.get_description()}")
        print(f"Incident Date: {incident.get_incident_date()}")
        print(f"Incident Type: {incident.get_incident_type()}")  # Print incident type
        # Add more fields as needed

    else:
        print(f"No incident found with ID: {incident_id}")

except Exception as e:
    print(f"Error occurred: {str(e)}")
