class LawEnforcementAgency:
    def __init__(self, agency_id, agency_name, jurisdiction, contact_information):
        self.__agency_id = agency_id
        self.__agency_name = agency_name
        self.__jurisdiction = jurisdiction
        self.__contact_information = contact_information

    # Getters and setters
    def get_agency_id(self):
        return self.__agency_id

    def set_agency_id(self, agency_id):
        self.__agency_id = agency_id

    def get_agency_name(self):
        return self.__agency_name

    def set_agency_name(self, agency_name):
        self.__agency_name = agency_name

    def get_jurisdiction(self):
        return self.__jurisdiction

    def set_jurisdiction(self, jurisdiction):
        self.__jurisdiction = jurisdiction

    def get_contact_information(self):
        return self.__contact_information

    def set_contact_information(self, contact_information):
        self.__contact_information = contact_information

    def __str__(self):
        return f"Agency ID: {self.__agency_id}, Name: {self.__agency_name}, Jurisdiction: {self.__jurisdiction}, Contact Information: {self.__contact_information}"
