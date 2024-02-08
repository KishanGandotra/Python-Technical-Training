from DAO.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl
from ENTITY.INCIDENT import Incident

def create_incident(crime_analysis_service):
    print("\nCreate Incident:")
    # Gather incident details from the user
    incident_id = input("Enter Incident ID: ")
    incident_type = input("Enter Incident Type: ")
    incident_date = input("Enter Incident Date (YYYY-MM-DD): ")
    location = input("Enter Location: ")
    description = input("Enter Description: ")
    status = input("Enter Status: ")
    victim_id = input("Enter Victim ID: ")
    suspect_id = input("Enter Suspect ID: ")

    # Create an Incident object with the gathered details
    new_incident = Incident(incident_id, incident_type, incident_date, location, description, status, victim_id, suspect_id)

    # Call the service to create the incident
    try:
        success = crime_analysis_service.create_incident(new_incident)
        if success:
            print("Incident created successfully.")
        else:
            print("Failed to create incident.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


def update_incident_status(crime_analysis_service):
    print("\nUpdate Incident Status:")
    incident_id = int(input("Enter Incident ID to update status: "))
    new_status = input("Enter new status: ")

    # Call the service to update the incident status
    try:
        success = crime_analysis_service.update_incident_status( new_status,incident_id)
        if success:
            print("Incident status updated successfully.")
        else:
            print("Failed to update incident status.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


def get_incidents_in_date_range(crime_analysis_service):
    print("\nGet Incidents in Date Range:")
    start_date = input("Enter Start Date (YYYY-MM-DD): ")
    end_date = input("Enter End Date (YYYY-MM-DD): ")

    # Call the service to get incidents within the date range
    try:
        incidents_in_range = crime_analysis_service.get_incidents_in_date_range(start_date, end_date)
        if incidents_in_range:
            print("Incidents within the date range:")
            for incident in incidents_in_range:
                print(incident)
        else:
            print("No incidents found within the date range.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


def search_incidents(crime_analysis_service):
    print("\nSearch Incidents:")
    criteria = input("Enter the criteria for searching incidents: ")

    # Call the service to search for incidents based on the provided criteria
    try:
        matching_incidents = crime_analysis_service.search_incidents(criteria)
        if matching_incidents:
            print("Incidents matching the criteria:")
            for incident in matching_incidents:
                print(incident)
        else:
            print(f"No incidents found matching the criteria '{criteria}'.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


def generate_incident_report(crime_analysis_service):
    print("\nGenerate Incident Report:")
    incident_id = input("Enter Incident ID to generate report: ")

    # Call the service to generate the incident report
    try:
        incident_report = crime_analysis_service.generate_incident_report(incident_id)
        if incident_report:
            print("Incident Report:")
            print(incident_report)
        else:
            print(f"No report generated for incident ID {incident_id}.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Assuming crime_analysis_service has a method named generate_incident_report
# which accepts an incident_id as a string and returns the incident report.



def create_case(crime_analysis_service):
    print("\nCreate Case:")
    case_description = input("Enter Case Description: ")
    incident_ids_input = int(input("Enter Incident ID:: "))

    # Call the service to create a new case and associate it with incidents
    try:
        return  crime_analysis_service.create_case(case_description, incident_ids_input)


    except Exception as e:
        print(f"Error occurred: {str(e)}")



def get_case_details(crime_analysis_service):
    print("\nGet Case Details:")
    case_id = input("Enter Case ID to get details: ")

    # Convert the case_id input to an integer
    case_id = int(case_id)

    # Call the service to get details of the specific case
    try:
        case_details = crime_analysis_service.get_case_details(case_id)
        # if case_details:
        #     print("Case Details:")
        #     print(f"Case ID: {case_details.case_id}")
        #     print(f"Description: {case_details.description}")
        #     print("Associated Incidents:")
        #     for incident_id in case_details.incident_ids:
        #         print(f"Incident ID: {incident_id}")
        # else:
        #     print(f"No details found for case ID {case_id}.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")



def update_case_details(crime_analysis_service):
    print("\nUpdate Case Details:")
    case_id = input("Enter Case ID to update details: ")
    new_description = input("Enter new description: ")

    # Call the service to update the case details
    try:
        success = crime_analysis_service.update_case_details(case_id, new_description)
        if success:
            print("Case details updated successfully.")
        else:
            print("Failed to update case details.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


def get_all_cases(crime_analysis_service):
    print("\nGet All Cases:")
    try:
        all_cases = crime_analysis_service.get_all_cases()
        if all_cases:
            print("List of All Cases:")
            for case in all_cases:
                for case in all_cases:
                    print(f"Case ID: {case['case_id']}, Description: {case['case_description']}")

        else:
            print("No cases found.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")


def main():
    # Create an instance of the CrimeAnalysisServiceImpl class
    crime_analysis_service = CrimeAnalysisServiceImpl()



    while True:
        print("\nCrime Analysis System Menu:")
        print("1. Create Incident")
        print("2. Update Incident Status")
        print("3. Get Incidents in Date Range")
        print("4. Search Incidents")
        print("5. Generate Incident Report")
        #print("6. Create Case")
        print("6. Get Case Details")
        print("7. Update Case Details")
        print("8. Get All Cases")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_incident(crime_analysis_service)
        elif choice == "2":
            update_incident_status(crime_analysis_service)
        elif choice == "3":
            get_incidents_in_date_range(crime_analysis_service)
        elif choice == "4":
            search_incidents(crime_analysis_service)
        elif choice == "5":
            generate_incident_report(crime_analysis_service)
        # elif choice == "6":
        #     create_case(crime_analysis_service)
        elif choice == "6":
            get_case_details(crime_analysis_service)
        elif choice == "7":
            update_case_details(crime_analysis_service)
        elif choice == "8":
            get_all_cases(crime_analysis_service)
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
